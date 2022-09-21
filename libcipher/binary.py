# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

UppercaseList = [ 'A', 'B', 'C',
                  'D', 'E', 'F',
                  'G', 'H', 'I',
                  'J', 'K', 'L',
                  'M', 'N', 'O',
                  'P', 'Q', 'R',
                  'S', 'T', 'U',
                  'V', 'W', 'X',
                  'Y', 'Z' ]

LowercaseList = [ 'a', 'b', 'c',
                  'd', 'e', 'f',
                  'g', 'h', 'i',
                  'j', 'k', 'l',
                  'm', 'n', 'o',
                  'p', 'q', 'r',
                  's', 't', 'u',
                  'v', 'w', 'x',
                  'y', 'z' ]

def convert_to_binary(character: str) -> str:
    '''Convert a given character to binary'''
    # For easier manage of bytes, apply the ISO-8859-1 encoding
    character_bytes = bytearray(character, 'latin1')
    binary = bin(character_bytes[0])

    # Remove characters that don't belong in binary
    binary = binary[2:]

    # If character is ASCII, add extra zeroes
    while len(binary) < 8:
        binary = '0' + binary
    
    return binary

def encrypt_binary(string: str, offset: int) -> str:
    '''Encrypt a given string of text to binary'''
    cipher = ''
    for letter in string:
        # Search if letter exists in lists
        if letter in UppercaseList:
            letter_number = UppercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limit
            if letter_number >= len(UppercaseList):
                letter_number -= len(UppercaseList)
            
            binary_character = convert_to_binary(UppercaseList[letter_number])
            cipher += binary_character + ' '
            continue
        
        if letter in LowercaseList:
            letter_number = LowercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limit
            if letter_number >= len(LowercaseList):
                letter_number -= len(LowercaseList)
            
            binary_character = convert_to_binary(LowercaseList[letter_number])
            cipher += binary_character + ' '
            continue

        # Apply shift to numbers (DISABLED BY DEFAULT)
        """ if letter.isnumeric():
            new_number = int(letter) + offset

            # Make number only one digit
            if new_number >= 10:
                new_number -= 10
            
            cipher += str(new_number)
            continue """

        # If it's a non-listed character, pass it directly
        binary_character = convert_to_binary(letter)
        cipher += binary_character + ' '

    return cipher

def decrypt_binary(string: str, offset: int) -> str:
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

            # Search if letter exists in lists
            if character in UppercaseList:
                letter_number = UppercaseList.index(character) - offset
            
                # Check if letter offset bypasses list limit
                if letter_number < 0:
                    letter_number += len(UppercaseList)

                decipher += UppercaseList[letter_number]
                ciphered_text = ''
                continue
            
            if character in LowercaseList:
                letter_number = LowercaseList.index(character) - offset
            
                # Check if letter offset bypasses list limit
                if letter_number < 0:
                    letter_number += len(LowercaseList)
            
                decipher += LowercaseList[letter_number]
                ciphered_text = ''
                continue

            # Apply shift to numbers (DISABLED BY DEFAULT)
            """ if character.isnumeric():
                new_number = int(character) - offset

                # Make number only one digit
                if new_number < 0:
                    new_number += 10
            
                decipher += str(new_number)
                ciphered_text = ''
                continue """
            decipher += character
            ciphered_text = ''
        else:
            # Store binary string of single character
            ciphered_text += letter

    return decipher
