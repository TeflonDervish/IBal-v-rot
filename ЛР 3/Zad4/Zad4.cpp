#include <iostream>
#include <fstream>
#include <bitset>

void encryptDecryptFile(const std::string& inputFile, const std::string& outputFile, const std::string& key) {
    std::ifstream input(inputFile, std::ios::binary);
    std::ofstream output(outputFile, std::ios::binary);

    if (!input.is_open() || !output.is_open()) {
        std::cerr << "Error opening files!" << std::endl;
        return;
    }

    // Convert key to binary representation
    std::bitset<8> binaryKey(key[0]);

    char ch;
    while (input.get(ch)) {
        // XOR each byte with the key
        ch ^= binaryKey.to_ulong();

        // Write the result to the output file
        output.put(ch);

        // Rotate key for the next byte
        binaryKey = (binaryKey << 1) | (binaryKey >> 7);
    }

    input.close();
    output.close();
}

int main() {
    // Пример использования
    std::string inputFile = "input.txt";
    std::string encryptedFile = "encrypted.txt";
    std::string decryptedFile = "decrypted.txt";
    std::string key = "K";  // Ключ для шифрования (может быть любым символом)

    // Зашифровать файл
    encryptDecryptFile(inputFile, encryptedFile, key);
    std::cout << "File encrypted successfully." << std::endl;

    // Расшифровать файл
    encryptDecryptFile(encryptedFile, decryptedFile, key);
    std::cout << "File decrypted successfully." << std::endl;

    return 0;
}
1   