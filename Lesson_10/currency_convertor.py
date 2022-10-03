import json

URL = 'https://api.exchangerate.host/convert'




def currency_validation(currency_from: str, currency_to: str) -> bool:
    with open('symbols.json', 'r') as symbols:
        data = json.load(symbols)
        if currency_from in data['symbols'] and currency_to in data['symbols']:
            return True
        return False
