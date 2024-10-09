#get all alphabetic values
#store in an array
#switch letters based on index

#edge cases:
#user doesnt enter a string
#need to store data in two arrays, one as a data storage and one as an index reference

def is_letter(letter):
    if letter != " ":
        return True
    else:
        return False

def encode(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    mirrored_alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA".lower()
    split_message = list(message)
    encoded_message = ""


    print(split_message)
    for i in range(len(split_message)):
        if split_message[i] == " ":
            encoded_message += " "
        else:
            encoded_message += mirrored_alphabet[alphabet.index(split_message[i])]
    return encoded_message

def decode(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    mirrored_alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA".lower()
    split_message = list(message)
    decoded_message = ""


    print(split_message)
    for i in range(len(split_message)):
        if split_message[i] == " ":
            decoded_message += " "
        else:
            decoded_message += alphabet[mirrored_alphabet.index(split_message[i])]
    return decoded_message

while True:
    try:
        user_input = str(input("Please enter a string to decode:"))
        print(encode(user_input))
        print(decode(encode(user_input)))
    except ValueError as e:
        print(f"Input must be of type string: {e}")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")