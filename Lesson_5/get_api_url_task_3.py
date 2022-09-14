##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створити функцію, котра приймає урл (та опційний параметр bd булевого формату
для завдання 4), і очікує там словник з ключами, описаними в завданні 1
в функції перевіряється, що якщо в учня бали від 90 до 100, учень має
винагороди, його вік від 9 до 18 років, то формуємо стрічку типу:

"[Запит від {}] Учень {імя} {смайл} є відмінником, його бал {бал},
відзначимо, що {примітки}"

стрічку обрізаємо до 150 символів і добавляємо в файл
поле запит від в стрічці формуємо використанням коду
import datetime
now = datetime.datetime.now().date()
після імені учня вставте смайл на ваш вибір (список смайлів має зберігатися
окремо в файлі)
"""


import message
import functions
import requests
import pprint
import datetime


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=ap44tkfEZmXZcNHVNsU4aVWT0IHYFLDW4CoHcxSROM-NAkpyHXXhz9nYOZ96soADFCb_g0F63V9et7DOgccTPq2S18C6uWtom5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIKv156aVe9gXafo6LGLJD9yP5ElTzOQHH9qtO0HXe8bawI963vOO6aeoaLX1ZkT1a0dFM1DI83ZDm12Y77X02w1cuA8a3DlH9z9Jw9Md8uu&lib=M8ecTaJYwdwgxxRi_V4BJsJ7pVMj42q0Z'
now = datetime.datetime.now().date()



def school_high_scores(url) -> None:
    google_data = functions.get_data(url)['data']
    for dictionary in google_data:
        age = dictionary['age']
        rewards = dictionary['has_rewards']
        score = dictionary['score']
        name = dictionary['name']
        notes = dictionary['notes']

        if score >= 90 and rewards and 9 <= age <= 18:
            result_string = functions.get_cut_string(message.message.format(now, name, message.face_smile, score, notes))
            functions.add_to_file(data=result_string)

school_high_scores(url)




