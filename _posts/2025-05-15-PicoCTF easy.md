---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-15
categories: ["cryptography"]
tags: ["easy"]

---
# PicoCTF Challenges| Easy|PicoGym

##  HASHCRACK
Author: Nana Ama Atombo-Sackey  
Category: Cryptography  
Difficulty: Easy

### Challenge Overview:
 ![HashCrack Screenshot](/assets/lib/hashcrack.png)

### Hints Given:
•	Understanding hashes is very crucial. Read more here.

•	Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.

•	Tried using any hash cracking tools?

### Access the server Using Netcat:
netcat is network communnication tool, its commonly used for interacting with remote servers.

![Hashcrack Screenshot](/assets/lib/Picture1.png)
In this challenge, I will use CrackStation,
### a free online password cracking tool that supports a wide range of hash types. ###

![Hashcrack Screenshot](/assets/lib/Picture2.png) 
after cracking this hash, when i enter in this terminal , its again show another hash  

  
![Hashcrack Screenshot](/assets/lib/Picture3.png)


![Hashcrack Screenshot](/assets/lib/Picture4.png)


![Hashcrack Screenshot](/assets/lib/Picture5.png)
 
![Hashcrack Screenshot](/assets/lib/Picture6.png)
 

this was final hash  AND I got the flag:
Flag: 
```
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_36a1cf73}   
```
## EVEN RSA CAN BE BROKEN 

Author: MICHAEL CROTTY 
Category: Cryptography  
Difficulty: Easy

![Hashcrack Screenshot](/assets/lib/Picture7.png)  

### Hints: ###
How much do we trust randomness?
Notice anything interesting about N?
Try comparing N across multiple requests

When you connect with nc verbal-sleep.picoctf.net 51510 you will get output that looks like this:
#### N: 17537614138261784213928370696328752813986709042120259741743863531969271925248508130709263987579968737098825108090143054462035829031497144145084077726439478 
e: 65537  

Ciphertext: 1862202474168637121872319135644317889384481444154089212360721245109801826108338981069221317033529716486407831083567338102494200390951480362472079543955817
###

It will change every time you run it so whatever script or way you solve it will have to be in a different terminal. This is a script that would work:

```
from Crypto.Util.number import long_to_bytes
N = 17537614138261784213928370696328752813986709042120259741743863531969271925248508130709263987579968737098825108090143054462035829031497144145084077726439478
e = 65537
c = 1862202474168637121872319135644317889384481444154089212360721245109801826108338981069221317033529716486407831083567338102494200390951480362472079543955817
q = N // 2

phi = q - 1
d = pow(e, -1, phi)
m = pow(c, d, N)

print(long_to_bytes(m).decode())
```
Keep in mind to run this script you need to have pycryptodome: 

```
pip install pycryptodome. 
``` 
After running the script you should get the flag.
the flag is :
```
Flag: picoCTF{tw0_1$_pr!m38177...}
```
  

# 13 #
 ### Description: ###
 Cryptography can be easy ,do you know what ROT13 IS ?
 #### cvpbPGS{abg_gbb_onq_bs_n_ceboyrz} ####
### Hints :
This can be solved online if you don't want to do it by hand!  

We can observe the encoded cipher text format here
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
The challenge description already mentions ROT13. So we can use the ROT13 decoder to decode the cipher text. The decoded cipher
#### ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it ####

![Hashcrack Screenshot](/assets/lib/Picture8.png)    

Here your flag:
```
picoCTF{not_too_bad_of_a_problem}
```


## THE NUMBERS ##
author:DANNY

### Description : ###
The numbers.... what do they mean?

### HINTS: ###
The flag is in the format PICOCTF{}

Clicking “numbers” in the challenge leads to an image of numbers. 
![Hashcrack Screenshot](/assets/lib/Picture9.png)

Initially, the array of numbers might seem confusing. But after closer inspection, 
we notice the numbers range from 1 to 26 — matching the position of letters in the alphabet.

We get the Final flag:
```
PICOCTF{THENUMBERSMASON}
```

## MOD 26: ##
### DESCRIPTION: ###
 Cryptography can be easy ,do you know what ROT13 IS ?
 #### cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh} ####

### Hints: ###
This can be solved online if you don't want to do it by hand!

The problem provides what seems to be a ciphertext:
```
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}
```
We have decoded the following flag using the CYBER CHEF tool:
![Hashcrack Screenshot](/assets/lib/Picture10.png)

the decoded flag is:
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}
```

## INTERENCDEC: ##
![Hashcrack Screenshot](/assets/lib/Picture11.png)

Hints:
Engaging in various decoding processes is of utmost importance
Can you get the real meaning from this file


 Upon downloading and inspecting the file, I immediately recognized the structure of the content as a Base64-encoded string. A common indicator of Base64 encoding is the presence of one or two equals signs (=) at the end of the string, which acts as padding. The content of "enc_flag" was as follows: 
 #### YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg== ####
 To decode this, I used the following command:
 echo YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg== | base64 --decode
This revealed another encoded string:
 ```
 b’d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==’
 ```
The presence of b' at the start and quotation marks around the text seemed out of place—likely an obstruction of the encoding process or something designed to throw off the decoding process. By removing these extraneous characters, I was left with the following string:
``` 
d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==
```
Once again, the double equals sign at the end confirmed it was another Base64-encoded string. I decoded it using the same method, which gave me the following text:
```
wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}
```

Although this looked promising, it didn’t yet reveal the flag. Recognizing the need for further decryption, I used an online tool called dCode, which has a cipher identifier tool and offers other cryptographic utilities. By inputting the decoded string, the tool identified it as a Caesar cipher.

Using the dCode tool’s Caesar cipher decryption utility, I was able to decrypt the message, which revealed the final flag:

![Hashcrack Screenshot](/assets/lib/Picture12.png)

The Decoded flag :
```
picoCTF{caesar_d3cr9pt3d_a47c6d69}
```
#### I hope you enjoyed this writeup!  #### 
#### Happy Hacking ####