🧱 OOP (8) – Classes Advanced (CS50 Short) – Structured Notes

➡️ Guideline: Examples include the class definition (`class ...`) and runnable `main()` snippets so you can see how the pieces fit together.

########################################################################################################################

1. Motivation: Why Strings Are a Bad Fit

• Initial approach (fragile):

```python
packages = [
    "Package 1: Alice to Bob, 10 kilograms",
    "Package 2: Bob to Charlie, 5 kilograms"
]
```

• Problems with using strings:
   → Too flexible; no enforced structure.
   → Easy to mess up ordering/formatting/miss fields.
   → Hard to extract sender/recipient/weight or scale reliably.


2. Idea: Represent Packages as Objects

• A package is a real-world object with fields:
   → ID (number), sender, recipient, weight.
• Goal: rigid structure that always stores these correctly.
• 👉 Classes give us that structure.


3. What Is a Class?

• Class = template/blueprint to create objects.  
• Lets me encapsulate related data, enforce structure, avoid formatting errors.


4. Creating a Class

```python
class Package:
    ...
```

• Use class keyword; class names are capitalized by convention.  
• Package is a template, not an actual package yet.


5. The __init__ Method (Constructor)

• __init__ runs automatically when an object is created; initializes data.

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
```


6. Understanding self

• self refers to the specific object being created/used.  
• Each instance stores its own data:
   → self.number, self.sender, self.recipient, self.weight.


7. What the Constructor Stores

• Each Package object will have instance variables:
   → number, sender, recipient, weight.


8. Creating Package Objects (Instances)

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

• Calling Package(...) triggers __init__, creates objects, and stores data safely.


9. How Object Creation Works (Step-by-Step)

• Example: Package(1, "Alice", "Bob", 10)
   → Python creates a Package object.
   → Calls __init__.
   → Assigns self.number = 1, self.sender = "Alice", self.recipient = "Bob", self.weight = 10.


10. Final Program Structure (Exact Concept)

```python
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Charlie", 5)
    ]

    for package in packages:
        print(
            f"Package {package.number}: "
            f"{package.sender} to {package.recipient}, "
            f"{package.weight} kg"
        )


if __name__ == "__main__":
    main()
```


11. Why This Is Better Than Strings

• Data is structured; each package always has the same fields.  
• Easier to access attributes, extend functionality, and avoid formatting bugs.  


12. What This Short Covers (and What It Doesn’t)

✅ Covered: why classes help, class syntax, __init__, self, creating objects, encapsulating data.  
❌ Not covered yet: methods, printing objects, validation, properties, inheritance (later shorts).  


13. Core Takeaway (CS50 Emphasis)

• Classes give structure to data that would be messy, fragile, and error-prone as raw strings.  


14. One-Sentence Summary

• A class is a template that lets me create objects with consistent, structured data instead of relying on fragile strings.  
