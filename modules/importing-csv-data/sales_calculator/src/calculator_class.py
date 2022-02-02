
import csv
import sys
from collections import namedtuple

class OrderAnalyzer(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.orders = {}
        self.load_csv()

    # read csv and load it into a dictionary with the keys being order ids
    def load_csv(self):
        with open(self.file_path) as csv_file:
            reader = csv.reader(csv_file)
            # get rid of header
            next(reader)

            for row in reader:
                if row[0] not in self.orders:
                    self.orders[row[0]] = {
                        "line_items": [row[1:4]],
                        "shipping_zip": row[4],
                        "order_total": float(row[2].strip())
                    }
                else:
                    order = self.orders[row[0]]
                    order["order_total"] += float(row[2].strip())
                    order["line_items"].append(row[1:4])


    def get_highest_order_total(self):
        max_total = 0
        largest_order_id = None
        for order_id, order in self.orders.items():
            if order["order_total"] > max_total:
                largest_order_id = order_id
                max_total = order["order_total"]

        return f"Largest order is {largest_order_id} with a total of {max_total} to zip code {self.orders[largest_order_id]['shipping_zip']}"

    @staticmethod
    def quit():
        # standardlib sys. Stops the program execution cleanly.
        sys.exit()


if __name__ == "__main__":
    print("Input file path to the csv you want to load")
    file_path = input()
    try:
        order_analyzer = OrderAnalyzer(file_path=file_path)
    except FileNotFoundError: # display a meaninful error message if the file path is bad
        print("Oops, thats not a valid file path. Exiting.")
        sys.exit()

    # namedtuple provides a pretty way to store my users choices with their action methods
    Choice = namedtuple("Choice", ["input", "func_name"])
    # What I want the users input to be
    choice_inputs = ["max", "q"]
    # Choices above correspond in order one for one to the method names below on OrderAnalyzer
    choice_function_names = ["get_highest_order_total", "quit"]
    choices = [Choice(input_str, func_name) for input_str, func_name in zip(choice_inputs, choice_function_names)]

    # run the command loop until the use explicitly exits
    run = True
    while run:
        print("___________________________________________________________________________")
        print("Analyzer choices: 'max' will output the largest order. 'q' will stop program")
        print("input valid choice")
        print("___________________________________________________________________________\n\n")
        user_input = input()
        if user_input not in choice_inputs:
            print("Please select a valid choice")
        else:
            for input_str, func_name in choices:
                if user_input == input_str:
                    # get the method based on the choice and execute
                    output = getattr(order_analyzer, func_name)()
                    print("***************************************************")
                    print(output)
                    print("***************************************************\n\n")