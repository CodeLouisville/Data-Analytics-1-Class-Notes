import csv
import json

# constants for the raw and clean data file paths
INPUT_FILE_PATH = 'data/raw/Fire_Open_Data.csv'
CATEGORY_OUTPUT_FILE_PATH = 'data/clean/call_data_by_category.json'

# open the input file in a context manager
with open(INPUT_FILE_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip the header
    next(csv_reader)

    # dictionary to store the category summary data
    category_data = {}

    # loop through the CSV reader
    for agency_name, call_date, create_time, dispatch_time, enroute_time, \
        arrive_time, clear_time, hour_of, location, event_type, priority, \
        fd_event_number, zip_code in csv_reader:
        
        # parse the event category
        event_category = event_type.split('--')[0]

        # keep track of the number of occurances of each category
        if event_category in category_data:
            category_data[event_category] += 1
        else:
            category_data[event_category] = 1
    
    # print out the event categories
    for key, value in category_data.items():
        print(f'{key} = {value}')

    # write the clean category data
    with open(CATEGORY_OUTPUT_FILE_PATH, 'w') as output_file:
        json.dump(category_data, output_file, indent=4)
