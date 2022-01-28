import csv
from json import load
import sys
from pprint import pprint


def load_file_to_dict(file_path):
    orders = {}
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip header with next
        next(csv_reader)

        for order_id, item_id, price, description, shipping_zip in csv_reader:
            if order_id in orders:
                # add the price of the current line to the total
                orders[order_id]["total"] += float(price)
                orders[order_id]["total"] = round(orders[order_id]["total"], 2)
            else:
                orders[order_id] = {
                    "total": round(float(price), 2),
                    "shipping_zip": shipping_zip
                }

    return orders

def print_largest_order(orders_dict):
    max_total = 0
    max_order_id = None
    for order_id, order_data in orders_dict.items():
        order_total = order_data["total"]
        # check if our current highest total is less than the current order we are on in our iteration
        if max_total < order_total:
            # if the current total is higher then make it our new highest order
            max_total = order_total
            max_order_id = order_id

    print(f"Order with id of {max_order_id} has the largest total: ${max_total}")

def main():
    # Accept file path argument when running the program from the command line
    # file_path = sys.argv[1]
    # as an alternative to the above
    # accepting user input to use during the program
    file_path = input("What file do you want to load?\n")
    orders_dict = load_file_to_dict(file_path)
    print_largest_order(orders_dict)


if __name__ == "__main__":
    main()