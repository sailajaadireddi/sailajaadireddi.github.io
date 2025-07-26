---
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-25
categories: ["cryptography"]
tags: ["medium","","visual_cryptography","RSA"]

---
# PicoGym cryptography |Transposition-trail |Medium |PicoCTF2022|


![HashCrack Screenshot](/assets/lib/pic3.png)

The file contains 
```
heTfl g asiicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
```
## Solution:

Now use hint 
Split the msg into blocks of 3 
By observing the scrambled message, we can infer that the first 2 words of the message should be  ``` “The flag” ```
Let’s zoom into the first 3 blocks (of 3), which will make up the first 2 words.
```
•	First block: heT
•	Second block: fl
•	Third block: g a
```
So From the above 3 blocks. 
we can conclude that the third character of each block should be the first. This will be followed by the first and second character of the block.

Here is the Decrypted message: 
## Flag:
```
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
```