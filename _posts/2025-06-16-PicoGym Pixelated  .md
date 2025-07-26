---
CTF: "PicoCTF"
author: Xpl01te4gl3
date: 2025-05-25
categories: ["cryptography"]
tags: ["medium","visual_cryptography"]

---
# PicoGym cryptography |Pixelated |Medium |PicoCTF2022|


## Description:
I have these 2 images, can you make a flag out of them?
scrambled1.png scrambled2.png

## Hints:
https://en.wikipedia.org/wiki/Visual_cryptography
Think of different ways you can “stack” images

## Solution:
We can use the concept of visual cryptography to solve this problem.
```
Visual Cryptography is a cryptographic technique where an image is divided into multiple shares (or layers) so that individually, they reveal no information. However, when these shares are overlaid or stacked together, the original image or secret can be visually reconstructed without needing a computer—just the human eye
```

so basically, we need to combine two photos that were given to us in order to retrieve the original image.
I wrote a Python code using chatGPT for this purpose:
```
from PIL import Image

def combine_images(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Ensure both images have the same size
    if image1.size != image2.size:
        raise ValueError("Images must have the same size")

    # Combine the images using a simple averaging technique
    combined_image = Image.blend(image1, image2, alpha=0.5)

    # Save the combined image
    combined_image.save(output_path)

if __name__ == "__main__":
    # Provide the paths of the input images and the desired output path
    image1_path = "scrambled1.png"
    image2_path = "scrambled2.png"
    output_path = "combined_image.png"

    combine_images(image1_path, image2_path, output_path)
```

  This is what i got after running the code:


  ![HashCrack Screenshot](/assets/lib/combined_image.png)

  After Zooming it in a website  https://29a.ch/photo-forensics/#forensic-magnifier

  I can see the flag is:
```
  picoCTF{1b867c3e}
```