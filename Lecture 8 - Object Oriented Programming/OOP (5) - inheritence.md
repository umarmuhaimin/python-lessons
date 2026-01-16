🧬 OOP (5) – Inheritance – Structured Notes

########################################################################################################################

🧠 Plain-language view (non-CS)

• Inheritance: a child class reuses and extends what a parent class provides.  
• Analogy: “Student” and “Professor” both come from “Wizard”; they share wizard traits (name) but add their own (house, subject).  
• Benefit: avoid repeating shared code; changes to the parent flow to children.  


✨ Core idea

• Inheritance is one of the most powerful OOP features: a class can inherit methods, variables, and attributes from another class.  


🪄 Example: Wizard → Student/Professor

```python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...
```

• Student and Professor inherit Wizard’s __init__ logic via super().__init__(name); both get the name validation and storage.  
• super() calls the parent implementation; child classes add their own fields (house, subject).  
• Instantiations show one Wizard, one Student, one Professor with their respective data.  


⚖️ Inheritance and Exceptions (built-in hierarchy)

• Python exceptions form a hierarchy with parents/children/grandchildren.  

```
BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...
```

• This hierarchy means catching a parent (e.g., ValueError) can handle its children; it’s inheritance in action.  


📚 Further reading

• Python docs on exceptions and classes cover more inheritance patterns and best practices.  
