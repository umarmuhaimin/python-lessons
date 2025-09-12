# If you want to write a program that ask questions and stop the system when getting the required answer ; you can use elif conditional statement method.
# For this method, you will start with if and followed by elif until the end of boolean expression / questions.
# You will not see much difference in between if and elif statement but the one that makes it different is the representation of flowchart on the decision tree table. So, if a statement is correct ; the program will straightaway end the code.

# Case (1) :
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
elif x == y:    # == means equivalent / equal
    print("x is equal to y")