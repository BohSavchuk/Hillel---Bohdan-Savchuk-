import functions_task2
import message
import datetime
import get_api_url_task_3
import mongoDB_config
import pymongo

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=ap44tkfEZmXZcNHVNsU4aVWT0IHYFLDW4CoHcxSROM-NAkpyHXXhz9nYOZ96soADFCb_g0F63V9et7DOgccTPq2S18C6uWtom5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIKv156aVe9gXafo6LGLJD9yP5ElTzOQHH9qtO0HXe8bawI963vOO6aeoaLX1ZkT1a0dFM1DI83ZDm12Y77X02w1cuA8a3DlH9z9Jw9Md8uu&lib=M8ecTaJYwdwgxxRi_V4BJsJ7pVMj42q0Z'
now = datetime.datetime.now().date()


#написати функцію, яка підєднується за токеном до бази даних, створює базу даних, колекцію.
def create_db_collection (token) -> None:
    """
    Create DB and Collection
    Args:
        token:

    Returns:

    """
    mongoDB_config.coll.insert_one({"name": "task_4"})



#доробити функцію з завдання 3: якщо bd True, то ми формуємо ту ж стрічку(проте без смайла, можете передбачити в колекції смайлів смайл як пуста
#стрічка), і записуємо в базу даних або по одному валідні json дані, або ж
#добавляємо їх в список  і використовуємо insert_many
#зауважте, що ви відправляєте замість notes тест нашої стрічки до 150 символів,
#інші поля залишаються без змін


def data_write_to_file(data,bd:bool = True, lenght: int = 150):
    new_file = open('Good_students.txt','a+')
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


#напишіть функцію, котра отримує всі дані з бази даних (назва бд та колекції
#у вас в конфігах)

def data_from_db():
    """
    getting data from MongoDB
    Returns:

    """
    token = pymongo.MongoClient( "mongodb+srv://bsavchuk1:Karabra123@cluster0.pazmk7c.mongodb.net/?retryWrites=true&w=majority")
    db = token.students
    coll = db.high_grade_students
    data_db = []
    for items in coll.find():
        data_db.append(items)
    return data_db

data_from_db()





