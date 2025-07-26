---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-27
categories: ["cryptography"]
tags: ["medium","RSA"]

---
# PicoGym cryptography |john_pollard  |Medium |PicoCTF2022|

## Description
Sometimes RSA certificates are breakable

## Hints:
The flag is in the format picoCTF{p,q}
Try swapping p and q if it does not work

## Solution

they had given a cetificate 
we need to find p and q from the certificate
so i decoded it using https://8gwifi.org/PemParserFunctions.jsp

Find the modulus value in the decoded certificate.
```
Modulus:966306421059967 
```
To solve this challenge, we need to find the prime factors of the RSA modulus `n`. 
We can use [Alpertron](https://www.alpertron.com.ar/ECM.HTM) to find the prime factors of `n`.

![HashCrack Screenshot](/assets/lib/cert.png)

## Flag:
```
picoCTF{73176001,67867967}
```