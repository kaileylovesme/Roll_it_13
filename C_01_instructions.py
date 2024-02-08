print("✨Roll it 13✨")


while True:
    want_instructions = input("Do you want to read the instructions?\n").lower()

    if want_instructions == "yes" or "y":
        print("You chose yes")
    elif want_instructions == "no" or "n":
        print("You chose no")
    else:
        print("You did not choose a valid response")
