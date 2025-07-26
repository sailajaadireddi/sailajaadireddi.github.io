---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-28
categories: ["cryptography"]
tags: ["medium","stegseek"]

---
# PicoGym cryptography |HideToSee |Medium |PicoCTF2022|

# HideToSee

![HashCrack Screenshot](/assets/lib/pic11.png)

## Hints:
Download the image and try to extract it.

## Solution:
Download the image. It looks like this:

![HashCrack Screenshot](/assets/lib/atbash.jpg)

After opening the file, we now know that the flag is likely encrypted using the Atbash Cipher. 

However, since we are tasked to extract hidden files, I tried using Stegseek

![HashCrack Screenshot](/assets/lib/pic12.png)

So Extracted Data is:
```
krxlXGU{zgyzhs_xizxp_7142uwv9}
```
![HashCrack Screenshot](/assets/lib/pic13.png)

 We can simply use an online Atbash Cipher tool to decrypt the flag. I used this.
## Flag:
```
picoCTF{atbash_crack_7142fde9}
```