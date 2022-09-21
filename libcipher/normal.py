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

def encrypt_normal(string: str, offset: int) -> str:
    '''Encrypt a string of text using the shift method'''
    cipher = ''
    for letter in string:
        # Search if letter exists in lists
        if letter in UppercaseList:
            letter_number = UppercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limit
            if letter_number >= len(UppercaseList):
                letter_number -= len(UppercaseList)
            
            cipher += UppercaseList[letter_number]
            continue
        
        if letter in LowercaseList:
            letter_number = LowercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limit
            if letter_number >= len(LowercaseList):
                letter_number -= len(LowercaseList)
            
            cipher += LowercaseList[letter_number]
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
        cipher += letter

    return cipher

def decrypt_normal(string: str, offset: int) -> str:
    '''Decrypt a string of text using the shift method'''
    decipher = ''
    for letter in string:
        # Search if letter exists in lists
        if letter in UppercaseList:
            letter_number = UppercaseList.index(letter) - offset
            
            # Check if letter offset bypasses list limit
            if letter_number < 0:
                letter_number += len(UppercaseList)
            
            decipher += UppercaseList[letter_number]
            continue
        
        if letter in LowercaseList:
            letter_number = LowercaseList.index(letter) - offset
            
            # Check if letter offset bypasses list limit
            if letter_number < 0:
                letter_number += len(LowercaseList)
            
            decipher += LowercaseList[letter_number]
            continue

        # Apply shift to numbers (DISABLED BY DEFAULT)
        """ if letter.isnumeric():
            new_number = int(letter) - offset

            # Make number only one digit
            if new_number < 0:
                new_number += 10
            
            decipher += str(new_number)
            continue """

        # If it's a non-listed character, pass it directly
        decipher += letter
        
    return decipher
