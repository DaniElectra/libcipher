# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

import sys
from .base64 import *
from .binary import *
from .hexadecimal import *
from .morse import *
from .normal import *

modules_list = {'base64', 'binary', 'hexadecimal', 'morse', 'normal'}

def letter_arrangement(string: str, offset: int, undo: bool, numbers: bool, key: str) -> str:
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
    key_letter_count = 0
    key_offset = 0
    
    for letter in string:
        # If there's a key assigned, extract it's offset value
        if key != "":
            # Keep a count for extracting the key letters,
            # and reset it when we reach the end of the key
            if key_letter_count >= len(key):
                key_letter_count = 0
        
            # Extract the key letter
            letter_key = key[key_letter_count]
            
            # Check the letter offset in lists
            if letter_key in UppercaseList:
                key_offset = UppercaseList.index(letter_key)

            if letter_key in LowercaseList:
                key_offset = LowercaseList.index(letter_key)
            
            key_letter_count += 1

        # Search if letter exists in lists
        if letter in UppercaseList:
            if undo:
                letter_number = UppercaseList.index(letter) - offset - key_offset
            else:
                letter_number = UppercaseList.index(letter) + offset + key_offset
            
            # Check if letter offset bypasses list limits
            while letter_number >= len(UppercaseList):
                letter_number -= len(UppercaseList)
            
            while letter_number < 0:
                letter_number += len(UppercaseList)

            new_string += UppercaseList[letter_number]
            continue

        if letter in LowercaseList:
            if undo:
                letter_number = LowercaseList.index(letter) - offset - key_offset
            else:
                letter_number = LowercaseList.index(letter) + offset + key_offset
            
            # Check if letter offset bypasses list limits
            while letter_number >= len(LowercaseList):
                letter_number -= len(LowercaseList)
            
            while letter_number < 0:
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
            while new_number >= 10:
                new_number -= 10

            while new_number < 0:
                new_number += 10
            
            new_string += str(new_number)
            continue
        
        # If it's a non-listed character, pass it directly
        new_string += letter
    return new_string

class Advanced:
    '''Advanced functions for the library, like letter shift and keys'''
    def encrypt(string: str, type: str, offset = 0, numbers = False, key = "") -> str:
        '''Encrypt a given string using the specified type, offset and key'''
        # Check if module exists in modules list
        if type in modules_list:
            encrypt_dynamic = getattr(sys.modules[__name__], 'encrypt_' + type)
        else:
            raise NotImplemented
        
        # Check if offset or key given. In that case, do letter arrangement
        if offset != 0 or key != "":
            string = letter_arrangement(string, offset, False, numbers, key)    

        cipher = encrypt_dynamic(string)
        return cipher

    def decrypt(string: str, type: str, offset = 0, numbers = False, key = "") -> str:
        '''Decrypt a given string using the specified type, offset and key'''
        # Check if module exists in modules list
        if type in modules_list:
            decrypt_dynamic = getattr(sys.modules[__name__], 'decrypt_' + type)
        else:
            raise NotImplemented
        
        decipher = decrypt_dynamic(string)

        # Check if offset or key given. In that case, do letter arrangement
        if offset != 0 or key != "":
            decipher = letter_arrangement(decipher, offset, True, numbers, key)

        return decipher

    def recrypt(input: str,
                input_type: str,
                output_type: str,
                input_offset = 0,
                output_offset = 0,
                input_numbers = False,
                output_numbers = False,
                input_key = "",
                output_key = "") -> str:
        '''Recrypt a given encoded string into other encoding, using given offsets and keys'''
        decrypted = Advanced.decrypt(input, input_type, input_offset, input_numbers, input_key)
        recrypted = Advanced.encrypt(decrypted, output_type, output_offset, output_numbers, output_key)
        return recrypted

def encrypt(string: str, type: str) -> str:
    '''Encrypt a given string using the specified type'''
    # Check if module exists in modules list
    if type in modules_list:
        encrypt_dynamic = getattr(sys.modules[__name__], 'encrypt_' + type)
    else:
        raise NotImplemented   

    cipher = encrypt_dynamic(string)
    return cipher

def decrypt(string: str, type: str) -> str:
    '''Decrypt a given string using the specified type'''
    # Check if module exists in modules list
    if type in modules_list:
        decrypt_dynamic = getattr(sys.modules[__name__], 'decrypt_' + type)
    else:
        raise NotImplemented
    
    decipher = decrypt_dynamic(string)

    return decipher

def recrypt(input: str, input_type: str, output_type: str) -> str:
    '''Recrypt a given encoded string into other encoding'''
    decrypted = decrypt(input, input_type)
    recrypted = encrypt(decrypted, output_type)
    return recrypted

def list_types() -> set:
    '''List all available encryption types for use with this library'''
    return modules_list
