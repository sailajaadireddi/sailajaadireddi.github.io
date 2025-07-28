---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-15
categories: ["cryptography"]
tags: ["medium","Caesar","key"]

---
# PicoGym cryptography |Caesar |Medium |PicoCTF

# Caesar
## Description:
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext)

## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

The given Encrypted message:
```
picoCTF{gvswwmrkxlivyfmgsrhnrisegl}
```
## Solution:
We need to do bruteforce . We can use a python script to do this:

To decrypt the message, I used help from chatgpt to write this Python script that systematically tried all 26 possible shifts, printing each result until the plaintext emerged.

```
def brute_force_caeser_cipher(encrypted_flag):
 alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet - in this case is the latin alphabet

 length_text = len(encrypted_flag)

 for shift in range(26):
     decrypted_message = ""
     for char in encrypted_flag:
      if char in alphabet:
       new_char = chr(((ord(char) - 97 - shift) % 26) + 97) # Decrypt the character using modular arithmetic
       decrypted_message += new_char
      else:
       decrypted_message += char  # Keep non-alphabet characters unchanged
     print(f"Shift {shift}: {decrypted_message}")  # Print the result for this shift

brute_force_caeser_cipher("gvswwmrkxlivyfmgsrhnrisegl")
```

After running the script,we finally get flag.

## Flag:
``` picoCTF{crossingtherubiconapisvsuj} ```

