### Python Lesson: Lists (and Related Concepts) ###

#########################################################################################################

# 🔹 Lists

# 👉 A list is a collection of values stored inside square brackets [ ].

# Example:
# fruits = ["apple", "banana", "cherry"]

# 👉 Items are ordered by index numbers, starting from 0.
#     → fruits[0] → "apple"
#     → fruits[1] → "banana"

# 👉 Lists can store mixed data types (numbers, strings, booleans, etc.).

#########################################################################################################

# 🔹 Accessing Elements 

# 👉 Use indexing with [] to get specific items.

# 👉 Example:
#     → print(fruits[0])  # apple
#     → print(fruits[2])  # cherry

#########################################################################################################

# 🔹 len() Function

# 👉 Built-in function that returns the number of items in a container.

# 👉 Works with:
#     Strings → return number of characters.
#     Lists → return number of elements.
#     Tuples → return number of elements.
#     Dictionaries → return number of key-value pairs.
#     Sets → return number of unique elements.
#     Ranges → return number of items in the range.

# 👉 Examples:
#     → print(len("hello"))         # 5  [string]
#     → print(len([1, 2, 3, 4]))    # 4  [integer]
#     → print(len({"a": 1, "b": 2})) # 2 [dictionary]

#########################################################################################################

# 🔹 Dictionaries (dict)
 
# 👉 A collection of key-value pairs, written with { }.

# 👉 Syntax: {key: value}

# 👉 Example:
#     → student = {"name": "Harry", "house": "Gryffindor", "patronus": "stag"}
#     → print(student["name"])   # Harry

# 👉 Keys are unique, values can be repeated.

#########################################################################################################

# 🔹 None

# 👉 Special value that represents the absence of a value.

# 👉 Often used as a default placeholder.

# print("") → ("") indicates nothing/none.

#########################################################################################################

# 🔹 In short:

# 👉 Lists [ ] → ordered collection of items, accessed by index.
# 👉 len() → counts items.
# 👉 dict { } → key-value pairs.
# 👉 None → no value.
