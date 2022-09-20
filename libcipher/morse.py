# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

import collections

MorseDictionaryLetters = collections.OrderedDict({ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..' })

MorseDictionary = { '0':'-----', '1':'.----', '2':'..---',
                    '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..',
                    '9':'----.', '.':'.-.-.-', ',':'--..--',
                    '?':'..--..', '\'':'.----.', '!':'-.-.--',
                    '/':'-..-.', '(':'-.--.', ')':'-.--.-',
                    '&':'.-...', ':':'---...', ';':'-.-.-.',
                    '=':'-...-', '+':'.-.-.', '-':'-....-',
                    '_':'..--.-', '"':'.-..-.', '$':'...-..-',
                    '@':'.--.-.' }

def encrypt_morse(string: str, offset: int):
    '''Encrypt a string using Morse code, and return the encoded string'''
    cipher = ''
    for letter in string:
        if letter != ' ':
            try:
                # Check the letter at the dictionary and add the correct sequence to the cipher
                letter_number = list(MorseDictionaryLetters.keys()).index(letter.upper()) + offset
                
                # If letter offset bypasses the dictionary length, count from the start
                if letter_number >= len(MorseDictionaryLetters):
                    letter_number -= len(MorseDictionaryLetters)

                new_letter = list(MorseDictionaryLetters)[letter_number]
                cipher += MorseDictionaryLetters[new_letter] + ' '
            except ValueError:
                # If the character isn't a letter, go to the normal dictionary
                cipher += MorseDictionary[letter] + ' '
        else:
            # A space means a different character
            # A slash indicates a different word
            cipher += '/ '
    return cipher

def decrypt_morse(string: str, offset: int):
    '''Decrypt a string using Morse code, and return the decoded string'''
    # Add an ending space to detect the last character
    string += ' '

    # Create inverse dictionaries for easier lookup
    InverseMorseDictionaryLetters = collections.OrderedDict({value: key for key, value in MorseDictionaryLetters.items()})
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
            try:
                letter_number = list(InverseMorseDictionaryLetters.keys()).index(ciphered_text) - offset
                if letter_number < 0:
                    letter_number += len(InverseMorseDictionaryLetters)
                new_letter = list(InverseMorseDictionaryLetters)[letter_number]
                decipher += InverseMorseDictionaryLetters[new_letter]
            except ValueError:
                decipher += InverseMorseDictionary[ciphered_text]
            ciphered_text = ''
        else:
            # Store Morse code of single character
            ciphered_text += letter

    return decipher
