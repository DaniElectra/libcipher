# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

def reconvert_hexadecimal(character: str) -> str:
    '''Reconvert a hexadecimal string to a character'''
    # Reconvert to Python binary
    if character[:2] != '0x':
        character = '0x' + character

    # Decode hex character
    character_int = int(character.lower(), 16)
    new_character = chr(character_int)
    return new_character

def encrypt_hexadecimal(string: str) -> str:
    '''Encrypt a given string of text to hexadecimal'''
    cipher = ''
    for letter in string:
        # For easier manage of bytes, apply the ISO-8859-1 encoding
        character_bytes = bytearray(letter, 'latin1')
        hexadecimal = hex(character_bytes[0])

        # Remove initial hexadecimal address
        hexadecimal = hexadecimal[2:]

        # Make hex characters uppercase
        # hexadecimal = hexadecimal.upper()

        cipher += hexadecimal + ' '

    return cipher

def decrypt_hexadecimal(string: str) -> str:
    '''Decrypt a given hexadecimal text to a string'''
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

            # Decode hex character
            character = reconvert_hexadecimal(ciphered_text)

            decipher += character
            ciphered_text = ''
        else:
            # Check if reading more than one character
            if len(ciphered_text) == 2 and ciphered_text != '0x':
                # Decode hex character
                character = reconvert_hexadecimal(ciphered_text)

                decipher += character
                ciphered_text = ''
                continue

            if len(ciphered_text) == 4 and ciphered_text[:2] == '0x':
                # Decode hex character
                character = reconvert_hexadecimal(ciphered_text)

                decipher += character
                ciphered_text = ''
                continue

            # Store hex string of single character
            ciphered_text += letter

    return decipher
