import requests
import pprint

URL_GOOGLE_API = 'https://script.google.com/macros/s/AKfycbw3saekZVjatrQ1VfFjgk8kBmI-LtrgB6gePE4JVpmMw9p8LHpcnOckpxFs1HT_Lhf1qA/exec'


def get_data(url: str = None) -> dict:

    response = requests.get(url)
    data = response.json()

    return data

#Name as config