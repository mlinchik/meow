import random

def game(choice, result):
    computer_choice = random.choice("rps")
    if str.lower(choice) == computer_choice:
        print("Draw")
    elif str.lower(choice) == "r" and computer_choice == "p":
        result["computer"]+=1
    elif str.lower(choice) == "r" and computer_choice == "s":
        result["player"]+=1
    elif str.lower(choice) == "p" and computer_choice == "s":
        result["computer"] += 1
    elif str.lower(choice) == "p" and computer_choice == "r":
        result["player"] += 1
    elif str.lower(choice) == "s" and computer_choice == "r":
        result["computer"] += 1
    elif str.lower(choice) == "s" and computer_choice == "p":
        result["player"] += 1