import string

def decrypt_monoalphabetic(ciphertext, mapping):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = mapping.get(char, char)
            decrypted_text += decrypted_char.upper() if is_upper else decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_decrypt(ciphertext):
    decrypted_text = ""
    german_frequencies = 'etaoinsrhldcugmfwbyvkpjxzq'

    for permutation in string.ascii_lowercase:
        mapping = {}
        for encrypted_char, decrypted_char in zip(permutation, german_frequencies):
            mapping[encrypted_char] = decrypted_char

        decrypted_text = decrypt_monoalphabetic(ciphertext, mapping)
        print(f"Permutation: {permutation}, Decrypted text: {decrypted_text}")

def main():
    ciphertext = input("Enter the monoalphabetic cipher text (German): ")

    brute_force_decrypt(ciphertext)

if __name__ == "__main__":
    main()
