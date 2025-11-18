# In this python file, we will go through if conditional statement.

# If you want to write a program that keep asking questions even though the system already got the required answers, you can use if conditional statement using either boolean expression or words.

# Boolean expression : 

# > greater
# >= greater or equal
# < lesser
# <= lesser or equal
# = assignment
# == equal to
# != not equal to

# Boolean expression : A logical statement or condition that evaluates to one of two possible outcomes: true or false.
# Boolean expression → Yes or no, True or false answer.

# Case (1) :
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x == y:    # == means equivalent / equal
    print("x is equal to y")