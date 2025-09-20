# For Loops Summary : 

# ✅ What is a for loop? 
# A for loop is used to iterate (repeat) over a sequence of values.
# A for loop repeats actions for each item in a sequence (like a list, range, or string).

# For example : 
# for variable in sequence: 
    # do something : print, continue, break or etc.
    # variable can be anything either from the variable name or {i, j and k which also knows as index}.
    # This variable is a loop variable and not a list variable. They are two separate things.
    # sequence can be a list, range or strings.

#########################################################################################################

# ✅ Lists 
# A list is a data type that stores multiple values in one variable.
# A list can store multiple values like (str, int, float, bool and more) in one variable.

# fruits = ["apple", "banana", "cherry"]  # list
# for fruit in fruits:   # loop variable = fruit
#   print(fruit)

# fruits = list variable (container).
# fruit = loop variable (takes each item from fruits one at a time).
# loop variable takes each item from list variable / sequence one at a time.

### Crucial examples between loop variable with a name vs loop variable with index {i, j or k} ### 

# Example (1)
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Here the loop variable is called fruit.
# On each loop, fruit takes one element from the list one at a time :

# Loop 1 → "apple"
# Loop 2 → "banana"
# Loop 3 → "cherry"
# Output : apple, banana, cherry
# This is descriptive → the variable name tells you it’s about fruits.


# Example (2)
# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i)

# Loop 1 → "apple"
# Loop 2 → "banana"
# Loop 3 → "cherry"
# Output : apple, banana, cherry

# Works exactly the same, but now the loop variable is called i.
# On each loop, i takes one element from the list one at a time until the last data on the list "cherry" :

# ✅ Key difference :
# No difference in functionality → both do the same thing.
# Only the variable name changes.
# fruit is clearer and self-explanatory.
# i is shorter, often used when dealing with numbers or indexes.

#########################################################################################################

# ✅ Range
# Use range() when looping through numbers (especially large ones).
# range() generates a sequence of numbers (useful for big counts).
### RECALL : order/indexing starts from 0, not 1 ###

# for i in range(5):   # i goes from 0 to 4
#     print(i)
# i here is a loop variable holding each number in the sequence.


# When you write:
# for i in range(5): 
#     print(i)

# i → is just a loop variable.
# range(5) is the sequence → it generates 5 numbers starting from zero : 0, 1, 2, 3, 4.

# On each iteration (repetition of loops), i takes the next value from range(5) from i = 0 to i = 4 {until the loop ends}.
# So step by step:
# 1st loop → i = 0
# 2nd loop → i = 1
# 3rd loop → i = 2
# 4th loop → i = 3
# 5th loop → i = 4
# After that, the loop ends.

# i (index) is just a loop variable name. You could replace it with anything: 
# for example :
# for number in range(5):
#     print(number)

# The loop variable which is "number" will take each item from range(5) one at a time starting from number = 0 until the loop ends.
# 1st loop → number = 0
# 2nd loop → number = 1
# 3rd loop → number = 2
# 4th loop → number = 3
# 5th loop → number = 4
# Loop ends.

### Both i and number works the same as a loop variable, its just the name that is different ###

#########################################################################################################

# ✅ Special Cases

# 👉  _ underscore : 
# It is used when the loop variable isn’t needed. 
# Loop variable is crucial to store data from a sequence where arrangement/order matters.
# Therefore, the underscore _ in a for loop is just a variable name that doesn't prioritise orders and arrangements. Its function is just for the loop to repeat the assignment until all sequence is printed/outputed.
# Use underscore _ in a for loop when you don't need to store any data and data arrangements/orders does not matter. Basically, if you want to output anything that doesn't require any lists of data.
# Simple explaination : “I don’t care about the value/arrangement/order of the element, I just want the loop to repeat untill all sequence are outputed.”

# Example 1 : {with underscore_} using for loops without storing any data.
# for _ in range(3):
#     print("Hello")

# Output : Hello, Hello, Hello {downwards}.
# We don’t need the numbers 0, 1, 2 from range(3), so we use _ instead of i.

# Example 2 : {with loop variable} using for loops and storing data.
# for i in range(3):
#     print("Hello", i)

# This prints: Hello [0], Hello [1], Hello [2] downwards.
# Using loop variable results in : first loop [0], second loop [1] and third loop [2]. - The end of the loop -

# i is the loop variable. It takes values from the iterator/sequence of range(3) → 0, 1, 2
# The arrangement/order matters in this case, because i changes step by step in sequence.
# Therefore, loop variable matters arrangement/order because the loop processes values one at a time, in order.
# In summary, we use i/loop variable because we want the element to have numbers witb orders/arrangements for storing data purposes.


# Use underscore _ when you are not storing any data using for loops.
# Use loop variable using either i (index) or any loop variable name to store data using for loops.


# Simplified Example :
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Output : apple [0], banana [1], cherry [2]
# In terms of index :
# fruits[0] → "apple"
# fruits[1] → "banana"
# fruits[2] → "cherry"
### This is called zero-based indexing ###

# fruit is the loop variable.
# It stores "apple", then "banana", then "cherry" from the lists/sequence.
# Order matters → the loop always follows the list’s order ; one step at a time.


# 👉 continue : 
# Skips the current iteration of the loop.
# Moves to the next item in the loop.
# We use continue to skip an iteration/loop, and continue to output the remaining item in the sequence.
# In short : we use continue to skip a round, and keep looping.

# Example:

# for i in range(5): 
#     if i == 2:
#         continue
#     print(i)   

# Output: 0, 1, 3, 4

# We have 5 orders/index, starting from [0,1,2,3 and 4].
# If i == 2 from the index/order which is on the third loop/iteration, it will skip the 3rd loop and moves onto the next item "the 4th loop and so on".
# It will skip printing 2 and continue to print the remaining item in the loop which are 3 and 4.


# 👉 break :
# Immediately stops the loop.
# No further iterations are executed.
# In short : break stops the loop entirely.

# Example:
# for i in range(5):
#     if i == 2:
#         break   # stop loop completely
#     print(i)

# Output: 0, 1

# We have 5 orders/index, starting from [0,1,2,3 and 4].
# If i == 2 from the index/order which is on the third loop/iteration, break will stop the loop immediately.
# i == 2 will not be included in the output because that is the loop where break takes place.
# Therefore only the first 2 order will be outputed which is : [0 and 1] only.
# Inequality signs matters.



