# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

def encrypt_binary(string: str) -> str:
    '''Encrypt a given string of text to binary'''
    cipher = ''
    for letter in string:
        # For easier manage of bytes, apply the ISO-8859-1 encoding
        character_bytes = bytearray(letter, 'latin1')
        binary = bin(character_bytes[0])

        # Remove characters that don't belong in binary
        binary = binary[2:]

        # If character is ASCII, add extra zeroes
        while len(binary) < 8:
            binary = '0' + binary

        cipher += binary + ' '

    return cipher

def decrypt_binary(string: str) -> str:
    '''Decrypt a given binary text to a string'''
    # Add an ending space to detect the last character
    string += ' '

    decipher = ''
    ciphered_text = ''
    for letter in string:
        # Check if character is a space
        if letter == ' ':
            # Ignore if there is an extra space
            if ciphered_text == '':
                continue

            # Reconvert to Python binary
            while ciphered_text[0] == '0':
                ciphered_text = ciphered_text[1:]

            # Decode binary character
            character_int = int(ciphered_text, 2)
            character = chr(character_int)

            decipher += character
            ciphered_text = ''
        else:
            # Store binary string of single character
            ciphered_text += letter

    return decipher
