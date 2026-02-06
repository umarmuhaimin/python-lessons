🎉 This Was CS50! – Structured Notes

########################################################################################################################

1. Fun finale program

```python
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
```
Output (example input “CS50 rocks”):
```
 ______________
< CS50 rocks >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
• cowsay prints the message in cow ASCII art; pyttsx3 speaks it aloud.  


2. Takeaway

• Combines third-party libraries (cowsay, pyttsx3) for a playful demo of Python’s extensibility.  
