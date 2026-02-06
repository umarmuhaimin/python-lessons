🔍 filter – Structured Notes

########################################################################################################################

1. What is filter? (Definition)

• filter(function, iterable) keeps only the items where function(item) returns True.  
• Think “select rows matching a condition” without writing a manual loop.  


2. Filtering with a named function

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
```
Output:
```
Harry
Hermione
Ron
```
• is_gryffindor returns True/False; filter keeps only True items.  


3. Filtering with a lambda (inline function)

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
```
Output:
```
Harry
Hermione
Ron
```
• Lambda is a short, anonymous function—handy for simple conditions.  


4. Takeaway

• Use filter to express “keep only the items that match this condition.”  
• Works with any iterable and any predicate (function returning bool).  
