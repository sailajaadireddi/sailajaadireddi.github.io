---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-06-19
categories: ["cryptography"]
tags: ["medium","key",basic mod1","basic mod2"]

---
# PicoGym cryptography |Basic mod |Medium |PicoCTF2022|

# Basic mod1

## Description:
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Hints:
Do you know what mod 37 means?
mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Solution:
Encrypted message is: 
```
128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140 
```
Lets write a simple python program which reads the message into a string first.

Then I will read each number into an array and take each number in the array mod 37

After that I will try to map each array field to the following scheme:

0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
 
 [script.py](/assets/files/script.py?raw=true)
# Flag:
```
picoCTF{R0UND_N_R0UND_B0D5F596}
```

# basic-mod2

## Description:
A new modular challenge!
Download the message here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Hints:
Do you know what the modular inverse is?
The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
It's recommended to use a tool to find the modular inverses


This challenge is similar to the previous challenge, basic-mod1,
but instead of calculating the modulus of each number, we need to calculate the modular inverse. There is also a slight difference in the character set instructions that we need to consider.

## Solution:
downloaded file displays a string of numbers:
```
 268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131
```
We need to calculate the modular inverse of each number and  map it to a character in the predefined character set in the description. I used a python script to do this.

```
chrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
enc_message = "268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131"
flag = ""
 
def modular_inverse(x: int, m: int) -> int:
   return pow(x, -1, m)
 
for i in enc_message.split():
   mod_inverse = modular_inverse(int(i),41)
 
   # -1 since the character set for this challenge starts from 1, unlike the previous challenge
   flag += chrs[mod_inverse-1]
 
print(flag)
```
## Flag:
```
picoCTF{1NV3R53LY_H4RD_8A05D939}

