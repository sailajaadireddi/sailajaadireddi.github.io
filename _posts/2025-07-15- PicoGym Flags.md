---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-07-15
categories: ["cryptography"]
tags: ["medium"]
---

# PicoGym cryptography |Flags |Medium |PicoCTF

# Flags

## Description:
What do the flags mean?

## Hints:
The flag is in the format PICOCTF{}

The flags given:

![HashCrack Screenshot](/assets/lib/flags.png)

## Solution:
The image seems like it is already in the correct picoCTF{...} flag format.

we can see the 3rd and 5th character of the ciphertext above being replaced by the same flag. The 2 “C”s in picoCTF have been replaced by the same flag.

ince I had no prior knowledge about the flags, I searched “blue flag with white square” on Google, and checked the top search results. This brought me to [this](https://www.nps.gov/media/photo/gallery-item.htm?id=29091438-15a4-447d-851c-5a9481d211f7&gid=791FF38A-DF86-4963-932F-EE7641143F49)page.

![HashCrack Screenshot](/assets/lib/flags2.png)

By mapping each signal flag to its corresponding letter via the ICS chart, the full message was revealed as:
## Flag:
```
PICOCTF{F1AG5AND5TUFF}
```