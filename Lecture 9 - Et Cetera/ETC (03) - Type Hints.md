🧭 Type Hints (with mypy) – Structured Notes

########################################################################################################################

1. Why type hints?

• Python is dynamically typed, but hints help catch mistakes early.  
• Tools like mypy check that variables match expected types.  
• Install mypy: `pip install mypy`.  


2. Basic function (no hints) — problematic

```python
def meow(n):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
```
Output (if run as-is):
```
Number: 3
Traceback (most recent call last):
  ...
TypeError: 'str' object cannot be interpreted as an integer
```
Why this error:
• input() returns a string, but the for loop expects an int to know how many times to loop.  
• Passing a str to range triggers TypeError.  


3. Add a parameter hint

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
```
Output: same TypeError as above.  
Why: we hinted the parameter but still passed a string; runtime behavior unchanged.  


4. Hint the variable too

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)
```
Output: same TypeError as above.  
Why: variable is annotated int but still holds a string from input(); mypy complains, runtime still fails.  


5. Fix by casting input

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)
```
Output (e.g., input 3):
```
Number: 3
meow
meow
meow
```
Explanation: we cast input to int, so types align and the loop runs.  


6. Return value confusion

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
```
Runtime output (input 2):
```
Number: 2
meow
meow
None
```
Why this error: meow returns None (no return), so assigning to a str variable is a mismatch; mypy warns, runtime prints “None.”  


7. Annotate the return (None)

```python
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
```
Runtime output (input 2):
```
Number: 2
meow
meow
None
```
Explanation: Return type annotated None; storing in str still causes mypy warning and prints “None.”  


8. Make it return a string

```python
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
```
Runtime output (input 2):
```
Number: 2
meow
meow
```
Explanation: Function returns a string, variable typed str, so mypy and runtime both succeed.  


9. Takeaways

• Use parameter and return hints to clarify intent.  
• Annotate variables when helpful.  
• Run `mypy your_file.py` to catch mismatches early.  
• Documentation: Python typing docs, mypy docs.  
