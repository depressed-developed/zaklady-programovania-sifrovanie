import string
import random

def generate_substitution_alphabet():
    """
    Generates a random substitution alphabet.
    """
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet[:] #creates a shallow copy of alphabet
    random.shuffle(shuffled_alphabet)
    return "".join(shuffled_alphabet)

def create_cipher_dict(shuffled_alphabet):
    """
    Creates encoding and decoding dictionaries based on a substitution alphabet.
    """
    original_alphabet = string.ascii_uppercase
    encode_dict = {original_alphabet[i]: shuffled_alphabet[i] for i in range(26)}
    decode_dict = {shuffled_alphabet[i]: original_alphabet[i] for i in range(26)}
    return encode_dict, decode_dict

def substitution_encode(plaintext, encode_dict):
    """
    Encodes the plaintext using the substitution cipher with the provided encoding dictionary.
    """
    plaintext = plaintext.upper()
    encoded_message = []
    
    for char in plaintext:
        if char.isalpha():
            encoded_message.append(encode_dict[char])
        else:
            encoded_message.append(char)  # Keep non-alphabet characters as is

    return "".join(encoded_message)

def substitution_decode(ciphertext, decode_dict):
    """
    Decodes the ciphertext using the substitution cipher with the provided decoding dictionary.
    """
    ciphertext = ciphertext.upper()
    decoded_message = []
    
    for char in ciphertext:
        if char.isalpha():
            decoded_message.append(decode_dict[char])
        else:
            decoded_message.append(char)  # Keep non-alphabet characters as is

    return "".join(decoded_message)

# Example usage
# Generate a random substitution alphabet


# Create encoding and decoding dictionaries


# Encode a message


# Decode the message

while True:
    try: 
        substitution_alphabet = generate_substitution_alphabet()
        encode_dict, decode_dict = create_cipher_dict(substitution_alphabet)
        print(f"Substitution Alphabet: {substitution_alphabet}")
        plaintext = str(input("Please enter a string to encode: "))
        encoded_message = substitution_encode(plaintext, encode_dict)
        print(f"Encoded Message: {encoded_message}")
        decoded_message = substitution_decode(encoded_message, decode_dict)
        print(f"Decoded Message: {decoded_message}")
    except ValueError:
        print("Message must be of type string.")
    except Exception as e:
        print(f"Unexpected error has occured: {e}")