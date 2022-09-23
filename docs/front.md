<!--
SPDX-FileCopyrightText: 2022 DaniElectra

SPDX-License-Identifier: Apache-2.0
-->

# Front-end Documentation  
 
The **libcipher** library has the following functions:  

## libcipher.list_types()  
This function returns a `set` with all the available encodings for use with the library.  

## libcipher.encrypt()  
This function encrypts a given string with the selected encoding. It has the following parameters:  
- `string`: The string to encode.  
- `type`: The encryption to use for encoding the string.  
- `offset` *(Optional)*: The letter shift to apply (positive numbers move the shift right).

## libcipher.decrypt()  
This function encrypts a given string with the selected encoding. It has the following parameters:  
- `string`: The encrypted string.  
- `type`: The encryption to use for decoding the string.  
- `offset` *(Optional)*: The letter shift to apply (positive numbers move the shift left).

## libcipher.recrypt()  
This function decrypts a given string to recrypt it again with another encoding. It has the following parameters:  
- `string`: The string to recode in a different encoding.  
- `input_type`: The encryption to use for decoding the encrypted string.  
- `output_type`: The encryption to use for encoding the string.  
- `input_offset` *(Optional)*: The letter shift to apply when decrypting (positive numbers move the shift left).  
- `output_offset` *(Optional)*: The letter shift to apply when encrypting to a new encoding (positive numbers move the shift right).
