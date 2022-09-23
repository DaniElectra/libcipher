# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

import importlib

def letter_arrangement(string: str, offset: int, undo: bool, numbers = False) -> str:
    '''Apply letter arrangement to string based on offset'''
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
    
    new_string = ''
    for letter in string:
        # Search if letter exists in lists
        if letter in UppercaseList:
            if undo:
                letter_number = UppercaseList.index(letter) - offset
            else:
                letter_number = UppercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limits
            if letter_number >= len(UppercaseList):
                letter_number -= len(UppercaseList)
            
            if letter_number < 0:
                letter_number += len(UppercaseList)

            new_string += UppercaseList[letter_number]
            continue

        if letter in LowercaseList:
            if undo:
                letter_number = LowercaseList.index(letter) - offset
            else:
                letter_number = LowercaseList.index(letter) + offset
            
            # Check if letter offset bypasses list limits
            if letter_number >= len(LowercaseList):
                letter_number -= len(LowercaseList)
            
            if letter_number < 0:
                letter_number += len(LowercaseList)

            new_string += LowercaseList[letter_number]
            continue

        # Check if applying number arrangement
        if letter.isnumeric() and numbers == True:
            if undo:
                new_number = int(letter) + offset
            else:
                new_number = int(letter) - offset

            # Make number only one digit
            if new_number >= 10:
                new_number -= 10

            if new_number < 0:
                new_number += 10
            
            new_string += str(new_number)
            continue
        
        # If it's a non-listed character, pass it directly
        new_string += letter
    return new_string

def encrypt(string: str, type: str, offset = 0) -> str:
    '''Encrypt a given string using the specified type and offset'''
    # Select module dynamically based on type
    module = importlib.import_module('libcipher.' + type)
    encrypt_dynamic = getattr(module, 'encrypt_' + type)
    
    # Check if offset isn't zero. In that case, do letter arrangement
    if offset != 0:
        string = letter_arrangement(string, offset, undo = False)    

    cipher = encrypt_dynamic(string)
    return cipher

def decrypt(string: str, type: str, offset = 0) -> str:
    '''Decrypt a given string using the specified type and offset'''
    # Select module dynamically based on type
    module = importlib.import_module('libcipher.' + type)
    decrypt_dynamic = getattr(module, 'decrypt_' + type)
    
    decipher = decrypt_dynamic(string)

    # Check if offset isn't zero. In that case, do letter arrangement
    if offset != 0:
        decipher = letter_arrangement(decipher, offset, undo = True)

    return decipher

def recrypt(input: str, input_type: str, output_type: str, input_offset = 0, output_offset = 0) -> str:
    '''Recrypt a given encoded string into other encoding, using given offsets'''
    decrypted = decrypt(input, input_type, input_offset)
    recrypted = encrypt(decrypted, output_type, output_offset)
    return recrypted
