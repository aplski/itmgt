'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''
#SHIFT LETTER
def shift_letter(letter, shift):
    'if letter == ' ':
        return ' '
    
    if not letter.isalpha() or len(letter) != 1:
        raise ValueError("Input must be a single alphabetic character.")
    
    start = ord('a') if letter.islower() else ord('A')

    new_position = (ord(letter) - start + shift) % 26 + start

    return chr(new_position)
    
#CAESAR CIPHER
def caesar_cipher(message, shift):
     for char in message:
        if char == ' ':
            result.append(' ')
        elif 'A' <= char <= 'Z':
            new_position = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_position))
        else:
            raise ValueError("Input must be a string of uppercase alphabetic characters and spaces only.")
    
    return ''.join(result)

#SHIFT BY LETTER
def shift_by_letter(letter, letter_shift):
    if letter == ' ':
        return ' '
    
    if not letter.isalpha() or not letter_shift.isalpha() or len(letter) != 1 or len(letter_shift) != 1:
        raise ValueError("Inputs must be single alphabetic characters.")
    
    shift_amount = ord(letter_shift.upper()) - ord('A')
    
    start = ord('A')
    new_position = (ord(letter) - start + shift_amount) % 26 + start

    return chr(new_position)

def shift_string_by_letter(s, letter_shift):
    result = []
    for char in s:
        shifted_char = shift_by_letter(char, letter_shift)
        result.append(shifted_char)
    return ''.join(result)

#VIGENERE CIPHER
def vigenere_cipher(message, key):
    def shift_by_letter(letter, letter_shift):
        if letter == " ":
            return " "
        orig_position = ord(letter) - ord('A')
        shift = ord(letter_shift) - ord('A')
        new_position = (orig_position + shift) % 26
        new_letter = chr(new_position + ord('A'))
        return new_letter

    extended_key = (key * ((len(message)//len(key))+1))[:len(message)]
    
    encrypted_message = []

    key_index = 0
    for letter in message:
        if letter == " ":
            encrypted_message.append(letter)
            key_index += 1
        else:
            encrypted_message.append(shift_by_letter(letter, extended_key[key_index]))
            key_index += 1

    return "".join(encrypted_message)

#SCYTALE CIPHER
def scytale_cipher(message, shift):
    orig_length = len(message)
    if orig_length % shift != 0:
        phrase_length = shift - (orig_length % shift)
        message += "_" * phrase_length
    phrase_length = len(message)
    encoded_message = [""] * phrase_length
    for i in range(phrase_length):
        encoded_index = (i // shift) + (phrase_length // shift) * (i % shift)
        encoded_message[i] = message[encoded_index]
    return "".join(encoded_message)

#SCYTALE DECIPHER    
def scytale_decipher(message, shift):
    length = len(message)
    decoded_message = [""] * length
    for i in range(length):
        original_index = (i % shift) * (length // shift) + (i // shift)
        decoded_message[original_index] = message[i]
    return "".join(decoded_message)