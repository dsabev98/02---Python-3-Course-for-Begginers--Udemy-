available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold == "quit":
        print("Game Over")
        break

print("Are you sure you want to go {}?".format(chosen_exit))
