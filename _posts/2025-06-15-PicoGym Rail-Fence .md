---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-06-15
categories: ["cryptography"]
tags: ["medium","Railfence"]

---
# PicoGym cryptography |Rail-Fence |Medium |PicoCTF

# Rail-fence

## Description :
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher)
Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message [here](https://en.wikipedia.org/wiki/Rail_fence_cipher)
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.


## Hints:
Once you've understood how the cipher works, it's best to draw it out yourself on paper.

Encoded Message:
```
Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6
```
## Solution:

 It said in the description that it is the rail fence cipher with 4 rails I used rail fence decode with the key being set to 4.
 So I justed used cyberchef.
 Here is the result:

 ![HashCrack Screenshot](/assets/lib/rail.png)
 ![HashCrack Screenshot](/assets/lib/fence.png)

## Flag:
 ```picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_4ND_83F6D8D7} ```