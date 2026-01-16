🎓 Lecture 8 – Object-Oriented Programming (OOP) – Structured Notes

🤔 What is OOP?

🧠 Plain-language example (non-CS)

• Class = a blueprint or recipe (e.g., “Student”).  
• Instance = one real object built from the class (e.g., Padma the student).  
• Class variable = a value shared by all instances from the same class (e.g., total_students).  
• Instance variable = data unique to one instance (e.g., Padma’s name, Padma’s house).  
• Instance method = action on one instance (Padma introduces herself).  
• Class method = action on the blueprint (e.g., count how many students exist).  
• Static method = related helper that doesn’t need instance data but belongs with the class.  
• Attributes = data an object carries (name, house); methods = actions it can do.  

• OOP = Object-Oriented Programming: a paradigm where code is organized around objects that bundle data (attributes) and behavior (methods).  
• Instead of writing loose functions and data structures, you define classes that model real entities (e.g., Student, Account, Order).  


🏭 Why OOP in production?

• Encapsulation: keep data + behavior together, reducing bugs from scattered state.  
• Reuse: classes and methods can be reused across features and teams.  
• Maintainability: clear boundaries make refactors safer as systems grow.  
• Extensibility: inheritance and composition make it easier to add new variants.  
• Collaboration: shared interfaces/contracts help multiple developers work in parallel.  

########################################################################################################################

🧭 Outline

• Object-Oriented Programming  
• Classes  
• raise  
• Decorators  
• Connecting to Previous Work in this Course  
• Class Methods  
• Static Methods  
• Inheritance  
• Inheritance and Exceptions  
• Operator Overloading  
• Summing Up  


💡 Object-Oriented Programming

• There are different paradigms of programming. As you learn other languages, you will start recognizing patterns like these.  
• Up until this point, you have worked procedurally step-by-step.  
• Object-oriented programming (OOP) is a compelling solution to programming-related problems.  


🚀 Starting Point (procedural)

• I started with a simple student.py script:

```python
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
```

• I note that this program follows a procedural, step-by-step paradigm—just like earlier work in the course.  


🧩 Adding Functions (abstraction)

• Drawing on earlier weeks, I created functions to abstract away parts of this program.

```python
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main()
```

• I see get_name and get_house abstract away the needs of main. The final lines tell the interpreter to run main.  


🎒 Using Tuples (two values, immutable)

• I further simplified things by storing the student as a tuple. A tuple is a sequence of values that can’t be modified. In spirit, I’m returning two values.

```python
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
```

• I notice get_student returns name, house.  


📦 Packing the Tuple

• To pack that tuple and return both items to a variable called student, I modified the code as follows.

```python
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
```

• This (name, house) return makes it obvious that two values come back together, and I can index into the tuple with student[0] or student[1].  


🔒 Immutability of Tuples (error example)

• Tuples are immutable, meaning I cannot change those values. Immutability helps me program defensively.

```python
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
```

• This code produced an error: since tuples are immutable, I can’t reassign student[1].  


📝 Using Lists (mutable)

• To give fellow programmers flexibility, I used a list instead.

```python
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()
```

• Lists are mutable, so the order of house and name can be switched. I might use this when flexibility is worth the risk of someone changing the order by mistake.  


🗂️ Using Dictionaries (key-value)

• I could also use a dictionary here; dictionaries provide key-value pairs.

```python
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
```

• In this case, two key-value pairs are returned, and I can index into the dictionary using the keys.  


⚙️ Improving the Dictionary Version

• I could still improve this: there was an unneeded variable. I removed student = {} since I didn’t need to create an empty dictionary first.

```python
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
```

• I can use {} braces in the return statement to create the dictionary and return it in the same line.  


🎯 Handling Special Cases (Padma) with Dictionary

• I handled the Padma special case in the dictionary version of the code.

```python
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
```

• Similar to earlier versions, I can use the key names to index into the student dictionary.  
