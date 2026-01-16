📦 OOP (11) – Instance Methods – Structured Notes

➡️ Guideline: Each example shows the class definition (`class ...`) and a runnable main loop (`def main(): ...`) so you can see how the pieces fit together.

########################################################################################################################

1. What Are Instance Methods?

• Functions that belong to a class and operate on a specific instance.  
• Always take self as the first parameter.  
• Can access/modify instance variables; represent object behavior.  


2. Starting Point: The Package Class

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
```

• Encapsulates package data via instance variables: number, sender, recipient, weight.  


3. Creating Package Instances

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    # placeholder to show the program runs
    for package in packages:
        print(package.number)


if __name__ == "__main__":
    main()
```

• Using def main(): mirrors prior patterns and makes the script runnable directly.  
• Each list element is a Package instance with its own data.  

• Alternatively, just the instances:

```python
packages = [
    Package(1, "Alice", "Bob", 10),
    Package(2, "Bob", "Charlie", 5)
]
```

• Each list element is a Package instance with its own data.  


4. Printing Package Data (Before Instance Methods)

```python
for package in packages:
    print(
        f"Package {package.number}: "
        f"{package.sender} to {package.recipient}, "
        f"{package.weight} kg"
    )
```

• Works, but formatting logic lives outside the class; repetitive.  


5. Motivation for Instance Methods

• Attach behavior to the object; encapsulate data + functionality; avoid repeated external logic.  


6. Introducing __str__ (dunder STR)

• Special instance method; called automatically by print(instance); must return a string.  


7. Defining __str__

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return "This is a package"
```


8. Testing __str__

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(package)


if __name__ == "__main__":
    main()
```

• Output:  
  This is a package  
  This is a package  
• Proves __str__ is auto-called by print.  


9. Improving __str__ Using Instance Variables

```python
def __str__(self):
    return (
        f"Package {self.number}: "
        f"{self.sender} to {self.recipient}, "
        f"{self.weight} kg"
    )
```

• Accesses instance variables via self; produces meaningful output.  


10. Printing After __str__

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(package)


if __name__ == "__main__":
    main()
```

• Output:  
  Package 1: Alice to Bob, 10 kg  
  Package 2: Bob to Charlie, 5 kg  
• Printing logic now lives inside the class.  


11. Instance Methods for Behavior

• Beyond formatting: e.g., calculating shipping cost depends on one package’s data → instance method.  


12. Using an Instance Method

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(
            f"{package} costs "
            f\"${package.calculate_cost(2)}\"
        )


if __name__ == "__main__":
    main()
```

• Assumes cost = $2 per kg.  


13. Defining calculate_cost

```python
def calculate_cost(self, cost_per_kg):
    return self.weight * cost_per_kg
```

• Uses instance data (self.weight) plus argument cost_per_kg; returns total.  


14. Full Class With Instance Methods

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return (
            f"Package {self.number}: "
            f"{self.sender} to {self.recipient}, "
            f"{self.weight} kg"
        )

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg
```


15. Final Output

• Final output from the combination of the full class with instance methods and the main loop:

```python
def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(f"{package} costs ${package.calculate_cost(2)}")


if __name__ == "__main__":
    main()
```

• Output:  
  Package 1: Alice to Bob, 10 kg costs $20  
  Package 2: Bob to Charlie, 5 kg costs $10  


16. Why Instance Methods Matter

• Enable clean OO design, encapsulation of logic, behavior tied to data, reusable/readable code.  


17. Special vs Normal Instance Methods

• __str__: defines how the object prints.  
• calculate_cost: adds real behavior.  
• Both require self.  


18. Core Takeaway (CS50 Style)

• Instance methods are functions inside a class that operate on individual instances via self.  


19. One-Sentence Summary

• Instance methods let objects act on their own data, combining behavior and state inside the class.  
