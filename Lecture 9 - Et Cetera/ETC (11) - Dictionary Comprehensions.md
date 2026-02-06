🗂️ Dictionary Comprehensions – Structured Notes

########################################################################################################################

1. What is a dict comprehension? (Definition)

• A one-liner to build dictionaries: `{key_expr: value_expr for item in iterable if condition}`.  
• Same idea as list comprehensions, but produces key–value pairs.  


2. Baseline (no comprehension)

```python
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)
```
Output:
```
[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]
```


3. Dict comprehension producing list of dicts

```python
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)
```
Output:
```
[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]
```
• One line replaces the explicit loop.  


4. Dict comprehension producing a single dict

```python
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
```
Output:
```
{'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}
```
• Keys are names, value is house; concise and readable.  


5. Takeaway

• Dict comprehensions let you construct dictionaries succinctly.  
• Use them to map or transform iterables into key–value structures, optionally with conditions.  
