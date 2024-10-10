
def encode(message):
    letters = [x for x in message]
    encoded_message = ""
    for i in range(len(message)):
        if letters[i] != " ":
            if(ord(message[i]) + 13) >= 97 and (ord(message[i]) + 13) <= 122:
                shifted_letter = chr(ord(message[i]) + 13)
                encoded_message += shifted_letter
            elif (ord(message[i]) + 13) > 122:
                shifted_letter = chr(96 + (13 - (122 - ord(message[i]))))
                encoded_message += shifted_letter
            else: 
                shifted_letter = chr(122 - (abs(13) - (ord(message[i]) - 97)))
                encoded_message += shifted_letter
        else:
            encoded_message += " "
    return encoded_message

while True:
    try:
        user_input = str(input("Please enter a string to decode:"))
        print(encode(user_input))
        #print(decode(encode(user_input)))
    except ValueError as e:
        print(f"Input must be of type string: {e}")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")