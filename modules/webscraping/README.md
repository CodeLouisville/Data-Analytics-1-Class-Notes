# Webscraping 101
As a last resort to collecting data from unreliable sources like a website's html code, Python has a powerful library called Selenium that handles
a lot of the webscraping complexity for you.  This demo is a non-comprehensive example of how you might use Selenium to scrape data from a website.

Selenium Docs can be found [here](https://www.selenium.dev/documentation/webdriver/elements/finders/) for reference.

## Contents
1. [Demo Overview](#demo-overview)
1. [Prerequisites](#prerequisites)
1. [Instructions](#instructions)
1. [Topic Overview](#topic-overview)
1. [Demo](#demo)

## Demo Overview
Using Python's Selenium library this package is going to scan a specified website with NBA player salary information, and display it as a Pandas Dataframe.
Comments are used heavily in the module, be sure to take advantage of them.

## Prerequisites
- python and pip installed on your computer

## Topic Overview
I can't find a API for the data I need, but I was able to find it on a website.  This example will be grabbing some data from a website
using Python.  The data will be cleaned, and then displayed using Python's Pandas library.

We will be collecting NBA player names, and their salaries from https://hoopshype.com/salaries/players/.

## Demo
1. Setup the environment
  1. Pull the code down:  `git clone git@github.com:CodeLouisville/Data-Analytics-1-Class-Notes.git`
  1. Enter project folder:
    * mac/linux/gitbash: `cd Data-Analytics-1-Class-Notes/modules/webscraping`
    * windows: `cd Data-Analytics-1-Class-Notes\modules\webscraping`
  1. Install required Python packages:  `pip install -r requirements`
1. Execute the code to confirm things are working.
  * mac/linux/gitbash:  `python ./src/main.py`
  * windows:  `python .\src\main.py`
  * Example output is available at the bottom of `src/main.py`.

### Student Exercise: Other data structures
1. Change the URL and display different data