# Data Cleaning

## Contents
1. [Demo Overview](#demo-overview)
1. [Prerequisites](#prerequisites)
1. [Topic Overview](#topic-overview)
1. [Demo](#demo)

## Demo Overview

This demo covers basic data discovery and cleaning for a sample analytics project.

## Prerequisites

- a GitHub.com account
- git, python installed on your computer


## Topic Overview

This demo covers the full data analysis process with a particular focus on the data cleaninig.

1. Define the question
1. Find the data
1. Clean the data
1. Analyze the data

### The Question

How often are fire trucks called out for fires compared to other reasons?

### The Data Source

Louisville publishes data on Fire Department emergency calls.

[Louisville/Jefferson County Fire Districts calls for service](https://data.louisvilleky.gov/dataset/louisvillejefferson-county-fire-districts-calls-service)

This file includes calls for service over a rollling 24 month period broken down by Fire Districts which includes but not limited to Fire and Medical Emergencies.


### File Details

|Dimension | Description |
| ------ | --------|
| Columns | AGENCY NAME – Name of the fire protection agency that has jurisdiction for the event.|
| |DATE – Date the event occurred.|
| |CREATE – Time the event was entered into the 911 CAD system. |
| |DISPATCH – Time dispatchers notified responders of event. |
| |ENROUTE - Time the first unit went responding to event. |
| |ARRIVE - Time the first unit called on scene to an event.|
| |CLEAR - Time last unit left scene and the event was closed.|
| |HOUR OF – Hour of the day the event occurred (24hr clock)|
| |LOCATION – Hundred block that event took place.|
| |EVENT TYPE – Type of event that took place.|
| |PRIORITY - Numeric value for the severity of incident. The lower the number the greater the severity.|
| |FD EVENT NUMBER – Unique number for event assigned to the agency that has jurisdiction.|
| |ZIP CODE – The zip code in which the event occurred. |
| Records | 158898 items |


### Sample Data

|AGENCY_NAME|DATE|CREATE|DISPATCH|ENROUTE|ARRIVE|CLEAR|HOUR OF|LOCATION|EVENT TYPE|PRIORITY|FD EVENT NUMBER|ZIP_CODE|
|-----------|----|------|--------|-------|------|-----|-------|--------|----------|--------|---------------|---------|
|Louisville Fire Department|01/01/2020|00:07:44||||00:08:00|0000|400 BLOCK OF S 5TH ST|ALARM--Fire Alarm Sounding-Commercial|2|LF190042159|40202|
|Louisville Fire Department|01/01/2020|00:10:18|00:10:48|00:11:48|00:15:41|00:21:13|0000|1200 BLOCK OF LARCHMONT AVE|FIRE--Fire-Type Unknown|2|LF200000001|40215|
|Louisville Fire Department|01/01/2020|00:20:24|00:20:44|00:21:56|00:25:18|00:51:35|0000|1800 BLOCK OF MCCLOSKEY AVE|FIRE--Fire/Close to Structure|2|LF200000002|40210|
|Louisville Fire Department|01/01/2020|00:26:23|00:26:43|00:27:53|00:34:15|00:52:36|0000|100 BLOCK OF COLONIAL OAKS CT|MEDICAL--MEDICAL - MED_CALL|7|LF200000003|40214|
|Louisville Fire Department|01/01/2020|00:30:03|00:30:28|00:32:15|00:37:06|00:56:50|0000|3500 BLOCK OF WHEELER AVE|MEDICAL--MEDICAL - MED_CALL|7|LF200000004|40215|
|Pleasure Ridge Park FD|01/01/2020|00:33:57|00:34:11|00:36:01|00:40:22|01:08:20|0000|8200 BLOCK OF DIXIE HWY|MEDICAL--MEDICAL - MED_CALL|7|F2219007864|40258|
|St Matthews FD|01/01/2020|00:41:46|00:42:01|00:44:45|00:48:58|01:09:06|0000|800 BLOCK OF WASHBURN AVE|FIRE--Dumpster Fire|3|F2619004232|40222|
|Middletown FD|01/01/2020|00:55:51|00:56:02|00:58:47|01:02:47|02:29:05|0000|2500 BLOCK OF EVERGREEN RD|ACCIDENT--Injury Accident|2|F9919005687|40223|
|Pleasure Ridge Park FD|01/01/2020|01:11:05|01:11:26|01:13:10|01:19:38|01:35:31|0100|7800 BLOCK OF BRAMBLE LN|MEDICAL--MEDICAL - MED_CALL|7|F2220000001| |



## Demo

### Mentor Demo: Identifying Data Issues
There are several issues with the sample data that could make the analysis of the data more difficult.

1. The event type column contains multiple pieces of information. It contains a category and a sub-category separated by "--".
1. Minor issue - the column titles use different formats - snake case and words with spaces. It would be ideal to have the clean data use consistent formats.


### Student Execrise: Identifying Data Issues
Review the sample data (viewing the table on Github is the easiest way) and identify at least 1 more issue with the sample data.

### Mentor Demo: Cleaning and summarizing data
The `clean_calls.py` script cleans the data and save a summary data file that could be used for visualization or analysis.

The data is summarized by Event Category and saved as a json file with the following format:

Call Data by Event Category
`
    {
        'FIRE' : 1234,
        'MEDICAL': 234
    }
`

### Student Exercise: Cleaning and summarizing data
Modify the `clean_calls.py` script to summarize the data by call Priority and save the summary data as a json file.

Call Data by Priority
`
    {
        '1' : 1234,
        '2' : 234
    }
`

### Mentor Demo: Analyze data

The `analyze_calls.py` script allows a user to interact with the clean data. The user can choose from a list of categories and see the total number of calls for the selected categoy.

`There were 15005 calls in the FIRE category`


### Student Task: Analyze data

Modify the `analyze_calls.py` script to prompt the user for a priority between 0 and 9 and display the number of calls for the selected priority.

`There were 9058 calls with priority 1.`


### Student Task: Clean and summarize data

Modify the `clean_calls.py` script again to summarize the data by Zip Code with totals for all calls, fire calls, and other calls. 

Remember that the Zip Code data needs some cleaning to deal with empty values. In this case, let's replace the empty Zip Code values with the string "Unknown".

Call Data by Zip
` 
    {
        '40203' = {
            'CALL_TOTAL' : 20,
            'FIRE_TOTAL' : 5,
            'OTHER_TOTAL' : 15
        },
        '40204' = {
            'CALL_TOTAL' : 21,
            'FIRE_TOTAL' : 7,
            'OTHER_TOTAL' : 14
        },
        'Unknown' = {
            'CALL_TOTAL' : 28,
            'FIRE_TOTAL' : 14,
            'OTHER_TOTAL' : 14
        }
    }
`

### Student Task: Analyze the zip code data
Modify the `analyze_calls.py` script to prompt the user for a zip code and then display the % of calls in the "FIRE" category.

`8.0% of fire department calls in zip code 40203 are for fires.`