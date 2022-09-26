def zip_function (tuple_1, tuple_2):
    """
    Function receive 2 tupples and transforms them into 1 dict
    Args:
        tuple_1(tuple):
        tuple_2(tuple):

    Returns:

    """
    data = list(zip(tuple_1, tuple_2))
    return data

tuple_1 = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
tuple_2 = (('BTC', 'ETH', 'XRP', 'LTC'))

print(zip_function(tuple_1,tuple_2))


