📦 Unpacking – Structured Notes

########################################################################################################################

1. What is unpacking? (Definition)

• Unpacking spreads a container (list/tuple/dict) into separate variables or arguments.  
• * expands sequences positionally; ** expands dictionaries by name.  

2. Simple unpacking

```python
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
```
• Splits input on space, assigns first word to first, ignores the rest with _.  


3. Function without unpacking (verbose)

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")
```
Output:
```
5395 Knuts
```


4. Passing list elements manually

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]), "Knuts")
```
Output:
```
5395 Knuts
```
• Works, but indexing is repetitive.  


5. Sequence unpacking with *

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(*coins), "Knuts")
```
Output:
```
5395 Knuts
```
• * expands the list into positional arguments.  


6. Keyword arguments (order independent)

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")
```
Output:
```
5395 Knuts
```
• Passing by name lets you reorder safely.  


7. Dictionary unpacking with **

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")
```
Output:
```
5395 Knuts
```
• ** expands a dict into keyword arguments (keys must match parameter names).  


8. Takeaway

• * unpacks sequences into positional args; ** unpacks dictionaries into keyword args.  
• Use unpacking to keep calls concise and order-agnostic.  
