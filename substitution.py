import string
import random

def generate_substitution_alphabet():
    """
    Generates a random substitution alphabet.
    """
    alphabet = list(string.ascii_uppercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return "".join(shuffled_alphabet)

def create_cipher_dict(alphabet):
    """
    Creates encoding and decoding dictionaries based on a substitution alphabet.
    """
    original_alphabet = string.ascii_uppercase
    encode_dict = {original_alphabet[i]: alphabet[i] for i in range(26)}
    decode_dict = {alphabet[i]: original_alphabet[i] for i in range(26)}
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
substitution_alphabet = generate_substitution_alphabet()
print(f"Substitution Alphabet: {substitution_alphabet}")

# Create encoding and decoding dictionaries
encode_dict, decode_dict = create_cipher_dict(substitution_alphabet)

# Encode a message
plaintext = "HELLO SUBSTITUTION CIPHER"
encoded_message = substitution_encode(plaintext, encode_dict)
print(f"Encoded Message: {encoded_message}")

# Decode the message
decoded_message = substitution_decode(encoded_message, decode_dict)
print(f"Decoded Message: {decoded_message}")
