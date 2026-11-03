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
                return f"You chose {choices[user_choice - 1]}"
            else:
                print("Enter a number 1-3 from above!")
        except ValueError:
            print("Enter a number 1-3 from above!")

def getAlphabet(prompt):
    while True:
        user_input = input(prompt)
        if (len(user_input) > 0
            and len(user_input) == len(set(user_input))):
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

def encrypt(message, alphabet, shift):
    shift = shift % len(alphabet)
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]
    translation = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(translation)

def start_a_message():
    alphabet = getAlphabet("Enter the supported characters to use (no duplicated characters or whitespace): ")
    shift = getShift("Enter the shift amount (positive or negative): ")
    while True:
        message = input("Enter your message: ")
        if message:
            encrypted_message = encrypt(message, alphabet, shift)
            file_name = input("Enter filename: ")
            with open({file_name}, "w") as file:
                file.write("MESSAGES\n--------\n")
            break
        else:
            print("Message cannot be empty!")
    print()
    print(alphabet); print(shift)
    print(f"Encrypter message: {encrypted_message}")
    print(f"Message saved to {file_name}")
    print()

def main():
    main_menu("Enter a number (1-3) from above: ")
    start_a_message()

if __name__ == "__main__":
    main()