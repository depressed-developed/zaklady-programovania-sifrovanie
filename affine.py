from math import gcd

def mod_inverse(a, m):
    """Finds the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No modular inverse if gcd(a, m) != 1

def affine_encode(plaintext, a, b):
    """Encodes plaintext using the Affine cipher with keys a and b."""
    m = 26  # Size of the alphabet
    encoded_text = []
    
    for char in plaintext.upper():
        if char.isalpha():  # Encode only alphabet characters
            x = ord(char) - ord('A') #value in the alphabet
            encoded_char = (a * x + b) % m
            encoded_text.append(chr(encoded_char + ord('A')))
        else:
            encoded_text.append(char)  # Keep non-alphabet characters as is

    return "".join(encoded_text)

def affine_decode(ciphertext, a, b):
    """Decodes ciphertext encoded with the Affine cipher using keys a and b."""
    m = 26  # Size of the alphabet
    decoded_text = []
    a_inv = mod_inverse(a, m)
    
    if a_inv is None:
        raise ValueError(f"No modular inverse for a={a} under modulo {m}")

    for char in ciphertext.upper():
        if char.isalpha():  # Decode only alphabet characters
            y = ord(char) - ord('A')
            decoded_char = (a_inv * (y - b)) % m
            decoded_text.append(chr(decoded_char + ord('A')))
        else:
            decoded_text.append(char)  # Keep non-alphabet characters as is

    return "".join(decoded_text)

def affine_bruteforce_decode(ciphertext):
    """Brute-force decodes an Affine cipher by trying all possible a and b values."""
    m = 26  # Size of the alphabet
    possible_decodings = []

    for a in range(1, m):
        if gcd(a, m) == 1:  # Only consider values of a that are coprime with m
            for b in range(m):
                try:
                    decoded_text = affine_decode(ciphertext, a, b)
                    possible_decodings.append((a, b, decoded_text))
                except ValueError:
                    continue  # Skip if there's no modular inverse for this a

    return possible_decodings


while True:
    try:
        user_input = str(input("Do you wish do encode or decode a message? e/d "))
        if (user_input == "e"):
            try:
                message_to_encode = str(input("Please enter a message to encode: "))
                first_key = int(input("Please enter the first key to encode with: "))
                second_key =  int(input("Please enter the second key to encode with: "))
                encoded_message = affine_encode(message_to_encode, first_key, second_key)
                print(f"Encoded Message: {encoded_message}")
            except ValueError:
                print("Input must be a whole number")
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
        elif (user_input == "d"):
            try:
                message_to_decode = str(input("Please enter a message to decode: "))
                print("Brute-force decoding results:")
                possible_decodings = affine_bruteforce_decode(encoded_message)
                for a, b, decoded_text in possible_decodings:
                    print(f"a={a}, b={b}: {decoded_text}")
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
        else:
            print("Enter 'e' to encode or 'd' to decode")
    except ValueError:
        print(f'Message must be of type string')
    except Exception as e:
        print(f'An unexpected error has occured: {e}')

