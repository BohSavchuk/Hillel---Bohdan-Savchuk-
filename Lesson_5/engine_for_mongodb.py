import functions_task2
import message
import datetime

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=ap44tkfEZmXZcNHVNsU4aVWT0IHYFLDW4CoHcxSROM-NAkpyHXXhz9nYOZ96soADFCb_g0F63V9et7DOgccTPq2S18C6uWtom5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIKv156aVe9gXafo6LGLJD9yP5ElTzOQHH9qtO0HXe8bawI963vOO6aeoaLX1ZkT1a0dFM1DI83ZDm12Y77X02w1cuA8a3DlH9z9Jw9Md8uu&lib=M8ecTaJYwdwgxxRi_V4BJsJ7pVMj42q0Z'
now = datetime.datetime.now().date()







def add_to_file_db(url):
    """
    Function Write file to DB
    Args:
        data: list
        file_name: str
        db: True/False


    Returns: True/False

    """

    google_data = functions_task2.get_data(url)['data']
    for dictionary in google_data:
        age = dictionary['age']
        rewards = dictionary['has_rewards']
        score = dictionary['score']
        name = dictionary['name']
        notes = dictionary['notes']

        if score >= 90 and rewards and 9 <= age <= 18:
            result_string = functions_task2.get_cut_string(message.message.format(now, name, score, notes))
            data = result_string
    return data






def data_write_to_file(data,name_of_file, bd:bool = True, lenght: int = 150)
    new_file = open(name_of_file,'a+')
    for item in data:
        if len(item['message']) > lenght:
            edited_item = item['message'][:150]
            new_file.write(edited_item +'\n')
        else:
            new_file.write(edited_item + '\n')
    new_file.close()
    db=True
    return db






def message_for_db (data, db:bool, lenght = 150) -> list:
    """

    Args:
        data:list
        db:True/False
        lenght: int

    Returns: list
    """
    if db:
        for item in data:
            item['message'] = message.db_message.format(now, item['name'], item['score'], item['note'])
            if len(item['message']) > lenght:
                item['message'] = item['message'][:lenght]
    return data









def create_file_db(path_to_file: str = 'high_grade_students_db.txt', data: str = ''):
    """
    Function open file and added 'task 2' text
    Args:
        path_to_file:
        data:

    Returns:
    """

    with open(path_to_file, 'a', encoding='utf-8') as file:
        file.write(data + '\n')




def add_to_file_db(url):
    """
    Function Write file to DB
    Args:
        data: list
        file_name: str
        db: True/False


    Returns: True/False

    """

    google_data = functions_task2.get_data(url)['data']
    for dictionary in google_data:
        age = dictionary['age']
        rewards = dictionary['has_rewards']
        score = dictionary['score']
        name = dictionary['name']
        notes = dictionary['notes']

        if score >= 90 and rewards and 9 <= age <= 18:
            result_string = functions_task2.get_cut_string(message.message.format(now, name, score, notes))
        mongoDB_config



def message_for_db(data, db:bool, lenght = 150) -> list:
    """
    Args:
        data:list
        db:True/False
        lenght: int

    Returns: list
    """
    if db:
        for item in data:
            item['message'] = message.db_message.format(now, item['name'], item['score'], item['note'])
            if len(item['message']) > lenght:
                item['message'] = item['message'][:lenght]
    return data



