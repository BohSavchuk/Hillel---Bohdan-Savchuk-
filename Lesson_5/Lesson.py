import requests
import pprint

URL = 'https://script.google.com/macros/s/AKfycby3JjZFwGfrbIVGMuAKgpjngtvUddIfT6BtZxzO18N30BSCd2P7imyZKMFBZbCHWObfDg/exec'

#response = requests.get(URL)
#data = response.json()
#print(data)
#pprint.pprint(data)


def get_data(url: str = No ne):
   response = requests.get(URL)
   data = response.json()

   return data

pprint.pprint(get_data(URL))