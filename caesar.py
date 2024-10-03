
def encode(message, step):
    letters = [x for x in message]
    encoded_message = ""
    for i in range(len(message)):
        if letters[i] != " ":
            if(ord(message[i]) + step) >= 97 and (ord(message[i]) + step) <= 122:
                shifted_letter = chr(ord(message[i]) + step)
                encoded_message += shifted_letter
            elif (ord(message[i]) + step) > 122:
                shifted_letter = chr(97 + (step - (122 - ord(message[i]))))
                encoded_message += shifted_letter
            else: 
                shifted_letter = chr(122 - (abs(step) - (ord(message[i]) - 97)))
                encoded_message += shifted_letter
        else:
            encoded_message += " "
    return encoded_message


def decode(message):
    possible_solutions = []
    letters = [x for x in message]
   
    for k in range(-25, 25):
        encoded_message = ""
        for i in range(len(message)):
            
            if letters[i] != " ":
                if(ord(message[i]) + k) >= 97 and (ord(message[i]) + k) <= 122:
                    shifted_letter = chr(ord(message[i]) + k)
                    encoded_message += shifted_letter
                elif (ord(message[i]) + k) > 122:
                    shifted_letter = chr(97 + (k - (122 - ord(message[i]))))
                    encoded_message += shifted_letter
                else: 
                    shifted_letter = chr(122 - (abs(k) - (ord(message[i]) - 97)))
                    encoded_message += shifted_letter
            else:
                encoded_message += " "
        possible_solutions.append(encoded_message)
    return possible_solutions

def print_list(messages):
    for message in messages:
        print(message)

while True:
    try: 
        operation_type = str(input("Encode or decode (e/d):"))
        if(operation_type == "e"):
            user_message = str(input("Enter a sentence to encode:"))
            user_step = int(input("Enter an encoding step between -25 and 25: ")) 
            encoded_message = encode(user_message, user_step)
            print(f"Encoded value of {user_message} is: {encoded_message}")
        elif(operation_type == "d"):
            user_message = str(input("Enter a sentence to decode:"))
            decoded_solutions = decode(user_message)
            print_list(decoded_solutions)
    except ValueError:
        print("Message must be of type string.")
        print("step must be of type int.")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")