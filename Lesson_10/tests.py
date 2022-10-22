import datetime
import exchange_rates_convertor



def test_date_today():
    assert type(exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d')) == str, 'Not a string'
    assert len(exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d')) == 10, 'has wrong length'
    assert exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d').split('-')[0][:3] == '202', 'next epoch'
    assert len(exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d').split('-')[0]) == 4, 'wrong year'
    assert int(exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d').split('-')[1]) < 13, 'wrong month'
    assert int(exchange_rates_convertor.get_todays_date().strftime('%Y-%m-%d').split('-')[2]) < 32, 'wrong date'
    #assert type(exchange_rates_convertor.get_todays_date()) == datetime.datetime


def test_get_current_date_str_format():
    assert type(exchange_rates_convertor.get_todays_date_str_format()) == str, 'Not a string'
    assert len(exchange_rates_convertor.get_todays_date_str_format()) == 10, 'has wrong length'
    assert exchange_rates_convertor.get_todays_date_str_format().split('-')[0][:3] == '202', 'next epoch'
    assert len(exchange_rates_convertor.get_todays_date_str_format().split('-')[0]) == 4, 'wrong year'
    assert int(exchange_rates_convertor.get_todays_date_str_format().split('-')[1]) < 13, 'wrong month'
    assert int(exchange_rates_convertor.get_todays_date_str_format().split('-')[2]) < 32, 'wrong date'
    assert type(exchange_rates_convertor.get_todays_date_str_format()) == str


def test_is_valid_user_date_format_function():
    assert not exchange_rates_convertor.is_valid_input_date_format('2022-220022-2020-2020')
    assert not exchange_rates_convertor.is_valid_input_date_format('1080-12-12')
    assert not exchange_rates_convertor.is_valid_input_date_format('100000-12-12')
    assert not exchange_rates_convertor.is_valid_input_date_format('2022-0-12')
    assert not exchange_rates_convertor.is_valid_input_date_format('2020-14-12')
    assert not exchange_rates_convertor.is_valid_input_date_format('2020-12-122')
    assert not exchange_rates_convertor.is_valid_input_date_format('2020-12-0')
    assert not exchange_rates_convertor.is_valid_input_date_format('2020-02-30')
    assert exchange_rates_convertor.is_valid_input_date_format('2020-01-30')
    assert not exchange_rates_convertor.is_valid_input_date_format('2021-02-29')
    assert not exchange_rates_convertor.is_valid_input_date_format('')


if __name__ == '__main__':
    test_date_today()
    test_is_valid_user_date_format_function()
    test_get_current_date_str_format()
