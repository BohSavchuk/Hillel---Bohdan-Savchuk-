import exchange_rates_convertor



URL = 'https://api.exchangerate.host/convert'


exchange_rates_functions = {

    1: exchange_rates_convertor.get_todays_date(),
    2: exchange_rates_convertor.convertor,
    3: exchange_rates_convertor.save_as_csv
}

convert = exchange_rates_functions[2]('UAH', 'USD', 100.00, '2022-09-10')
add_as_csv = exchange_rates_functions[2](convert, True)
