🧊 Constants – Structured Notes

########################################################################################################################

1. What are “constants” in Python?

• Idea: variables you shouldn’t change (defensive coding).  
• Python doesn’t enforce immutability; all-caps names are an honor system signal.  


2. Module-level constant example

```python
MEOWS = 3

for _ in range(MEOWS):
    print("meow")
```
Output:
```
meow
meow
meow
```
• MEOWS is treated as a constant by convention (ALL CAPS, defined at the top).  
• Python will let you reassign it—so discipline is required.  


3. Class “constant” example

```python
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
```
Output:
```
meow
meow
meow
```
• MEOWS lives on the class; every instance can read it via Cat.MEOWS.  
• Still not enforced, but centralizes the value and signals “don’t change.”  


4. Takeaway

• Use ALL_CAPS at the top (or on the class) to mark intended constants.  
• Python won’t stop reassignment—team discipline and code reviews do.  
