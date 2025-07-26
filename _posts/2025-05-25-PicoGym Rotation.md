---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-25
categories: ["cryptography"]
tags: ["medium"]

---
# PicoGym cryptography |Rotation |Medium |PicoCTF2022|

# Rotation
## Description:
You will find the flag after decrypting this file
Download the encrypted flag here.
https://artifacts.picoctf.net/c/386/encrypted.txt

## Hints:

Sometimes rotation is right

#### File contains:
```
xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}
```
## Solution:
We can use this tool [Caesar Cipher Decoder](https://www.dcode.fr/caesar-cipher) to decrypt the file: 

![HashCrack Screenshot](/assets/lib/pic10.png)

## Flag:
```
picoCTF{r0tat1on_d3crypt3d_4c71f5b0}
```