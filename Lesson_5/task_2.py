from typing import Any

import requests
import pprint

#створіть функцію для перевірки, що за замовчуванням число не менше 0 та не  більше 100 (потрібно, щоб верхня та нижня межа могли налаштовуватися)


def min_max_value(integer: int, min_value=0, max_value=100) -> bool:
    """

  #  Args:
   #     integer: int

    #Returns:
     #   data (True|False)

    """
    variable = integer
    if min_value < variable < max_value:
       return True
    return False

assert min_max_value(99) == True
assert min_max_value(123) == False
assert type(min_max_value(1)) == int




# Cтворіть функцію для перевірки, що отриманий аргумент є числом (інт)
def is_int(value: Any) -> bool:
    """

    Args:
        integer(int):

    Returns:
        data (True|False)
    """
    if type(value) == int and type(value) != bool:
        return True
    return False


assert is_int(1) is True
assert is_int('asdsa') is False, 'not int'
assert is_int(True) is False, 'not int'





# Получаем стринг возращаем json. (валідувати не потрібно, ми поки що працюємо з даними, вважаючи,що вони валідні)

URL = 'https://dummyjson.com/carts'


def get_data(url: str = None) -> dict:
    """
      Args:
          url: str

      Returns: dict
      """
    response = requests.get(url)
    data = response.json()
    return data

assert type(get_data(URL)) == dict,'not json (dict)'

# створити функцію, яка приймає стрічку, і має її повернути, враховуючи , що ця
# стрічка має бути довжиною не більше 150 символів (може регулюватися через
# передачу аргумента функції), а якщо отримана стрічка буде довшою за 150
# символів, то стрічка має бути обрізана до 150 символів, причому останні
# три символи мають бути ... (трьома крапками)


def get_cut_string(string: str, length=150) -> str:
    """
    The function return
      Args:
          string (str):str
          length(int): default value 150

       Returns:str

      """
    if len(string) <= length:
        return string
    else:
        cut_string = string[:length-3] + '...'
        return cut_string


assert type(get_cut_string("a")) == str, "is not string"
assert len(get_cut_string("a"*100)) == 100
assert len(get_cut_string("a"*200)) == 150
assert get_cut_string("a"*200)[-3:] == '...'





#написати функцію, котра дозаписує (режим "а") в файл певні текстові дані

def add_to_file (path_to_file: str = 'task_file.txt', data = 'task 2'):
    with open(path_to_file,'a', encoding='utf-8') as file:
        file.write(data)






