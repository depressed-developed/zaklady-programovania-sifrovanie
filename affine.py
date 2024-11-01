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
            x = ord(char) - ord('A')
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

# Example usage
plaintext = "HELLOAFFINECIPHER"
a, b = 5, 8  # Sample keys
encoded_message = affine_encode(plaintext, a, b)
print(f"Encoded Message: {encoded_message}")

# Brute-force decode the encoded message
print("Brute-force decoding results:")
possible_decodings = affine_bruteforce_decode(encoded_message)
for a, b, decoded_text in possible_decodings:
    print(f"a={a}, b={b}: {decoded_text}")
