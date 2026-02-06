🔢 enumerate – Structured Notes

########################################################################################################################

1. What is enumerate? (Definition)

• enumerate(iterable, start=0) yields pairs of (index, value) while looping.  
• Avoids manual range(len(...)) and keeps code cleaner.  


2. Manual indexing (baseline)

```python
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```
Output:
```
1 Hermione
2 Harry
3 Ron
```


3. Using enumerate

```python
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)
```
Output:
```
1 Hermione
2 Harry
3 Ron
```
• enumerate hands you both index and value; no need for range or indexing.  


4. Takeaway

• Prefer enumerate when you need indexes while iterating—it’s clearer and less error-prone.  
