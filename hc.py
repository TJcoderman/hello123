import numpy as np
import math

def letter_to_number(letter):
    return ord(letter) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))

def hill_cipher_encrypt(plaintext, key):
    # Convert to uppercase and remove spaces
    plaintext = plaintext.upper().replace(" ", "")
    
    # Pad with 'X' if needed to make length even
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    # Convert plaintext letters to numbers (A=0, B=1, ..., Z=25)
    text_numbers = [letter_to_number(ch) for ch in plaintext]
    
    # Convert key to NumPy array
    key_matrix = np.array(key)
    
    ciphertext = ""
    # Process the text two numbers (one pair) at a time
    for i in range(0, len(text_numbers), 2):
        pair = np.array([[text_numbers[i]], [text_numbers[i+1]]])  # 2x1 column vector
        # Multiply key with the pair and take mod 26
        encrypted_pair = np.dot(key_matrix, pair) % 26
        # Convert numbers back to letters and append to ciphertext
        ciphertext += number_to_letter(encrypted_pair[0, 0])
        ciphertext += number_to_letter(encrypted_pair[1, 0])
    
    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    text_numbers = [letter_to_number(ch) for ch in ciphertext]
    
    key_matrix = np.array(key)
    # Calculate determinant and take it modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26

    # Check if key is invertible: det must be non-zero and coprime with 26
    if det == 0 or math.gcd(det, 26) != 1:
        raise ValueError("Key matrix is not invertible modulo 26.")
    
    # Compute modular inverse of the determinant
    det_inv = pow(det, -1, 26)
    
    # Compute adjugate matrix for 2x2 matrix
    adjugate = np.array([[key_matrix[1, 1], -key_matrix[0, 1]],
                         [-key_matrix[1, 0], key_matrix[0, 0]]]) % 26
    
    # Compute the inverse key matrix modulo 26
    key_inverse = (det_inv * adjugate) % 26
    
    plaintext = ""
    for i in range(0, len(text_numbers), 2):
        pair = np.array([[text_numbers[i]], [text_numbers[i+1]]])
        decrypted_pair = np.dot(key_inverse, pair) % 26
        plaintext += number_to_letter(decrypted_pair[0, 0])
        plaintext += number_to_letter(decrypted_pair[1, 0])
    
    return plaintext

def main():
    # Take the key dynamically from the user.
    key_input = input("Enter 4 key numbers for the 2x2 matrix (space-separated): ")
    key_numbers = list(map(int, key_input.split()))
    
    if len(key_numbers) != 4:
        print("Error: You must enter exactly 4 numbers for a 2x2 key matrix.")
        return
    
    key = [[key_numbers[0], key_numbers[1]],
           [key_numbers[2], key_numbers[3]]]
    
    # Check if the key matrix is invertible modulo 26.
    key_matrix = np.array(key)
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    if det == 0 or math.gcd(det, 26) != 1:
        print("The key matrix is not invertible modulo 26. Please try another key.")
        return
    
    plaintext = input("Enter the plaintext (only letters): ")
    
    encrypted_text = hill_cipher_encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = hill_cipher_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
