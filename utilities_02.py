def main_menu(prompt):
    """Display the menu and returns a valid choice"""
    print("CAESAR CIPHER MESSAGING")
    print("-----------------------")
    choices = ["Start a message", "Read and reply to a message", "Quit"]
    for x, choice in enumerate(choices, start=1):
        print(f"{x}. {choice}")
    while True:
        try:
            user_choice = int(input(prompt))
            if 1 <= user_choice <= 3:
                return user_choice
            print("Enter a number 1-3 from above!")
        except ValueError:
            print("Enter a number 1-3 from above!")

def getAlphabet(prompt):
    """Get a nonempty set of characters to use as an alphabet without any duplicate characters"""
    while True:
        user_input = input(prompt)
        if user_input and len(user_input) == len(set(user_input)): # Checks for all of the characters to be unique
            return user_input
        print("Alphabet cannot be empty or contain duplicate characters!")

def getShift(prompt):
    """Gets the shift from the user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid shift!")

def encrypt(message, alphabet, shift):
    """Encrypt or decrypt the message"""
    shift = shift % len(alphabet) # lets the shift be longer than the alphabet
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift] # grabs the last letters of the alphabet and moves it towards the front
    translation = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(translation)

def getMessage(prompt):
    """Get a message that is nonempty"""
    while True:
        message = input(prompt)
        if message:
            return message
        print("Message cannot be empty!")

def createMessage():
    """Creates the text file"""
    alphabet = getAlphabet("Enter supported characters: "); shift = getShift("Enter shift: "); message = getMessage("Enter your message: "); encrypted = encrypt(message, alphabet, shift)
    while True:
        filename = input("Enter filename: ")
        if not filename.endswith(".txt"): #checks if it ends with .txt
            print("Filename must end in .txt!")
            continue
        try:
            with open(filename, "x") as file: # writes the message in the txt file and makes sure said file doesnt exist
                file.write(f"{alphabet}\n{shift}\n{encrypted}\n")
            print(f"Encrypted message: {encrypted}")
            break
        except FileExistsError:
            confirm = input("File exists. Overwrite? (Y/N): ")
            if confirm.lower() == "y":
                with open(filename, "w") as file:
                    file.write(f"{alphabet}\n{shift}\n{encrypted}\n")
                break
            elif confirm.lower() != "n":
                print("Enter Y or N!")
    print(f"Encrypted message: {encrypted}\n Message saved to {filename}!")

def replyToMessage(filename, alphabet, shift):
    """Encrypt a reply and append it to the file"""
    reply = getMessage("Enter your reply: ")
    encrypted = encrypt(reply, alphabet, shift) # encrypts the reply and gives it a variable name
    print(f"Encrypted message: {encrypted}")
    with open(filename, "a") as file: #writes the reply to the message in the txt file
        file.write(f"{encrypted}\n")
    print(f"Message saved to {filename}!")

def displayMessages(lines, alphabet, shift):
    """Decrypt and display all messages"""
    print("\nMESSAGES\n--------")
    for number, message in enumerate(lines[2:], start=1): # is the 1. and 2. in displaying the txt file
        message = message.strip()
        decrypted = encrypt(message, alphabet, -shift)
        print(f"{number}. {decrypted}")
    print("\nSupported characters:")
    print(alphabet)
    print()

def getSettings(lines):
    """Gets and validates the alphabet and shift"""
    alphabet = lines[0].strip() # removes whitespace
    shift = int(lines[1].strip()) #also removes whitespace
    if not alphabet or len(alphabet) != len(set(alphabet)) or len(lines) < 3:
        raise ValueError
    return alphabet, shift # returns the alphabet and shift

def readMessages():
    """Read a conversation and allow the user to reply"""
    while True:
        filename = input("Enter filename (M for main menu): ")
        if filename.lower() == "m":
            return
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            alphabet, shift = getSettings(lines)
            break
        except FileNotFoundError:
            print(f"Error: File '{filename}' was not found.")
        except (ValueError, IndexError):
            print("Error: Invalid conversation file.")
            return
    displayMessages(lines, alphabet, shift) # decrypts and prints the test in the txt file on the screen
    replyToMessage(filename, alphabet, shift) # makes it so that the user can reply to the message

def main():
    createMessage()
    readMessages()
    main_menu()

if __name__ == "__main__":
    main()