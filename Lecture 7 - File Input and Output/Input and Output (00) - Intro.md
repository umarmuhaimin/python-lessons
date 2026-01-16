📁 File I/O (Complete Lecture Notes)

########################################################################################################################

1) What “File I/O” means

• So far, your programs stored data only in memory → when the program ends, the data is gone.
• File I/O lets your program save data to files and read data back later. 


2) Starting example (input → output)

```python
name = input("What's your name?" )
print(f"hello, {name}")
```


3) Collect multiple inputs in a list (but still only in memory)

```python
names = []

for _ in range(3):
    name = input("What's your name?" )
    names.append(name)
```


• Simplified:

```python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))
```


• Print sorted:

```python
names = []
for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
```

• But after the program ends, the list is still lost → that’s why we use files. 


4) open() basics (write vs append)

• Write mode "w" (overwrites file each run)

```python
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
```


• Append mode "a" (adds to the end)

```python
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(name)
file.close()
```

• Problem: names run together (no new line). 

• Fix with newline:

```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```



5) with (auto-closes the file)

```python
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```

• Key idea: with handles closing for you. 


6) Reading from a file

• Read all lines into a list

```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
```

• Output looks messy because each line already has \n. 

• Fix using rstrip():

```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
```


• Simplest pattern: loop directly over the file

```python
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
```


• Read → store → sort → print:

```python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```



7) CSV (Comma-Separated Values)

• Example CSV file students.csv:

Hermione,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin


• Read CSV by splitting strings

```python
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
```


• Cleaner: unpack into variables

```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```


• Sort as strings

```python
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
```


• Store as dictionaries (better structure)

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```


• Sort list of dictionaries using key=...

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
```


• Using lambda (one-off function):

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```



8) Why csv library matters (commas inside values)

• If CSV contains something like:

Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor

Then .split(",") breaks (too many commas). 

• Use csv.reader:

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
```


• Even better: add headers to the CSV:

name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor


• Use csv.DictReader:

```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
```



9) Writing to CSV (DictWriter)

```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```

• +1


10) Binary files + Pillow (PIL) — animated GIF “animate part”

• Binary files are 1s and 0s (images/music/etc).
• Pillow (PIL) can work with image files and create animated GIFs. 

• costumes.py:

```python
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
```

• Run:

```python
python costumes.py costume1.gif costume2.gif
```

• Then you can view the output GIF (in CS50’s environment they use code costumes.gif). 


Why Files Matter

• Files allow you to:
   → Store user data
   → Build databases
   → Save logs
   → Read large datasets
   → Share data between programs


11) Summary of Key Functions

• Function / Purpose
• open() — Open a file
• .read() — Read entire file
• .write() — Write to file
• .close() — Close file
• with — Auto-close files
• csv.reader() — Read CSV rows
• csv.writer() — Write CSV rows
• csv.DictReader() — Read CSV as dict
• csv.DictWriter() — Write CSV as dict


12) Best Practices (CS50 Emphasis)

• Always use with
• Use csv module for CSV files
• Strip newlines when reading
• Handle exceptions
• Keep file operations simple
• Don’t hardcode absolute paths


13) Big Picture Takeaways

• File I/O lets programs persist data
• Text files and CSVs are common formats
• Python provides built-in tools for file handling
• Structured data should use csv
• Clean file handling leads to reliable programs
