from currency_converter.data import RATES, PRECISION, CONVERSION_MATRIX

class CurrencyConverter:
    def __init__(self):
        self.rates = RATES
        self.precision = PRECISION
        self.conversion_matrix = CONVERSION_MATRIX

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return round(amount, self.precision[to_currency])
        
        rate = self.get_rate(from_currency, to_currency)
        if not rate:
            return None
        
        converted_amount = amount * rate
        return round(converted_amount, self.precision[to_currency])
    
    def get_rate(self, from_currency, to_currency):
        # Direct rate
        direct_rate_key = from_currency + to_currency
        if direct_rate_key in self.rates:
            return self.rates[direct_rate_key]
        
        # Inverse rate
        inverse_rate_key = to_currency + from_currency
        if inverse_rate_key in self.rates:
            return 1 / self.rates[inverse_rate_key]
        
        # Cross via another currency
        cross_currency = self.conversion_matrix.get(from_currency, {}).get(to_currency)
        if not cross_currency:
            return None
        
        if cross_currency == 'D':
            return None
        
        rate1 = self.get_rate(from_currency, cross_currency)
        rate2 = self.get_rate(cross_currency, to_currency)
        if rate1 and rate2:
            return rate1 * rate2
        
        return None
