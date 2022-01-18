"""
The names will be different depending on when you execute this, but the final result should print the json and a list of names like so:

{'people': [{'craft': 'ISS', 'name': 'Mark Vande Hei'}, {'craft': 'ISS', 'name': 'Pyotr Dubrov'}, {'craft': 'ISS', 'name': 'Anton Shkaplerov'}, {'craft': 'Shenzhou 13', 'name': 'Zhai Zhigang'}, {'craft': 'Shenzhou 13', 'name': 'Wang Yaping'}, {'craft': 'Shenzhou 13', 'name': 'Ye Guangfu'}, {'craft': 'ISS', 'name': 'Raja Chari'}, {'craft': 'ISS', 'name': 'Tom Marshburn'}, {'craft': 'ISS', 'name': 'Kayla Barron'}, {'craft': 'ISS', 'name': 'Matthias Maurer'}], 'message': 'success', 'number': 10}
The people currently in space are:
Mark Vande Hei
Pyotr Dubrov
Anton Shkaplerov
Zhai Zhigang
Wang Yaping
Ye Guangfu
Raja Chari
Tom Marshburn
Kayla Barron
Matthias Maurer
"""
import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print(json)

print("The people currently in space are:")
for p in json["people"]:
    print(p["name"])
