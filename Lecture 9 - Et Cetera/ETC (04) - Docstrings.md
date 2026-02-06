📝 Docstrings – Structured Notes

########################################################################################################################

1. What is a docstring? (Definition)

• A docstring is a string literal placed inside a function/module/class to document what it does.  
• Written with triple quotes; tools (and help()) read it for documentation.  

2. Basic docstring

```python
def meow(n):
    """Meow n times."""
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
```
Output (Number = 2):
```
meow
meow
```
• Triple double quotes document what the function does.  


2. Expanded/docstring format

```python
def meow(n):
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
```
Output (Number = 2):
```
meow
meow
```
• This style lists parameters, types, raises, returns, and return types—useful for tools like Sphinx to auto-generate docs.  


3. Takeaway

• Use docstrings to describe purpose, parameters, return values, and exceptions.  
• Standardized docstrings make automated documentation possible (e.g., Sphinx).  
