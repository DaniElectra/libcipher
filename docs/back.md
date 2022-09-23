<!--
SPDX-FileCopyrightText: 2022 DaniElectra

SPDX-License-Identifier: Apache-2.0
-->

# Back-end Documentation  

The functions of an encoding for the **libcipher** library must have the same name as the Python file itself (for example: the `example.py` functions must be called `encrypt_example()` and `decrypt_example()`).  

## The functions  
The functions (currently) only contain one single input: the string to convert. The string is usually converted letter by letter, but it isn't mandatory.  
After converting the string, it also has to be returned as a string.  

```python
def encrypt_example(string: str) -> str:
    '''Encrypt a given string using the "example" encoding'''
    cipher = ''
    for letter in string:
        '''Insert code to encode each character and add it to "cipher"'''
    return cipher
```  

Before the encoding can work with the library, it has to be imported in `core.py` and added to the `modules_list` set.
