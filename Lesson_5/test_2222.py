import pymongo
import datetime
import mongo_db_functions
import get_api_url_task_3
import functions_task2

token = pymongo.MongoClient("mongodb+srv://bsavchuk1:Karabra123@cluster0.pazmk7c.mongodb.net/?retryWrites=true&w=majority")


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=ap44tkfEZmXZcNHVNsU4aVWT0IHYFLDW4CoHcxSROM-NAkpyHXXhz9nYOZ96soADFCb_g0F63V9et7DOgccTPq2S18C6uWtom5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnIKv156aVe9gXafo6LGLJD9yP5ElTzOQHH9qtO0HXe8bawI963vOO6aeoaLX1ZkT1a0dFM1DI83ZDm12Y77X02w1cuA8a3DlH9z9Jw9Md8uu&lib=M8ecTaJYwdwgxxRi_V4BJsJ7pVMj42q0Z'
now = datetime.datetime.now().date()

my_functions_for_mongodb = {
    1: get_api_url_task_3.school_high_scores,
    2: mongo_db_functions.data_write_to_file,
    3: mongo_db_functions.message_for_db
}

data_with_message = my_functions_for_mongodb[1](functions_task2.get_data(url))
data_write_to_file = my_functions_for_mongodb[2](data_with_message)


db = token.students
coll = db.high_grade_students_task_4
add_data_to_db = my_functions_for_mongodb[3](data_with_message, data_write_to_file)
coll.insert_many(add_data_to_db)