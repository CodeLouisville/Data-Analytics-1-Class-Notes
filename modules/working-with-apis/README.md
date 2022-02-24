# Working With APIs

## Contents
1. [Demo Overview](#demo-overview)
1. [Prerequisites](#prerequisites)
1. [Topic Overview](#topic-overview)
1. [References](#references)
1. [Demo](#demo)
1. [Mentor Demo](#mentor-demo-1)
1. [Homework](#optional-homework)

## Demo Overview
This is a demo of an open weather api. The purpose of this demo is to dicuss interacting with and retrieving data from APIs. It will also touch on how to use the response from the API within your python program.

## Prerequisites
- python 3+
- a free rapidapi.com account
- the requests library `pip install requests

## Topic Overview
API stands for Application Programming Interface and broadly speaking is a middle layer that allows two pieces of software to interface with eachother. Within the context of the web the term API commonly refers to an interface at a specific url that allows for interacting with a certain application or database. A common introduction into APIs is the case of fetching data from a service for use within your own application. For instance, if you wanted to make an app about film and television then something like [The Open Movie Database](https://www.omdbapi.com/) might be of interest. By making HTTP requests to a specific url(endpoint) with certain parameters the API can return data back to you based on the specifics of your request. This sort of interaction is what we will focus on as it is the most common and useful case in the context of data analysis.

## References
1. https://rapidapi.com/
2. https://www.omdbapi.com/
3. https://www.redhat.com/en/topics/api/what-is-a-rest-api
4. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
5. https://www.postman.com/

## Demo

### Mentor Demo
1. show rapidapi and how to discover an api
2. demonstrate using the rapid api documentation to transfer the request into a python script
3. talk about keeping your API key a secret (E.G. don't commit it to your public github repo)
4. show conversion of response from json to a python object
5. demonstrate Postman

### Optional Homework
1. Find an open API you are interested on rapidapi or elsewhere on the web and try to make some requests!
