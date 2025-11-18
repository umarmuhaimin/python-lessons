### Objective : In this python file, we will learn ways to print data from a list ###

#########################################################################################################

# 🔹 Beginner_level_list 
students = ["Hermione", "Harry", "Ron"]
print(students[0])
print(students[1])
print(students[2])
# Output : 
# → Hermione [0]
# → Harry [1]
# → Ron [2]

# 👉 Order/arrangement matters in a list that stores data.

# 🔹 Forloop_list
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
# Output : 
# → Hermione [0]
# → Harry [1]
# → Ron [2]

# 🔹 Range_list
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(students[i])         # from i = 0 → i = 2
# Output : 
# → Hermione [0]
# → Harry [1]
# → Ron [2]

# 👉 Explaination : 
# → range() only accepts numbers.
# → len() tells us how many items are in the list.  So if the item inside the list is a string/integer/etc ; len() will convert the data inside the list into numbers.
# → By combining them, we can loop through a list by its indexes.
# → This lets us access each item one by one using list[index].
# → Because i is being used as an index to access each element of the list.
# → So effectively, the code prints all items in the list one by one.

# 👉 Why len() is needed:
# → len(students) → gives the number of items in the list (3).
# → range(3) → now Python knows to loop i = 0, 1, 2.
# → That’s why len() is used: it translates the list into a number that range() can work with.

# 👉 Step by step:
# → len(students) → gives 3 (because there are 3 names).
# → range(3) → generates numbers [0, 1, 2].
# → The loop runs with i = 0, then i = 1, then i = 2 one at a time.
# → Each time, students[i] prints:
#    → When i = 0 → "Hermione"
#    → When i = 1 → "Harry"
#    → When i = 2 → "Ron"

# 👉 Summary : 
# → i itself is just a number (the index).
# → students[i] means: "go into the list students and get the item at position i one by one from the first item until the last item from the list."
# So every loop, i changes → students[i] prints one single item.
# Since you have a loop variable "i" from "for i in range()" → order/arrangement matters.

# 🔹 Printing List with Position Numbers 
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i, students[i])
# Output :
# → 0 Hermione
# → 1 Harry
# → 2 Ron

# 🔹 Printing List with Position Numbers starting from "1" instead of "0"
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])
# Output :
# → 1 Hermione  👉 i = 0 + 1 → 1
# → 2 Harry     👉 i = 1 + 1 → 2
# → 3 Ron       👉 i = 2 + 1 → 3

#########################################################################################################

### Dictionaries (dict) ###
 
# 👉 A collection of key-value pairs, written with { }.
# 👉 Syntax: {key: value}
# 👉 Keys are unique, values can be repeated.

# 🔹 Accessing Dictionary Values for each respective keys.
# → Print the name of houses for each respective person 

# 👉 General method for dict :
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"]) 
# Output :
# → Gryffindor
# → Gryffindor
# → Gryffindor
# → Slytherin

# 👉 forloops_dict :
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
for student in students:
    print(student, students[student], sep=", ")
# Output :
# → Hermione, Gryffindor
# → Harry, Gryffindor
# → Ron, Gryffindor
# → Draco, Slytherin

# 👉 List of Dictionaries : Storing Multiple Dictionaries in a List / Storing multiple pairs of key_and_value in a list.
# a dictionary is when you have a single set of {key: value}
# [1] dict means 1 set of {key: value} → {key: value}
# [2] dict means 2 set of {key: value} → {key: value}, {key: value}
# [3] dict means 3 set of {key: value} → {key: value}, {key: value}, {key: value}
# In short, if you have multiple dictionaries → USE List of dictionaries. List is because you have "[]".
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
{"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
# Output :
# → Hermione, Gryffindor, Otter
# → Harry, Gryffindor, Stag
# → Ron, Gryffindor, Jack Russel terrier
# → Draco, Slytherin, None











