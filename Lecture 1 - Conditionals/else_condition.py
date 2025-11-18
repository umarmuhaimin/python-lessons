# If you want to write a program using conditional statement with the most simplified flowchart, you can use else statement.
# else statement : if the system meets the true value, it will end the code. If the system does not meet the true value, then it will assume the return value is false / will output us a response that does not meet the main condition.
# In order to use the else statement : you need to include either if / elif statement at the beginning of the code / program.
# RECALL : in order to use elif statement, you need to have if statement first.


# Case (1) :
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# RECALL these steps : if, then (":"), else.
# 1. if statement: / elif statement:
# 2. else statement:


# Case (2) : Not equal to "!="
x = int(input("What's x? "))
y = int(input("What's y? "))

if x !=y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# Case (3) : Equal to "=="
x = int(input("What's x? "))
y = int(input("What's y? "))

if x ==y: 
    print("x is equal to y")
else:
    print("x is not equal to y")

