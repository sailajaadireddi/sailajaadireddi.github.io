---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-29
categories: ["cryptography"]
tags: ["medium","morsecode"]

---
# PicoGym cryptography |Tapping|Medium |PicoCTF
# Tapping

## Description:
Theres tapping coming in from the wires. What's it saying nc jupiter.challenges.picoctf.org 48247.

## Hints:
What kind of encoding uses dashes and dots?
The flag is in the format PICOCTF{}

## Solution:
I opened webshell  and ran the provided command:
```
nc jupiter.challenges.picoctf.org 9422
```
The response was a series of dashes and dots. I realized that this was Morse code. 
![HashCrack Screenshot](/assets/lib/tap.png)

Decoding morse code using [online tools](https://www.dcode.fr/morse-code)

## Flag:
```
PICOCTF{M0RS3C0D31SFUN2683824610#}
```