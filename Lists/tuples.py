# 📘 Tuples – Key Learning Points

# 🔹 Definition:
# → A tuple is an ordered, immutable collection of items — similar to a list, but cannot be changed after creation.

# 👉 Syntax:
# → Use parentheses ( ) instead of square brackets [ ].
#   numbers = (1, 2, 3)

# 👉 Immutability:
# → Once a tuple is created, the elements cannot be modified, added, or removed.
#   numbers[0] = 5   # ❌ Error – tuples are immutable

# 👉 Indexing & Access:
# → You can access items using index positions, just like lists.
#   print(numbers[1])   # Output: 2

# 👉 Iteration:
# → You can use a for loop to go through all elements.
#   for n in numbers:
#       print(n)

# 👉 Single-item tuple:
# → Must include a comma — otherwise Python treats it as a normal value.
x = (5,)   # ✅ tuple
y = (5)    # ❌ just an integer

# 👉 Tuple unpacking:
# → You can assign values to multiple variables in one line.
coordinates = (10, 20)
x, y = coordinates
print(x)  # 10
print(y)  # 20

# 👉 Useful when:
# → You need fixed data that should not be changed.
# → You want faster performance (tuples are slightly faster than lists).
# → You want to use them as keys in dictionaries (lists can’t be keys).

# 👉 Conversion:
# → You can convert between tuples and lists.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)