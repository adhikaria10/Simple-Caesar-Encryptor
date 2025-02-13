import string


def menu():
    print("\nSelect any option from the menu")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Press 'Q' to exit")


def caesarEncrypt(plainText, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encryptedText = plainText.lower().translate(cipher)

    return encryptedText


def caesarDecrypt(encryptedText, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    decryptedText = encryptedText.translate(cipher)

    return decryptedText


while True:
    menu()
    print()
    option = input("Select an option: ")
    if option == '1':
        plainText = input("Enter the plain text that you want to get encrypted: \n")
        encryptedText = caesarEncrypt(plainText, 3)
        print(f'Encrypted message: {encryptedText}')

    elif option == '2':
        encryptedText = input("Enter the encrypted text that you want to get decrypted: \n")
        decryptedText = caesarDecrypt(encryptedText, 3)
        print(f'Decrypted message: {decryptedText}')

    elif option == 'Q' or option == 'q':
        print("Quitting!!!")
        print("You have a wonderful day. See you again!")
        break

    else:
        print("No such option. Please select the correct option.")
