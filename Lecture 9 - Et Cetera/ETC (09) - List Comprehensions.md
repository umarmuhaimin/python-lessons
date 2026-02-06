🧾 List Comprehensions – Structured Notes

########################################################################################################################

1. What is a list comprehension? (Definition)

• A compact way to build a list in one readable expression.  
• Pattern: `[expression for item in iterable if condition]`.  


2. Uppercasing words (comprehension vs loop)

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
```
Output:
```
THIS IS CS50
```
• Replaces a map or manual loop with a single-line expression.  


3. Filtering with a comprehension (classic loop)

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
```
Output:
```
Harry
Hermione
Ron
```
• Builds list with an if-condition inside the loop.  


4. Same logic with a list comprehension

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
```
Output:
```
Harry
Hermione
Ron
```
• One line builds the filtered list—expression, loop, and condition combined.  


5. Takeaway

• Use comprehensions to create transformed/filtered lists succinctly.  
• Keep them readable: simple expressions and conditions are best.  
