# 🔹 Create a block function that prints block " # " vertically with respect to height.

# 👉 first method :
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):       # since _ is used, arrangement/order doesn't matter. 
        print("#")                # So it will just print the data from the range downwards starting from 1 → last number.

main()
# Output :
# → #
# → #
# → #


# 👉 Second method :
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="") 
# Output :
# → #
# → #
# → #


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
# Output :
# → ####

##########################################################################################################################################

# 🔹 Printing a Square
# → Square has the same value of height and width. In short, square has the same size of height and width.
# → In this python file, we will make rows as (height) and column as (width). BUT, in actual case : rows(width) and column(height)

# 👉 first method :
def main():
    print_square(3)

def print_square(size):
    # Outer loop → controls the rows (height)
    for i in range(size):
        # Inner loop → controls the columns in each row (width)
        for j in range(size):
            print("#", end="")   # Print a brick without moving to a new line
        print()  # Move to the next line after finishing one row

main()
# Output :
# → ###
# → ###
# → ###


# ✅ Steps (for size = 3)
# 1. Outer loop starts → i = 0 (Row 1)
#     → Inner loop: j = 0 → #
#     → Inner loop: j = 1 → #
#     → Inner loop: j = 2 → #
#     → End inner loop → print() → move to next line.
# 2. Outer loop → i = 1 (Row 2)
#     → Inner loop: j = 0 → #
#     → Inner loop: j = 1 → #
#     → Inner loop: j = 2 → #
#     → End inner loop → print() → move to next line.
# 3. Outer loop → i = 2 (Row 3)
#     → Inner loop: j = 0 → #
#     → Inner loop: j = 1 → #
#     → Inner loop: j = 2 → #
#     → End inner loop → print() → move to next line.
#     → At the end, you will still have the default python newline because of print().

# ✅ Steps inside loops :
# • Outer loop (for i in range(size)):
#     → Runs once for every row (top → bottom). {height}
#     → Example with size = 3: i = 0, 1, 2.
# • Inner loop (for j in range(size)):
#     → Runs once for every column in the current row (left → right). {width}
#     → Example with size = 3: j = 0, 1, 2.
# • Inside the inner loop → print("#", end=""):
#     → Prints # without moving to the next line.
#     → Keeps placing bricks side by side in the same row.
# • After inner loop finishes → print():
#     → Moves to a new line after the row is complete.
#     → Then the outer loop continues to the next row.

# ✅ Flow : Outer loop picks a row → Inner loop fills it with bricks → new line → repeat.
# → Code is processed from the top to the bottom. So it will go through the outer loop first, then inner loop, make a new line, and repeat.

# ✅ Definitions : 
# → print_square(size) → prints a square of # symbols with height = width = size.
# → Outer loop (for i in range(size)) → goes through each row.
# → Inner loop (for j in range(size)) → prints # across the row.
# → print("#", end="") → prints # without adding a new line.
# → print() → creates a new line after finishing a row.


# 👉 Second method :
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()
# Output :
# → ###
# → ###
# → ###

# ✅ Explaination : 
# → Outer loop runs size times (rows).
# → Each row prints "#" * size (columns).
# → Direct printing inside the loop.


# 👉 Third method :
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
    # Output :
# → ###
# → ###
# → ###

# ✅ Explaination : 
# → Outer loop still runs size times (rows).
# → Instead of printing directly, it calls print_row(size).
# → print_row(width) is just a helper function that prints the row.


# 👉 Difference between second and third method : 
# • Code style:
#     → First version is shorter (one function, direct print).
#     → Second version is cleaner / modular (separates responsibilities into functions).
# • Output: identical (prints a square of #).
# • Think of the second method as the “structured” way: if you later wanted different row designs, you just change print_row() without touching print_square().









