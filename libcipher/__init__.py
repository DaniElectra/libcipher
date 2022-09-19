# SPDX-FileCopyrightText: 2022 DaniElectra
#
# SPDX-License-Identifier: Apache-2.0
import importlib

def encrypt(string: str, type: str, offset = 0):
    '''Encrypt a given string using the specified type and offset'''
    module = importlib.import_module('libcipher.' + type)
    encrypt_dynamic = getattr(module, 'encrypt_' + type)
    cipher = encrypt_dynamic(string, offset)
    return cipher

def decrypt(string: str, type: str, offset = 0):
    '''Decrypt a given string using the specified type and offset'''
    module = importlib.import_module('libcipher.' + type)
    decrypt_dynamic = getattr(module, 'decrypt_' + type)
    decipher = decrypt_dynamic(string, offset)
    return decipher
    