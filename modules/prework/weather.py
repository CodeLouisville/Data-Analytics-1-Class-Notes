import requests

# instead of copying and pasing to read the json, use pprint
from pprint import pprint

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
pprint(json)

description = json.get("weather")[0].get("description")
print("Today's force is", description)

temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")

print("The minimum temperator is", temp_min)
print("The maximum temperator is", temp_max)
