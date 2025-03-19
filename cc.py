def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def key_check():
    while True:
        try:
            key = int(input("Enter the key (1-25): "))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be between 1 and 25. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def dec_encrp():
    while True:
        choice = input("Encrypt or Decrypt? (e/d): ").lower()
        if choice in ['e', 'd']:
            return choice
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

def main():
    text = input("Enter the text: ")
    mode = dec_encrp()
    key = key_check()
    
    # Convert key to shift value (negative for decryption)
    shift = key if mode == 'e' else -key
    
    result = caesar_cipher(text, shift)
    print("\nResult:", result)

if __name__ == "__main__":
    main()