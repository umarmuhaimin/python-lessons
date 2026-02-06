🧭 argparse – Structured Notes

########################################################################################################################

1. Why argparse? (Definition)

• argparse is Python’s built-in command-line parser; it reads flags/values for you.  
• Manually parsing sys.argv gets messy as options grow.  
• argparse handles parsing, validation, help text, types, and defaults so you write less error-prone code.  


2. Manual parsing with sys.argv (baseline)

```python
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py [-n NUMBER]")
```
Output examples:
```
$ python meows.py
meow
$ python meows.py -n 3
meow
meow
meow
$ python meows.py -x
usage: meows.py [-n NUMBER]
```
• Works, but logic grows unwieldy with more options.  


3. Basic argparse setup

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
```
Output:
```
$ python meows.py -n 2
meow
meow
```
• argparse builds the parser, defines expected args, and parses them for you.  


4. Adding description and help

```python
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
```
Output:
```
$ python meows.py -h
usage: meows.py [-h] [-n N]

Meow like a cat

options:
  -h, --help  show this help message and exit
  -n N        number of times to meow
```
• description and help give users built-in guidance via -h/--help.  


5. Defaults and types

```python
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
```
Outputs:
```
$ python meows.py
meow
$ python meows.py -n 3
meow
meow
meow
```
• type=int enforces integer input; default=1 handles missing -n.  


6. Takeaway

• Use argparse for robust CLI parsing: descriptions, help, defaults, and type checking with minimal code.  
