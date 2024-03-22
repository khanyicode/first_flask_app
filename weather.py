import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_lan_lon(city_name, state_name, country_code, API_key):
    resp = requests.get('http://api.openweathermap.org/geo/1.0/direct', params={'q': f'{city_name},{state_name},{country_code}', 'appid': API_key}).json()
    print(resp)

get_lan_lon('Toronto', 'Ontario', 'Canada', api_key)