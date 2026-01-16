🖼️ Pillow (Python Image Library) – Structured Notes

########################################################################################################################

1. What is Pillow?

• Pillow is a Python library used for image manipulation.
• It allows you to:
   → Open images
   → Inspect image properties
   → Rotate images
   → Apply filters
   → Save modified images
• Pillow works with image files on your computer (JPEG, PNG, etc.).


2. The Problem Being Solved

• Given an image (in.jpeg) that is upside down.
• Goal:
   → Open the image
   → Rotate it so it’s right side up
   → Save the corrected image
• Example image: The Great Wave off Kanagawa by Hokusai


3. Creating the Program (image.py)

• Start with a standard Python structure: define main(); call main() at the bottom.

```python
def main():
    pass


if __name__ == "__main__":
    main()
```


4. Importing Pillow

• Pillow is accessed through the PIL module.
• We specifically need the Image class.

```python
from PIL import Image
```

• Explanation: Image is a class representing an image; it provides methods to open, manipulate, and save images.


5. Opening an Image

• Use Image.open() to load an image file; this returns an image object.

```python
img = Image.open("in.jpeg")
```

• Similar to clicking and opening an image manually. Once opened, Python can manipulate the image.


6. Closing an Image (Manual Way)

```python
img.close()
```

• Good practice to close files and images when done; problem: easy to forget to close images.


7. Best Practice: Using with

• Automatically opens and closes the image.

```python
with Image.open("in.jpeg") as img:
    pass
```

• Explanation:
   → While inside the with block: the image is open; you can manipulate it.
   → Once you exit the block: the image closes automatically.


8. Inspecting Image Properties

• Getting Image Size

```python
with Image.open("in.jpeg") as img:
    print(img.size)
```

• Output example: (1052, 720)
   → Meaning: 1052 pixels wide; 720 pixels tall.

• Getting Image Format

```python
with Image.open("in.jpeg") as img:
    print(img.format)
```

• Output: JPEG; confirms the file type.


9. Rotating an Image

• The image is upside down; rotate it 180 degrees.

```python
with Image.open("in.jpeg") as img:
    img = img.rotate(180)
    img.save("out.jpeg")
```

• Explanation:
   → rotate(180) flips the image
   → save() writes the new image to disk
   → Original image remains unchanged


10. Result

• A new file appears: out.jpeg
• The image is now right side up


11. Applying Image Filters

• Pillow supports filters via ImageFilter.
• Import ImageFilter:

```python
from PIL import Image, ImageFilter
```


12. Blur Filter Example

```python
from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("out.jpeg")


if __name__ == "__main__":
    main()
```

• Explanation:
   → ImageFilter.BLUR applies a blur effect
   → Image is opened, rotated, blurred, saved


13. Edge Detection Filter

• Another available filter: FIND_EDGES; highlights edges in the image.

```python
from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


if __name__ == "__main__":
    main()
```

• Result:
   → The image is rotated
   → Edges are emphasized
   → Creates a stylized version of the artwork


14. What We Learned

• Using Pillow, we can:
   → Open images (Image.open)
   → Automatically manage resources (with)
   → Inspect image attributes (size, format)
   → Rotate images (rotate)
   → Apply filters (filter)
   → Save modified images (save)


15. Key Takeaways

• Pillow treats images like objects.
• Image manipulation is done through methods.
• with is safer than manual open/close.
• Filters allow creative and analytical image processing.
• Pillow supports far more features than shown (crop, resize, color, etc.).


16. Final Summary

• Pillow is a powerful image-processing library.
• Enables file I/O with images.
• Integrates naturally with Python syntax.
• Useful for:
   → Graphics
   → Data visualization
   → Automation
   → Creative projects
