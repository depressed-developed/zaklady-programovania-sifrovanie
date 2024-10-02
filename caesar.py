
def encode(message, step):
    letters = [x for x in message]
    encoded_message = ""
    for i in range(len(message)):
        if letters[i] != " ":
            if (ord(message[i]) + step) > 122:
                shifted_letter = chr(step - (122 - ord(message[i])))
                encoded_message += shifted_letter
            elif (ord(message[i]) - abs(step)) < 97:
                shifted_letter = chr(122 - (abs(step) - (ord(message[i]) - 97)))
                encoded_message += shifted_letter
            else:
                shifted_letter = chr(ord(message[i]) + step)
                encoded_message += shifted_letter
        else:
            encoded_message += " "
    return encoded_message



while True:
    try: 
        user_message = str(input("Enter a sentence to encode:"))
        user_step = int(input("Enter an encoding step between -25 and 25: ")) 
        encoded_message = encode(user_message, user_step)
        print(f"Encoded value of {user_message} is: {encoded_message}")
    except ValueError:
        print("Message must be of type string.")
        print("step must be of type int.")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")