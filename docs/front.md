<!--
SPDX-FileCopyrightText: 2022 DaniElectra

SPDX-License-Identifier: Apache-2.0
-->

# Front-end Documentation  
 
The **libcipher** library has basic and advanced functions:  

## Basic functions  
These functions are simple and easy to understand for common use of this library. It only has the essential functionality of encryption.  

### libcipher.list_types()  
This function returns a `set` with all the available encodings for use with the library.  

### libcipher.encrypt()  
This function encrypts a given string with the selected encoding. It has the following parameters:  
- `string`: The string to encode.  
- `type`: The encryption to use for encoding the string.  

### libcipher.decrypt()  
This function encrypts a given string with the selected encoding. It has the following parameters:  
- `string`: The encrypted string.  
- `type`: The encryption to use for decoding the string.  

### libcipher.recrypt()  
This function decrypts a given string to recrypt it again with another encoding. It has the following parameters:  
- `string`: The string to recode in a different encoding.  
- `input_type`: The encryption to use for decoding the encrypted string.  
- `output_type`: The encryption to use for encoding the string.  

## Advanced functions  
These functions have extra functionality that are not present in normal common-use functions, like letter shifting combined with encryption.  
This functionality is available under the `Advanced` class.  

### libcipher.Advanced.encrypt()  
This function encrypts a given string with the selected and offset. It has the following parameters:  
- `string`: The string to encode.  
- `type`: The encryption to use for encoding the string.  
- `offset` *(Optional)*: The letter shift to apply (positive numbers move the shift right). Default: `0`  
- `numbers` *(Optional)*: A boolean to check whether to apply letter shift to numbers. Default: `False`  
- `key` *(Optional)*: Encrypt the text using a key (Vigenère cipher). It is combined with the given offset. Default: `""`  

### libcipher.Advanced.decrypt()  
This function encrypts a given string with the selected encoding and offset. It has the following parameters:  
- `string`: The encrypted string.  
- `type`: The encryption to use for decoding the string.  
- `offset` *(Optional)*: The letter shift to apply (positive numbers move the shift left). Default: `0`  
- `numbers` *(Optional)*: A boolean to check whether to apply letter shift to numbers. Default: `False`  
- `key` *(Optional)*: Decrypt the text using a key (Vigenère cipher). It is combined with the given offset. Default: `""`  

### libcipher.Advanced.recrypt()  
This function decrypts a given string to recrypt it again with another encoding. It has the following parameters:  
- `string`: The string to recode in a different encoding.  
- `input_type`: The encryption to use for decoding the encrypted string.  
- `output_type`: The encryption to use for encoding the string.  
- `input_offset` *(Optional)*: The letter shift to apply when decrypting (positive numbers move the shift left). Default: `0`  
- `output_offset` *(Optional)*: The letter shift to apply when encrypting to a new encoding (positive numbers move the shift right). Default: `0`  
- `input_numbers` *(Optional)*: A boolean to check whether to apply letter shift to numbers when decrypting. Default: `False`  
- `output_numbers` *(Optional)*: A boolean to check whether to apply letter shift to numbers when encrypting. Default: `False`  
- `input_key` *(Optional)*: Decrypt the input using a key (Vigenère cipher). It is combined with the given offset. Default: `""`  
- `output_key` *(Optional)*: Encrypt the output using a key (Vigenère cipher). It is combined with the given offset. Default: `""`  
