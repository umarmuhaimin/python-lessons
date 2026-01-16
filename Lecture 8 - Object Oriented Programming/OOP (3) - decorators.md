🏷️ OOP (3) – Decorators & Properties – Structured Notes

########################################################################################################################

🔎 Plain-language view (non-CS)

• Think of a property as a controlled gate: when someone sets or gets a value, I can run checks first.  
• @property is like putting a badge on a function that says “I’m the gatekeeper for this attribute.”  
• The real data lives in a private-ish spot (like _house); the property controls how others interact with it.  


🔐 Adding a validated property (house)

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

• @property defines house as a property; @house.setter runs whenever house is set (e.g., student.house = "Gryffindor").  
• I validate inside the setter and store the actual value in _house (prefixed underscore signals “don’t touch directly”).  
• The getter returns _house so users see a validated value; the setter enforces the rules.  


🛡️ Protecting both name and house

• Why getter/setter: they let me validate and control access while keeping a simple attribute-like syntax (student.name).  
• Setters enforce rules (no empty name, valid house) before storing data; getters return the cleaned/approved value.  
• Decorators like @property and @<attr>.setter turn plain methods into this controlled interface without changing how I read/write attributes.  

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

• Same pattern for name: @property + @name.setter validate and store into _name.  
• Properties give me a clean syntax (student.name) but still allow validation and encapsulation behind the scenes.  


📚 Further reading

• Python docs on methods and properties cover more patterns and best practices.  
