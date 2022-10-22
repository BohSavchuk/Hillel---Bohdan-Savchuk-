import requests
from datetime import datetime as dt
import json
import calendar
import sys
import csv


URL = 'https://api.exchangerate.host/convert'




def currency_validation(currency_from: str, currency_to: str) -> bool:
    with open('symbols.json', 'r') as symbols:
        data = json.load(symbols)
        if currency_from in data['symbols'] and currency_to in data['symbols']:
            return True
        return False



def get_todays_date() -> dt.date:
    """Return current data"""
    date_today = dt.now().date()
    return date_today




def get_todays_date_str_format() -> str:
    """Return current data in '%Y-%m-%d' format"""
    date_today = dt.now().strftime('%Y-%m-%d')
    return date_today




def get_data_from_user_terminal():
    """data from CLI"""
    return sys.argv[1:]



def is_valid_input_date_format (value) -> bool:
    """Expect date in format data in str format %Y-%m-%d"""
    if not value:
        return False

    try:
        year, month, day = [int(value) for value in value.split('-')]
    except Exception:
        return False

    is_valid_year = False
    is_valid_month = False
    is_valid_day = False

    if 1919 < year < 9999:
        is_valid_year = True

    if 0 < month < 13:
        is_valid_month = True

    if all([calendar.isleap(year), month == 2, (0 < day <= 29)]):
        is_valid_day = True
    elif all([calendar.isleap(year), month == 2, (0 < day <= 28)]):
        is_valid_day = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and (0 < day <= 31):
        is_valid_day = True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        is_valid_day = True

    return all([is_valid_year, is_valid_month, is_valid_day])


def get_date_for_currency_rate() -> str:
    user_data = get_data_from_user_terminal()
    day_today = get_todays_date()
    if user_data:
        is_valid_date_format = is_valid_input_date_formate(*user_data)
        if is_valid_date_format:
            date = dt(*[int(value) for value in user_data[0].split('-')])
        else:
            date = day_today
    else:
        date = day_today

    if date <= day_today:
        return date.strftime('%Y-%m-%d')

    return day_today.strftime('%Y-%m-%d')


def convertor(c_from: str, c_to: str, amount: float, date: str):
    if currency_validation(c_from, c_to):
        valid_date = get_date_for_currency_rate(date)
        result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
        for day in valid_date:
            data = requests.get(URL, params={'from': c_from, 'to': c_to, 'amount': str(amount), 'date': day})
            response = data.json()
            converter_result = []
            converter_result.append(response['date'])
            converter_result.append(response['query']['from'])
            converter_result.append(response['query']['to'])
            converter_result.append(response['query']['amount'])
            converter_result.append(response['info']['rate'])
            converter_result.append(response['result'])
            result.append(converter_result)
        return result
    else:
        return print('Wrong format.Right format should be %Y-%m-%d. Check and try again')


def save_as_csv(result: list, save: bool):
    if save:
        with open('currency_exchange.csv', 'w') as csv_file:
            data = csv.writer(csv_file)
            data.writerows(result)



