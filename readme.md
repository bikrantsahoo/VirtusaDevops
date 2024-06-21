# Currency Converter App

A command line application to convert currencies based on given rates using python

## Features
This has mutiple features.
- Conversion between multiple currencies.
- Handles direct, inverse, and cross-currency conversions.
- Supports precision for different currencies.

## Installation

Clone the repository and install the dependencies:

git clone https://github.com/bikrantsahoo/VirtusaDevops.git
cd currency_converter
pip install -r requirements.txt


##usage

python -m currency_converter.cli 100 AUD USD
python -m unittest discover tests


##Containerise

docker build -t currency_converter .
docker run --rm currency_converter 100 AUD USD


