def encryption(message, shift_key):
    encrypted_message = ''
    for letter in message:
        new_letter = chr(ord(letter) + shift_key)
        encrypted_message += new_letter
    return encrypted_message


def decryption(message, shift_key):
    decrypted_message = ''
    for letter in message:
        new_letter = chr(ord(letter) - shift_key)
        decrypted_message += new_letter
    return decrypted_message


def main():
    shift_key = int(input("Pick a # between 1-9 "))
    message = input("What is your secret message? ")
    encrypted_message = encryption(message, shift_key)
    decrypted_message = decryption(encrypted_message, shift_key)
    print(f"{encrypted_message}, {decrypted_message}")


if __name__ == "__main__":
    main()



