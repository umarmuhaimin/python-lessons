# 🔹 Create a block function that prints block " # " vertically with respect to height.

# 👉 first method :
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):       # since _ is used, arrangement/order doesn't matter. 
        print("#")                # So it will just print the data from the range downwards starting from 1 → last number.

main()

# 👉 Second method :
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="") 


# 🔎 " #\n " means each # will be in a new line.
# 🔎 " \n " is a prompt to make a new line.
# 🔎 { end="" } means to remove Python’s default newline at the end of print output.
# 🔎 { end="" } removes the automatic newline added by print.

##########################################################################################################################################

# 🔹 Create a block function that prints block " # " horizontally with respect to width.

# 👉 first method :
def main():
    print_column(4)

def print_column(width):
    print("#" * width)            # since there is no " #\n " on the print(), program will not make a new line for each " # ".
                                  # Therefore, each " # " will be printed horizontally.
main()






