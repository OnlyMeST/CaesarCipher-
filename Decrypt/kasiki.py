import collections
import re

def calculate_ioc(text):
    #Calculate index of coincidence
    total_chars = len(text)
    char_freq = collections.Counter(text)
    ioc = sum(freq * (freq - 1) for freq in char_freq.values()) / (total_chars * (total_chars - 1))
    return ioc

def find_key_length(ciphertext, max_length=20):
    #Find potential key length by trial
    repeated_sequences = {}
    
    # Find repeated sequences in the ciphertext
    for length in range(3, max_length + 1):
        regex_pattern = re.compile(r'(?=([A-Za-z]{' + str(length) + '}))')
        matches = re.findall(regex_pattern, ciphertext)
        
        if matches:
            repeated_sequences[length] = [match[0] for match in matches]

    # Calculate the GCD of distances between repeated sequences
    potential_lengths = []
    for length, sequences in repeated_sequences.items():
        distances = [sequences[i + 1] - sequences[i] for i in range(len(sequences) - 1)]
        gcd = distances[0]
        for d in distances[1:]:
            gcd = _calculate_gcd(gcd, d)
        potential_lengths.append((length, gcd))
    potential_lengths.sort(key=lambda x: x[1], reverse=True)

    return potential_lengths

def _calculate_gcd(a, b):
    #calculate remainder via modulus method
    while b:
        a, b = b, a % b
    return a

def decrypt_vigenere(ciphertext, key_length):
    #Decrypt
    key = ''
    for i in range(key_length):
        ith_column = ciphertext[i::key_length]
        most_common_letter = collections.Counter(ith_column).most_common(1)[0][0]
        key += chr((ord(most_common_letter) - ord('E')) % 26 + ord('A'))

    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        decrypted_char = chr((ord(char) - ord(key[i % key_length])) % 26 + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text, key

ciphertext = "POILIEIWSAGJEKIWOFPLGIYMKYIMHYKRFZRIPSYHRZWWWLBTKAKGOIJXHPRXAPAFTDGLBOGUBPGNRQBKWABAPPSMHUAHBWHMDAEQTAZQCBVGIBNLUDMEIBYKPBSLEQ"
potential_key_lengths = find_key_length(ciphertext)
most_probable_length = potential_key_lengths[0][0] 
decrypted_text, key = decrypt_vigenere(ciphertext, most_probable_length)

print("Potential key lengths:", [length[0] for length in potential_key_lengths])
print("Most probable key length:", most_probable_length)
print("Decrypted text:", decrypted_text)
print("Found key:", key)
