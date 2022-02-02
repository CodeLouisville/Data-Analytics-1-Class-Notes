import random
import sys
from uuid import uuid4

ZIP_CODES = ("40214", "40203", "40118", "40205", "40204", "40206", "40177", "40025", "40023")
WIDGETS = [
    {
        "ITEM_ID": "T332",
        "PRICE": "19.99",
        "DESCRIPTION": "Cyan Widget",
    },
    {
        "ITEM_ID": "T823",
        "PRICE": "4.99",
        "DESCRIPTION": "Yellow Widget",
    },
    {
        "ITEM_ID": "T977",
        "PRICE": "8.49",
        "DESCRIPTION": "Green Widget",
    },
    {
        "ITEM_ID": "T022",
        "PRICE": "11.29",
        "DESCRIPTION": "Blue Widget",
    },
    {
        "ITEM_ID": "T249",
        "PRICE": "2.89",
        "DESCRIPTION": "Red Widget",
    },
    {
        "ITEM_ID": "T885",
        "PRICE": "82.32",
        "DESCRIPTION": "Maroon Widget",
    },
    {
        "ITEM_ID": "T491",
        "PRICE": "37.99",
        "DESCRIPTION": "Transparent Widget",
    },
]

def generate_order():
    order_id = uuid4()
    zip_code = random.choice(ZIP_CODES)
    rows = []

    for _ in range(0, random.randrange(1, 15)):
        item = random.choice(WIDGETS)
        print(f"{str(order_id)}, {item['ITEM_ID']}, {item['PRICE']}, {item['DESCRIPTION']}, {zip_code}")

    return rows

def generate_orders(num_orders):
    print("ORDER_ID, ITEM_ID, PRICE, DESCRIPTION, SHIPPING_ZIP")
    for _ in range(1, num_orders):
        generate_order()



if __name__ == "__main__":
    generate_orders(num_orders=int(sys.argv[1]))
