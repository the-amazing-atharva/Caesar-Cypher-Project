FIRST_CHAR_CODE = ord("A")  # 65
LAST_CHAR_CODE = ord("Z")  # 90
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1  # 26 letters
L_CHAR_CODE = ord("a")  # 97


def caesar_shift(message, shift):
    result = ""

    # Traversing through string
    for i in range(len(message)):
        ch = message[i]

        # checking for space
        if ch == " ":
            result += " "
        # checking for uppercase
        elif (ch.isupper()):
            result += chr((ord(ch) + shift - FIRST_CHAR_CODE) %
                          CHAR_RANGE + FIRST_CHAR_CODE)
        # checking for lowercase
        elif (ch.islower()):
            result += chr((ord(ch) + shift - L_CHAR_CODE) %
                          CHAR_RANGE + L_CHAR_CODE)
    return result


user_message = input("Message to Encrypt: ")
user_shift_key = int(input("Shift Key (integer): "))
cipher_text = caesar_shift(user_message, user_shift_key)
print(f"Cipher Text: {cipher_text}")
