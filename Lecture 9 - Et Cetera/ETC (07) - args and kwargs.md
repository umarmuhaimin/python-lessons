⚙️ *args and **kwargs – Structured Notes

########################################################################################################################

1. What are *args and **kwargs? (Definition)

• *args collects any number of positional arguments into a tuple.  
• **kwargs collects any number of keyword arguments into a dictionary.  
• They let functions accept flexible inputs (like print(*objects, sep=...)).  


2. Capturing positional arguments

```python
def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)
```
Output:
```
Positional: (100, 50, 25)
```


3. Capturing keyword arguments

```python
def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)
```
Output:
```
Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}
```


4. Why it matters

• *args lets you accept flexible numbers of positional values.  
• **kwargs lets you accept optional named parameters without predefining them.  
• Many built-ins (like print) rely on this flexibility.  
