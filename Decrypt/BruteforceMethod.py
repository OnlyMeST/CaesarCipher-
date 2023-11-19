def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_decrypt(ciphertext):
    decrypted_texts = []
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def main():
    ciphertext = ""
    decrypted_texts = brute_force_decrypt(ciphertext)
    print("Possible Decrypted Texts:")
    for idx, text in enumerate(decrypted_texts):
        print(f"Shift {idx}: {text}")

if __name__ == "__main__":
    main()




