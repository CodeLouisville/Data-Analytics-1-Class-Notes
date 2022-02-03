import json

CATEGORY_FILE_PATH = 'data/clean/call_data_by_category.json'

print('Categories:')
with open(CATEGORY_FILE_PATH) as file:
    category_data = json.load(file)
    print(*category_data.keys(), sep='\n')
    category = input("Enter a category:")
    if category in category_data:
        print(f'There were {category_data[category]} calls in the {category} category')
    else:
        print('Category not found.')

