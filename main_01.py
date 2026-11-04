import utilities_02 as ut

def main():
    """Control the main menu and program execution."""
    while True:
        userChoice = ut.main_menu("Enter a number (1-3) from above: ")
        if userChoice == 1:
            ut.createMessage()
        elif userChoice == 2:
            ut.readMessages()
        elif userChoice == 3:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()