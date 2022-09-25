import requests
import pprint

URL = 'https://script.google.com/macros/s/AKfycbw3saekZVjatrQ1VfFjgk8kBmI-LtrgB6gePE4JVpmMw9p8LHpcnOckpxFs1HT_Lhf1qA/exec'
URL_DUMMY = 'https://dummyjson.com/carts'
#response = requests.get(URL)
#data = response.json()
#print(data)
#pprint.pprint(data)


def get_data(url: str = None) -> dict:
   """
   get data from given url
   :param url : str
   :return: dict

   """
   response = requests.get(url)
   data = response.json()

   return data





pprint.pprint(get_data(URL))
pprint.pprint(get_data(URL_DUMMY))
