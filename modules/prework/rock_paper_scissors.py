import random

""" Human input required wrapping as a string, so I added the vars that 
are accepted as well.  When inputting the data as a human, the human can
input rock, paper, scissors, or "rock", "paper", "scissors".  This is a
personal preference, and not required.
"""
rock = "rock"
paper = "paper"
scissors = "scissors"

""" In the random.choice function, I create the sequence inside of the call by passing a list in with the options.
"""
computer_choice = random.choice([rock, paper, scissors])
user_choice = input("Do you want - rock, paper, or scissors?\n")
print("Computer choice: " + computer_choice)

if computer_choice == user_choice:
    print("TIE")
elif user_choice == rock and computer_choice == scissors:
    print("WIN")
elif user_choice == paper and computer_choice == rock:
    print("WIN")
elif user_choice == scissors and computer_choice == paper:
    print("WIN")
else:
    print("You lose.  Computer wins.")
