import numpy as np

def generate_playfair_key(key):
    key = key.replace("J", "I")  # Заменяем J на I
    key = key.upper()  # Приводим к верхнему регистру
    key = "".join(sorted(set(key), key=key.find))  # Удаляем повторяющиеся символы и сортируем по порядку ключа

    # Создаем матрицу 5x5 и заполняем ее символами из ключа, затем добавляем оставшиеся буквы алфавита
    matrix = [['' for _ in range(5)] for _ in range(5)]
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key_index = 0
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                while alphabet[0] in key:
                    alphabet = alphabet[1:]
                matrix[i][j] = alphabet[0]
                alphabet = alphabet[1:]

    return matrix

def find_position(matrix, letter):
    # Функция для нахождения позиции буквы в матрице
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)

def encrypt_playfair(plain_text, key):
    # Функция для шифрования текста шифром Плейфера
    playfair_matrix = generate_playfair_key(key)
    cipher_text = ""

    for i in range(0, len(plain_text), 2):
        pair = plain_text[i:i + 2]

        if len(pair) == 1:
            pair += 'X'

        row1, col1 = find_position(playfair_matrix, pair[0])
        row2, col2 = find_position(playfair_matrix, pair[1])

        if row1 == row2:
            cipher_text += playfair_matrix[row1][(col1 + 1) % 5] + playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += playfair_matrix[(row1 + 1) % 5][col1] + playfair_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

    return cipher_text

def decrypt_playfair(cipher_text, key):
    # Функция для дешифрования текста шифром Плейфера
    playfair_matrix = generate_playfair_key(key)
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        pair = cipher_text[i:i + 2]

        row1, col1 = find_position(playfair_matrix, pair[0])
        row2, col2 = find_position(playfair_matrix, pair[1])

        if row1 == row2:
            plain_text += playfair_matrix[row1][(col1 - 1) % 5] + playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += playfair_matrix[(row1 - 1) % 5][col1] + playfair_matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

    return plain_text

# Пример использовани
key = "NINE"
plain_text = "SAMIUPKAFE"
cipher_text = decrypt_playfair(plain_text, key)
decrypted_text = encrypt_playfair(cipher_text, key)

print(f"Original Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
