# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0

import base64

def encrypt_base64(string: str) -> str:
    '''Encrypt a given string using base64 encoding'''
    # Make a bytearray for use with Python's base64 tool
    bytes_array = bytearray(string, 'utf-8')

    # Encode the array and convert it to string
    new_array = base64.b64encode(bytes_array)
    new_string = new_array.decode('utf-8')

    return new_string

def decrypt_base64(string: str) -> str:
    '''Decrypt a given string using base64 encoding'''
    # Make a bytearray for use with Python's base64 tool
    bytes_array = bytearray(string, 'utf-8')

    # Decode the array and convert it to string
    new_array = base64.b64decode(bytes_array)
    new_string = new_array.decode('utf-8')

    return new_string
