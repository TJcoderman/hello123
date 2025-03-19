# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt text using the Affine Cipher
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isupper():
            # Encrypt uppercase letters
            x = ord(char) - 65
            y = (a * x + b) % 26
            result += chr(y + 65)
        elif char.islower():
            # Encrypt lowercase letters
            x = ord(char) - 97
            y = (a * x + b) % 26
            result += chr(y + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

# Function to decrypt text using the Affine Cipher
def affine_decrypt(ciphertext, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: 'a' has no modular inverse. Choose a different key."
    for char in ciphertext:
        if char.isupper():
            # Decrypt uppercase letters
            y = ord(char) - 65
            x = (a_inv * (y - b)) % 26
            result += chr(x + 65)
        elif char.islower():
            # Decrypt lowercase letters
            y = ord(char) - 97
            x = (a_inv * (y - b)) % 26
            result += chr(x + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

# Main function
def main():
    text = input("Enter the text: ")
    a = int(input("Enter key 'a' (must be coprime with 26): "))
    b = int(input("Enter key 'b': "))

    # Check if 'a' is coprime with 26
    if gcd(a, 26) != 1:
        print("Error: 'a' must be coprime with 26.")
        return

    # Encrypt the text
    encrypted_text = affine_encrypt(text, a, b)
    print("\nEncrypted Text:", encrypted_text)

    # Decrypt the text
    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Decrypted Text:", decrypted_text)

# Run the program
if __name__ == "__main__":
    main()