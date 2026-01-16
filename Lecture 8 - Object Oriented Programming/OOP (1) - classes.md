🏷️ OOP (1) – Classes – Structured Notes

########################################################################################################################

📘 What I mean by “class”

• Classes are a way, in object-oriented programming, to create my own type of data and give it a name.  
• A class feels like a mold for a type of data—a blueprint where I invent the data type and name it.  


🏗️ First pass: defining Student

```python
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
```

• By convention Student is capitalized. The ... reminds me I’ll finish that part later.  
• In get_student I can create a student of class Student with student = Student().  
• I use dot notation to access attributes of the student object.  
• Any time I create a class and use that blueprint, I create an object/instance; here, student is an object.  


🧱 Laying out expected attributes (__init__)

• Non-CS analogy: the class is a recipe; each baked cake is an object/instance. __init__ is the step where I actually mix ingredients for one cake, and self is “this cake I’m working on.”  
• Correlation: class is the blueprint; object/instance is the real thing built from it. The class defines what every Student should have (name, house), and each object stores its own values for those fields.  

• Why __init__: it’s the initializer that runs when I create a new instance; it sets up required attributes so every object starts in a valid state.  
• Why self: self is the handle to the specific instance being created/used, so assignments like self.name store data on that exact object. Without self, I’d just have local variables that disappear.  

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
```

• Inside Student, I standardize the attributes. A function inside a class is a method.  
• __init__ takes name and house, assigns them to this object; self refers to the current object just created.  
• The constructor call student = Student(name, house) triggers __init__ and produces the student.  
• Benefit: I avoid forgetting fields or creating half-initialized objects; every Student has name and house from the start.  


🔁 Minor simplification

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

• Returning Student(name, house) directly simplifies the previous version where I kept the constructor on its own line.  


📚 Further reading

• I can learn more in Python’s documentation of classes.  
