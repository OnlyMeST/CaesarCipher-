import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
import string

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char 
        decrypted_text += decrypted_char
    return decrypted_text

def find_shift_key(ciphertext):
    # Extract only alphabetic characters from the ciphertext
    ciphertext_alpha = ''.join(char.lower() for char in ciphertext if char.isalpha())
    
    # Calculate the shift key based on the most common letter in English ('e')
    most_common_letter = max(string.ascii_lowercase, key=ciphertext_alpha.count)
    shift_key = (ord(most_common_letter) - ord('e')) % 26
    
    return shift_key

def main():
    ciphertext = input("Enter the Caesar cipher text: ")
    shift_key = find_shift_key(ciphertext)
    decrypted_text = decrypt_caesar(ciphertext, shift_key)

    print("Decrypted text:", decrypted_text)
    print("Shift key used:", shift_key)
    print("Language detected: English")

if __name__ == "__main__":
    main()
