📦 OOP (10) – Instance Variables – Structured Notes

➡️ Guideline: Examples include the class definition (`class ...`) and runnable `main()` snippets so you can see how the pieces fit together.

########################################################################################################################

1. Recap: Packages as Objects

• We created a Package class as a template; each package is an instance.  
• Examples: Package 1 → Alice to Bob → 10 kg; Package 2 → Bob to Charlie → 5 kg.  


2. The Package Class

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
```


3. Creating Instances of the Class

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    # simple check that instances exist
    for package in packages:
        print(package.number)


if __name__ == "__main__":
    main()
```

• We have two objects from the same template; each stores its own data.  
• Non-CS view: two “package cards” filled out separately.  


4. What Happens When a Package Is Created

• Example: Package(1, "Alice", "Bob", 10)  
   → Python makes a new Package object.  
   → Calls __init__.  
   → self refers to that new object.  
   → Values are stored as attributes on that object.  


5. What Are Instance Variables?

• Variables that belong to one specific instance; defined via self.variable_name.  
• Each object has its own copy.  
• Here: self.number, self.sender, self.recipient, self.weight.  
• Non-CS view: each card has its own fields; changing one card doesn’t change another.  


6. Why Instance Variables Matter

• Package 1 has its own number; Package 2 has its own number.  
• Changing one doesn’t affect the other; data stays with its object.  


7. Accessing Instance Variables

• Syntax: instance.variable (e.g., package.number).  


8. Looping Through Instances

```python
for package in packages:
    print(package.number)
```

• Iteration: first package → Package(1,…); second → Package(2,…).  
• Output: 1 then 2.  


9. Proof of Independence

```python
packages = [
    Package(1, "Alice", "Bob", 10),
    Package(3, "Bob", "Charlie", 5)
]

# Output: 1, then 3
```

• Confirms values come from each instance, not shared.  


10. Printing a Prettier Output

```python
for package in packages:
    print(f"Package {package.number}")
```

• Output: Package 1 / Package 2.  


11. Accessing Multiple Instance Variables

```python
for package in packages:
    print(
        f"Package {package.number}: "
        f"{package.sender} to {package.recipient}"
    )
```

• Output:  
   → Package 1: Alice to Bob  
   → Package 2: Bob to Charlie  


12. Adding Weight

```python
for package in packages:
    print(
        f"Package {package.number}: "
        f"{package.sender} to {package.recipient}, "
        f"{package.weight} kilograms"
    )
```

• Output:  
   → Package 1: Alice to Bob, 10 kilograms  
   → Package 2: Bob to Charlie, 5 kilograms  


13. Why This Is Better Than Strings

• Strings like "Package 1: Alice to Bob, 10 kilograms" are fragile.  
• Instance variables enforce structure, avoid formatting errors, and scale as programs grow.  


14. Key Concept Clarified

• Instance variables are attributes that belong to a specific object, created when __init__ runs, and accessed via dot notation.  


15. Final Complete Example (As Taught)

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


packages = [
    Package(1, "Alice", "Bob", 10),
    Package(2, "Bob", "Charlie", 5)
]

def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(
            f"Package {package.number}: "
            f"{package.sender} to {package.recipient}, "
            f"{package.weight} kilograms"
        )


if __name__ == "__main__":
    main()
```


16. Core Takeaway (CS50 Emphasis)

• Instance variables store data specific to each object and are created when a class is instantiated.  


17. One-Sentence Summary

• Instance variables are values stored on individual objects via self, letting each instance keep its own unique data.  
