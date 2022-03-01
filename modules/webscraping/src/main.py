"""
This is a quick demo to show what a webscraping script could look like.  
"""
import pandas as pd
from pprint import pprint

# selenium is the goto library for webscraping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# select which browser driver you want to use
from webdriver_manager.chrome import ChromeDriverManager

# set the website we want to scrape
url = "https://hoopshype.com/salaries/players/"

# install selected browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

""" Attempt to make the call to the url, and if it fails for 'any' Exception
catch the failure, and raise a general Exception error.

NOTE:  catching a broad Exception like this is not good practice, instead
the more specific exception such as 'KeyError', or 'NotImplementedError'.
"""
try:
    driver.get(url)
except Exception:
    raise Exception("Your app is broken.")

def clean(data):
    """Redimentary data scrubber

    While working with the players, and salaries data I noticed a ton of empty strings
    that caused Dataframe misalignments.

    :return: Non-Empty items in data
    :rtype: list
    """
    scrubbed = []
    for item in data:
        # if an item exists aka True
        if item:
            scrubbed.append(item)
    return scrubbed

# make a scrubbed list of player names and salaries by CSS class ids found via the browser's inspect tool
players = clean([player.text for player in driver.find_elements(by=By.CLASS_NAME, value='name')])
salaries = clean([player.text for player in driver.find_elements(by=By.CLASS_NAME, value='hh-salaries-sorted')])

# strip headers and grab top 50
sport_data = {
    'Name': players[1:52],
    'Salaries': salaries[1:52]
}

# display the data
pprint(pd.DataFrame(sport_data))
# Example output:
#
#                      Name     Salaries
# 0           Stephen Curry  $45,780,966
# 1               John Wall  $44,310,840
# 2            James Harden  $44,310,840
# 3       Russell Westbrook  $44,211,146
# 4            Kevin Durant  $42,018,900
# 5            LeBron James  $41,180,544
# ...
# 45         Nikola Vucevic  $24,000,000
# 46            Buddy Hield  $23,073,234
# 47           John Collins  $23,000,000
# 48          Julius Randle  $21,780,000
# 49        Malcolm Brogdon  $21,700,000
# 50        Tim Hardaway Jr  $21,306,816
