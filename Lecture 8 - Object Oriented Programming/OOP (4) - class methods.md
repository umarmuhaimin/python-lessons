🏷️ OOP (4) – Class Methods – Structured Notes

########################################################################################################################

🧠 Plain-language view (non-CS)

• Class method = a function on the blueprint itself, not on one specific object.  
• Analogy: there’s only one Sorting Hat; I ask the hat (the blueprint) to sort, without making a copy of the hat.  
• Instance method = action on one object (e.g., one specific hat or student). Class method = action on the class as a whole.  


🔎 When to use class methods

• When behavior doesn’t depend on a specific object’s state.  
• When you want to call something via ClassName.method(...) instead of instance.method(...).  


🎩 Example: Sorting Hat (no classmethod)

```python
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")
```

• Here sort is an instance method; I must instantiate hat = Hat() to use it.  


🎩 Example: Sorting Hat as a @classmethod

```python
import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
```

• __init__ removed; no instance needed.  
• self is irrelevant; replaced by cls to refer to the class.  
• sort can be called directly on Hat. Houses live on the class, so every call sees the same list.  


🎓 Applying @classmethod to Student

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
```

• get_student was removed; get is now a @classmethod.  
• I can call Student.get() without first creating a Student instance.  
• cls(name, house) constructs the object, so subclasses can reuse get and still return the right subclass.  


🔗 Why class methods matter

• They let me expose constructor-like helpers without needing a preexisting object.  
• Useful for alternate constructors, shared utilities, or when state is at the class level.  


🧊 Static Methods (quick note)

• Beyond @classmethod (distinct from instance methods), there’s also @staticmethod.  
• Static methods live on the class but don’t touch class or instance data; they’re just helpers grouped with the class.  
• Not covered in depth here, but worth exploring to see how they differ from class methods.  
