# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

MorseDictionary = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '0':'-----', '1':'.----', '2':'..---',
                    '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..',
                    '9':'----.', '.':'.-.-.-', ',':'--..--',
                    '?':'..--..', '\'':'.----.', '!':'-.-.--',
                    '/':'-..-.', '(':'-.--.', ')':'-.--.-',
                    '&':'.-...', ':':'---...', ';':'-.-.-.',
                    '=':'-...-', '+':'.-.-.', '-':'-....-',
                    '_':'..--.-', '"':'.-..-.', '$':'...-..-',
                    '@':'.--.-.' }

def encrypt_morse(string: str) -> str:
    '''Encrypt a string using Morse code, and return the encoded string'''
    cipher = ''
    for letter in string:
        if letter != ' ':
            # Check the letter at the dictionary and add the correct sequence to the cipher
            cipher += MorseDictionary[letter.upper()] + ' '
        else:
            # A space means a different character
            # A slash indicates a different word
            cipher += '/ '
    return cipher

def decrypt_morse(string: str) -> str:
    '''Decrypt a string using Morse code, and return the decoded string'''
    # Add an ending space to detect the last character
    string += ' '

    # Create inverse dictionary for easier lookup
    InverseMorseDictionary = {value: key for key, value in MorseDictionary.items()}

    decipher = ''
    ciphered_text = ''
    for letter in string:
        # Check if character is a space
        if letter == ' ':
            # Ignore if there is a slash or an extra space
            if ciphered_text == '/':
                decipher += ' '
                ciphered_text = ''
                continue

            if ciphered_text == '':
                continue

            # Decode character using inverse dictionary
            decipher += InverseMorseDictionary[ciphered_text]
            ciphered_text = ''
        else:
            # Store Morse code of single character
            ciphered_text += letter

    return decipher
