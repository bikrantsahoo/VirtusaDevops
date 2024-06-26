RATES = {
    "AUDUSD": 0.8371,
    "CADUSD": 0.8711,
    "USDCNY": 6.1715,
    "EURUSD": 1.2315,
    "GBPUSD": 1.5683,
    "NZDUSD": 0.7750,
    "USDJPY": 119.95,
    "EURCZK": 27.6028,
    "EURDKK": 7.4405,
    "EURNOK": 8.6651,
}

# Precision
PRECISION = {
    "AUD": 2,
    "CAD": 2,
    "CNY": 2,
    "CZK": 2,
    "DKK": 2,
    "EUR": 2,
    "GBP": 2,
    "JPY": 0,
    "NOK": 2,
    "NZD": 2,
    "USD": 2,
}

# Conversion matrix
CONVERSION_MATRIX = {
    'AUD': {'USD': 'D'},
    'CAD': {'USD': 'D'},
    'CNY': {'USD': 'D'},
    'CZK': {'USD': 'EUR'},
    'DKK': {'EUR': 'D'},
    'EUR': {'USD': 'D'},
    'GBP': {'USD': 'D'},
    'JPY': {'USD': 'D'},
    'NOK': {'EUR': 'D'},
    'NZD': {'USD': 'D'},
    'USD': {'EUR': 'D'}
}
