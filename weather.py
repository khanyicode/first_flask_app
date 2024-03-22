
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_lan_lon(city_name, state_name, country_code, API_key):
    resp = requests.get('http://api.openweathermap.org/geo/1.0/direct', params={'q': f'{city_name},{state_name},{country_code}', 'appid': API_key}).json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_current_conditions(lon, lat, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}').json()
    print(resp)

if __name__ == "__main__":
    lat, lon = get_lan_lon('Toronto', 'Ontario', 'Canada', api_key)
    get_current_conditions(lon, lat, api_key)