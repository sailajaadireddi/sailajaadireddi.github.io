---
layout: post
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-07-15
categories: ["cryptography"]
tags: ["medium","vigenere","key"]

---
# PicoGym cryptography |Credstuff |Medium |PicoCTF2022|

# Credstuff

![HashCrack Screenshot](/assets/lib/pic14.png)

[leak](https://artifacts.picoctf.net/c/534/leak.tar)


### Hints:
Maybe other passwords will have hints about the leak?

### Solution:
let’s write a python program that finds the corresponding password for the user ‘cultiris’

According to the task description the n-th user corresponds to the n-th password.

So my task here is to find the position of the user ‘cultiris’ in the file ‘usernames.txt’ and find the password with the same position in the file ‘passwords.txt’

Here is the program I came up with:
```
username="cultiris"

username_file="leak/usernames.txt"

password_file="leak/passwords.txt"

def search_string_in_file(file_name, string_to_search):

    """Search for the given string in file and return lines containing that string,

    along with line numbers"""

    line_number = 0

    list_of_results = []  # Open the file in read only mode

    with open(file_name, 'r') as read_obj:
        for line in read_obj:

            # For each line, check if line contains the string

            line_number += 1

            if string_to_search in line:

                # If yes, then add the line number & line as a tuple in the list

                list_of_results.append((line_number, line.rstrip()))

    # Return list of tuples containing line numbers and lines where string is found

    return list_of_results



print(search_string_in_file(username_file, username))
lines = []                             		
with open ('leak/passwords.txt', 'rt') as psswd_file: 

    for line in psswd_file:               
        lines.append(line)   

print(lines[377])
```
Using my python program I found the username ‘cultiris’ on line 378:

So all I have to do now is to extract line 378 of the file ‘passwords.txt’.
I got this:
```
cvpbPGS{P7e1S_54I35_71Z3}
```
This seems to be encrypted.

I will Use a online tool [ROT13] to decrypt this.

### Flag:
```
picoCTF{C7r1F_54V35_71M3}
```