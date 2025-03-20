def simple_encrypt(text, key):
    # The number of columns is the length of the key.
    num_cols = len(key)

    # If the text doesn't fill all rows completely, add 'X' until it does.
    while len(text) % num_cols != 0:
        text += 'X'

    # Split the text into rows, each having num_cols characters.
    rows = [text[i:i + num_cols] for i in range(0, len(text), num_cols)]

    # Build the encrypted text by reading characters column-by-column.
    # The order of columns is defined by the key.
    cipher = ""
    for col in key:
        for row in rows:
            cipher += row[col]
    return cipher


def simple_decrypt(cipher, key):
    num_cols = len(key)
    # Determine the number of rows from the length of the cipher text.
    num_rows = len(cipher) // num_cols

    # Create an empty grid (list of lists) for the characters.
    grid = [[''] * num_cols for _ in range(num_rows)]
    index = 0

    # Fill the grid by columns.
    # The columns are filled in the order defined by the key.
    for col in key:
        for row in range(num_rows):
            grid[row][col] = cipher[index]
            index += 1

    # Read the grid row by row to get the original text.
    text = ""
    for row in grid:
        text += "".join(row)
    return text


def main():
    # Example usage:
    # Ask the user for the key in the form of numbers separated by spaces.
    # For instance: "2 0 1" means that the first column to read is index 2, then index 0, then index 1.
    key_str = input("Enter key as column order (e.g., '2 0 1'): ")
    key = [int(x) for x in key_str.split()]

    text = input("Enter text to encrypt: ")

    encrypted = simple_encrypt(text, key)
    print("Encrypted text:", encrypted)

    decrypted = simple_decrypt(encrypted, key)
    print("Decrypted text:", decrypted)


if __name__ == '__main__':
    main()
