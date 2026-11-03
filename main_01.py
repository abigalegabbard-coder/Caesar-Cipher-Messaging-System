import utilities_02 as ut

def main():
    while True:
        userChoice = ut.main_menu("Enter a number (1-3) from above: ")
        if userChoice == 1:
            ut.start_a_message()
        elif userChoice == 2:
            pass
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()