import requests
import logging
from secrets import get_secret_key

logging.basicConfig(filename="requests.log", level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.basicConfig(filename="errors.log", level=logging.ERROR, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

WEATHER_URL = "https://community-open-weather-map.p.rapidapi.com/weather"
HEADERS = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': get_secret_key()
    }

querystring = {
    "lang":"null",
    "units":"imperial",
    "mode":"JSON"
}

def get_message(data):
    if data["cod"] == "200":
        message = f"It is currently {data['main']['temp']} degrees in {data['name']}, {data['sys']['country']}."
    else:
        message = data["message"]

    return message

def fetch_weather_data(user_input):
    querystring.update(q=user_input)
    response = requests.get(WEATHER_URL, headers=HEADERS, params=querystring)
    data = response.json()
    logger.info(f"User entered: {user_input}")
    logger.info(f"Got response: {data}")
    return data

if __name__ == '__main__':
    key = get_secret_key()
    while True:
        user_input = input("Enter city name to get the current weather, or enter q to quit\n")
        if user_input == "q":
            exit()
        else:
            try:
                data = fetch_weather_data(user_input)
                message = get_message(data)
                print(message)
                print("\n")
            except Exception as exc:
                logger.error(f"User entered: {user_input} - {exc}")
                print("Something went wrong fetching data. Please try again.")
                print("\n")

