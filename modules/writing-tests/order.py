MENU = {
    1: "option 1",
    2: "option 2",
    3: "option 3",
    4: "option 4",
    5: "stock option",
    6: "exit",
}

def get_prompt(menu):
    prompt = "Select an option:\n"
    options = []
    for key, value in menu.items():
        options.append("{}: {}".format(key, value))

    print(options)
    prompt += ("\n".join(options))
    return prompt

def user_input(prompt):
    print(prompt)
    return input()

def main():
    run = True
    while run:
        prompt = get_prompt(menu=MENU)
        selection = user_input(prompt)
        if selection:
            print("You chose {}".format(MENU[selection]))
            run = False

if __name__ == "__main__":
    main()