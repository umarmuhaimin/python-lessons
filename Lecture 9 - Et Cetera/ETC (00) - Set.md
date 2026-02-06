🧰 Et Cetera – Sets (Python) – Structured Notes

########################################################################################################################

1. Big Picture

• “Et cetera” = “and the rest”: this is where the leftover Python ideas live.  
• A set in Python is just a collection that cannot contain duplicates.  


2. Manual Deduplication (lists)

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
```
Output:
```
Gryffindor
Ravenclaw
Slytherin
```

• Here we keep a list `houses`, check for duplicates by hand, and append only new items.  


3. Using set for Automatic Deduplication

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
```
Output:
```
Gryffindor
Ravenclaw
Slytherin
```

• Definition: a set is an unordered collection where every element is unique.  
• No duplicate check needed—`set.add()` automatically ignores repeats.  
• `sorted(houses)` converts the set to a sorted list so we can print it nicely.  


4. Why use a set?

• Removes duplicates for you.  
• Great when you care about membership/uniqueness more than order.  
• Adding, removing, and membership checks are fast.  


5. Learn more

• See Python’s docs on `set` for union, intersection, difference, and set comprehensions.  
