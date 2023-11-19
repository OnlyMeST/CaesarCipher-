import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
import string

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Download necessary resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def chi_squared(observed, expected):
    return sum((obs - exp) ** 2 / exp for obs, exp in zip(observed, expected))

def frequency_analysis(ciphertext):
    # Extract only alphabetic characters from the ciphertext
    ciphertext_alpha = ''.join(char.lower() for char in ciphertext if char.isalpha())

    # Calculate the frequency distribution of letters in the ciphertext
    freq_dist = FreqDist(ciphertext_alpha)

    # Get observed frequencies of letters in the ciphertext
    observed_freqs = [freq_dist.freq(letter) for letter in string.ascii_lowercase]

    # Expected frequencies for English and German
    english_expected_freqs = [0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241,
                              0.0675, 0.0751, 0.0193, 0.0010, 0.0596, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
    german_expected_freqs = [0.0652, 0.0189, 0.0306, 0.0508, 0.1740, 0.0166, 0.0301, 0.0458, 0.0650, 0.0027, 0.0142, 0.0344, 0.0253,
                             0.0978, 0.0251, 0.0079, 0.0002, 0.0700, 0.0727, 0.0615, 0.0435, 0.0067, 0.0077, 0.0002, 0.0320, 0.0001]

    # Calculate chi-squared statistic for English and German
    chi_squared_english = chi_squared(observed_freqs, english_expected_freqs)
    chi_squared_german = chi_squared(observed_freqs, german_expected_freqs)

    # Determine the language based on chi-squared statistic
    if chi_squared_english < chi_squared_german:
        language = 'english'
    else:
        language = 'german'

    # Calculate the shift key based on the most common letter ('e' for English, 'e' or 'n' for German)
    shift_key = (ord(freq_dist.max()) - ord('e')) % 26

    # Decrypt the ciphertext using the calculated shift
    decrypted_text = decrypt_caesar(ciphertext, shift_key)

    return decrypted_text, shift_key, language

def main():
    # Input ciphertext from the user
    ciphertext = input("Enter the Caesar cipher text: ")

    # Perform frequency analysis decryption
    decrypted_text, shift_key, language = frequency_analysis(ciphertext)
    
    print("Decrypted text:", decrypted_text)
    print("Shift key used:", shift_key)
    print("Language detected:", language)

if __name__ == "__main__":
    main()
