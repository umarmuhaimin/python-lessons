### Python Lists Cheat Sheet (Methods) ###

#########################################################################################################

# 🔹 Adding Items

fruits = ["apple", "banana"]

# 👉 list.append(item) → Adds item to the end of the list.
#     → fruits.append("cherry")
#     → print(fruits)  # ["apple", "banana", "cherry"]

# 👉 list.insert(index, item) → Inserts item at a specific position.
#     → fruits.insert(1, "orange")
#     → print(fruits)  # ["apple", "orange", "banana", "cherry"]

# 👉 list.extend(other_list) → Adds multiple items from another list.
#     → fruits.extend(["mango", "grape"])
#     → print(fruits)  # ["apple", "orange", "banana", "cherry", "mango", "grape"]

#########################################################################################################

# 🔹 Removing Items

fruits = ["apple", "banana"]

# 👉 list.remove(item) → Removes the first matching item.
#     → fruits.remove("banana")
#     → print(fruits)

# 👉 list.pop(index) → Removes item at index (default = last item).
#     → fruits.pop()      # removes last
#     → fruits.pop(1)     # removes item at index 1
#     → () means default. default = last item

# 👉 list.clear() → Removes all items.
#     → fruits.clear()
#     → print(fruits)  # []

#########################################################################################################

# 🔹 Searching & Counting

nums = [1, 2, 3, 2]

# 👉 list.index(item) → Returns the index of first occurrence.
#     → print(nums.index(2))  # 1
# Even though there are two 2s, .index() only gives the first one it finds.

# 👉 If you want all the positions of an item, you’d need a loop:
#     → nums = [10, 20, 30, 20, 40]
#     → for i in range(len(nums)):
#     →     if nums[i] == 20:
#     →         print(i)
# Output: 1, 3 → Postion index [1] and Position index [3]

# 👉 list.count(item) → Counts how many times an item appears.
#     → print(nums.count(2))  # 2

#########################################################################################################

# 🔹 Sorting & Reversing

nums = [3, 1, 4, 2]

# 👉 list.sort() → Sorts list in ascending order (numbers or alphabet).
#     → nums.sort()
#     → print(nums)  # [1, 2, 3, 4]


# 👉 list.sort(reverse=True) → Sort in descending order.
#     → nums.sort(reverse=True)
#     → print(nums)  # [4, 3, 2, 1]


# 👉 list.reverse() → Reverses the list (not sorted).
#     → fruits = ["apple", "banana", "cherry"]
#     → fruits.reverse()
#     → print(fruits)  # ["cherry", "banana", "apple"]

#########################################################################################################

# 🔹 Copying

# 👉 list.copy() → Creates a shallow copy of the list.
#     → new_fruits = fruits.copy()

#########################################################################################################

# 🔹 Tip: Lists are mutable → they can be changed after creation.

#########################################################################################################

# 🔎 Why use .index()?

# 👉 To locate something quickly in a list. In short, index() tells you the position of a value/item in the list.

# 👉 Example: 
#     → if you have 100 students and you want to know where "Hermione" is in the list, .index() gives you her position.

students = ["Harry", "Ron", "Hermione", "Draco"]
#     → print(students.index("Hermione"))
# Output : 2 → Position index [2]
# "Hermione" is in the 3rd place in the list (remember, Python starts counting at 0)

#########################################################################################################

# 🔹 how to safely check if an item is in a list before using .index()?

# 👉 Method 1: Using "in"
nums = [10, 20, 30, 40]

#     → if 20 in nums:
#     →     print(nums.index(20))  # ✅ Safe to use
#     → else:
#     →     print("20 not found")
# Output : 1

# 👉 Method 2: Try–Except (handles errors) [ADVANCED METHOD]
nums = [10, 20, 30, 40]

#     → try:
#     →     print(nums.index(50))  # 50 is not in the list
#     → except ValueError:
#     →     print("50 not found")
# Output : 50 not found

# ✅ Summary:

# Use in → quick check if item exists.
# Use try/except → handle error if item might not exist.

# 👉 To quick check if item exist → use "in"
# 👉 To check whether item might not exist → use "try/except"

#########################################################################################################

# 🔹 Here’s the practical breakdown for big projects in VS Code:

# 👉 Main code place (.py files):
#     → Where your main program lives.
#     → You’ll always keep your list logic, functions, classes, etc. here.
#     → Example: students.py has students = ["Harry", "Ron", "Hermione"].

# 👉 VS Code terminal (or Python shell):
#     → Perfect for quick testing / debugging when the project is big.
#     → If you’re not sure what’s inside students or want to test .index(), .append(), etc., you can:
#       1. Run your file (python students.py)
#       2. Or open a Python interactive shell in VS Code’s terminal and type:

#       >>> students = ["Harry", "Ron", "Hermione"]
#       >>> students.append("Draco")
#       >>> students
#       ['Harry', 'Ron', 'Hermione', 'Draco']

# 👉 So yes — in practical coding, if the project is too big and you don’t want to scroll through files or trace variables, you can use the terminal/interactive shell to test updates on lists (or any variable) without breaking your main code.


