# We use "or conditional statement" if we have two or more option whether it is a boolean expression / words to evaluate.
# We use "or conditional statement" if two or more option does not correlate with one another.
# For example : x > y is not equal to x < y in terms of boolean expression. Therefore, we can use "or conditional statement".


# Case (1) :
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")