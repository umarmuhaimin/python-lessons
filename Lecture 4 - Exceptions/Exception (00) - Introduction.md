⚙️ Python Exceptions – Structured Notes

########################################################################################################################

👉 1. What Are Exceptions?

• Exceptions are errors that occur during program execution.  
• Instead of crashing, Python lets you “handle” these errors gracefully.  
• Example of a runtime error (exception):  
```python
print(10 / 0)  # ZeroDivisionError
```


👉 2. Common Built-in Exceptions

• ZeroDivisionError: Dividing by zero.  
• ValueError: Wrong data type (e.g., int("abc")).  
• TypeError: Using an invalid operation on incompatible types.  
• NameError: Using a variable that doesn’t exist.  
• IndexError: Accessing an invalid index in a list.  
• KeyError: Accessing a non-existent key in a dictionary.  
• FileNotFoundError: Opening a file that doesn’t exist.  


👉 3. Using try and except

• Used to handle errors and prevent program crashes.  
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
```


👉 4. Optional Blocks

• else: Runs only if no error occurs.  
• finally: Runs no matter what (used for cleanup actions like closing files).  
```python
try:
    f = open("file.txt")
    print("File opened successfully.")
except FileNotFoundError:
    print("File not found.")
else:
    print("No error occurred.")
finally:
    f.close()
    print("File closed.")
```


👉 5. Raising Exceptions Manually

• Use raise to create your own error intentionally.  
```python
raise ValueError("Invalid input! Please try again.")
```


👉 6. Handling Multiple Exceptions

• You can catch multiple exceptions in one block:  
```python
try:
    # some code
    pass
except (TypeError, ValueError):
    print("Something went wrong.")
```


👉 7. Why Exception Handling Is Important

• Prevents program crashes.  
• Makes your code more reliable and user-friendly.  
• Helps you debug and handle unexpected behavior.  


👉 8. Best Practices

• Only catch exceptions you can handle.  
• Keep try blocks small and specific.  
• Use clear error messages for debugging.  
