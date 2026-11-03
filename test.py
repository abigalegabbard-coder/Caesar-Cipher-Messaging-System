import os

def main_menu(prompt):
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
            else:
                print("Enter a number 1-3 from above!")
        except ValueError:
            print("Enter a number 1-3 from above!")

def getAlphabet(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0 and len(user_input) == len(set(user_input)):
            print("Valid input!")
            return user_input
        else:
            print("Alphabet cannot be empty or contain duplicate characters!")

def getShift(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid shift!")

def getMessage(prompt):
    while True:
        message = input(prompt)
        if message:
            return message
        else:
            print("Message cannot be empty!")

def encrypt(message, alphabet, shift):
    shift = shift % len(alphabet)
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]
    translation = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(translation)

def createMessage(alphabet, shift, encrypted_message):
    file_name = input("Enter a filename: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    if os.path.exists(file_name):
        confirmation = input("File already exists. Overwrite? (yes/no): ")
        if confirmation.lower() != "yes":
            print("File not saved.")
            return
    with open(file_name, "w") as file:
        file.write(alphabet + "\n"); file.write(str(shift) + "\n"); file.write(encrypted_message + "\n")
    print("Encrypted message:", encrypted_message)
    print("Message saved to:", file_name)

def start_a_message():
    alphabet = getAlphabet("Enter the supported characters: ")
    shift = getShift("Enter the shift amount: ")
    message = getMessage("Enter your message: ")
    encrypted_message = encrypt(message, alphabet, shift)
    createMessage(alphabet, shift, encrypted_message)

def main():
    while True:
        choice = main_menu("Enter a number (1-3) from above: ")
        if choice == 1:
            start_a_message()
        elif choice == 2:
            pass
        elif choice == 3:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()