def rot13_encode_decode(message):
    result = []

    for char in message:
        # Check if it's an uppercase letter
        if 'A' <= char <= 'Z':
            # Rotate within uppercase letters
            rotated_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(rotated_char)
        # Check if it's a lowercase letter
        elif 'a' <= char <= 'z':
            # Rotate within lowercase letters
            rotated_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(rotated_char)
        else:
            # Leave non-alphabet characters as they are
            result.append(char)
    
    # Join list into final string
    return ''.join(result)


while True:
    try:
        user_input = str(input("Do you wish do encode or decode a message? e/d "))
        if (user_input == "e"):
            try:
                message_to_encode = str(input("Please enter a message to encode: "))
                encoded_message = rot13_encode_decode(message_to_encode)
                print(f"Encoded Message: {encoded_message}")
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
        elif (user_input == "d"):
            try:
                message_to_decode = str(input("Please enter a message to decode: "))
                decoded_message = rot13_encode_decode(message_to_decode)
                print(f'Decoded message: {decoded_message}')
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
        else:
            print("Enter 'e' to encode or 'd' to decode")
    except ValueError:
        print(f'Message must be of type string')
    except Exception as e:
        print(f'An unexpected error has occured: {e}')