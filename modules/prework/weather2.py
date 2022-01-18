import requests

# instead of copying and pasing to read the json, use pprint
from pprint import pprint


def get_weather_desc_and_temp():
    api_key = "e8f4fe52cc1d091a4e177b516d2e458d"
    city = "Louisville"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid="
        + api_key
    )

    request = requests.get(url)
    json = request.json()
    # pprint(json)

    description = json.get("weather")[0].get("description")
    print("Today's force is", description)

    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        "description": description,
        "temp_min": temp_min,
        "temp_max": temp_max,
    }


def main():
    weather_dict = get_weather_desc_and_temp()

    # Note `.get()` and direct access `dict["key"]` are interchangable
    # `.get()` returns `None` where direct access raises a failure`
    print("Today's forecase is", weather_dict.get("description"))
    print("The minimum temperator is", weather_dict.get("temp_min"))
    # example direct access into the dictionary object
    print("The maximum temperator is", weather_dict["temp_max"])


main()
