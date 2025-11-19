# 📚 Command-Line Arguments (sys.argv)

# → Command-line arguments allow users to provide input to a program when executing it from the command line.
# → In Python, the sys module provides access to command-line arguments via sys.argv.

# → sys is the module and argv is the variable that holds the list of arguments.
# → sys.argv is a list.
# → sys.argv[0] is the program name.
# → sys.argv[1] is the first argument, sys.argv[2] the second, and so on.

# 🔹 Important note :
# → sys.argv[0] = name of the program / filename (testing.py) --> index[0]
# → sys.argv[1] = first argument (e.g., Alice) --> index [1]

# → You must check the list length to avoid IndexError.

# ✅ Example :

# 👉 sys.argv[1]
import sys
print("hello, my name is", sys.argv[1])

# Output: If run as python3 testing.py Alice, it prints "hello, my name is Alice".


# 👉 sys.argv[0]
import sys
print("hello, my name is", sys.argv[0])

# Output: If run as python3 testing.py, it prints "hello, my name is filename.py/testing.py"
# Both filename.py and testing.py is the name of the program.


# 👉 sys.argv[1]
import sys
print("hello, my name is", sys.argv[1])

# Output: If run as python3 testing.py, without any argument : it prints "IndexError: list index out of range" because sys.argv[1] does not exist.


# 👉 To handle sys.argv[] error because of no arguments on the command line, we can use exception so that it will be user friendly.

import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments. Please provide your name as a command-line argument.")


# 👉 Smarter way to handle the IndexError problem using if, elif and else statement :

import sys
if len(sys.argv) < 2: # which means the length of sys.argv is only 1 (the program name) and no other arguments. No arguments will cause IndexError.
    print("Too few arguments. Please provide your name as a command-line argument.")
elif len(sys.argv) > 2: # which means the length of sys.argv is greater than 2 (the program name, 1st, 2nd and so on argument). This causes too many arguments problem.
    print("Too many arguments. Please provide only your name as a command-line argument.")
else:
    print("hello, my name is", sys.argv[1])

# Output:
# If run as python3 testing.py Alice, it prints "hello, my name is Alice".
# If run as python3 testing.py, it prints "Too few arguments. Please provide your name as a command-line argument."
# If run as python3 testing.py Alice Bob, it prints "Too many arguments. Please provide only your name as a command-line argument."
# If run as python3 testing.py "David Malan", it prints "hello, my name is David Malan".

# Note: To provide a name with spaces as a single argument, enclose it in quotes


# 👉 Using sys.exit as a replacement to print().
# → sys.exit() can be used to terminate the program early.
# → Since user provide either too few or too many arguments, we can terminate the program using sys.exit().
# → There's nothing more to do if the user's input is invalid, so might as well exit.

import sys
if len(sys.argv) < 2: # which means the length of sys.argv is only 1 (the program name) and no other arguments. No arguments will cause IndexError.
    sys.exit("Too few arguments. Please provide your name as a command-line argument.")
elif len(sys.argv) > 2: # which means the length of sys.argv is greater than 2 (the program name, 1st, 2nd and so on argument). This causes too many arguments problem.
    sys.exit("Too many arguments. Please provide only your name as a command-line argument.")
else:
    print("hello, my name is", sys.argv[1])

# Output:
# If run as python3 testing.py Alice, it prints "hello, my name is Alice".
# If run as python3 testing.py, it prints "Too few arguments. Please provide your name as a command-line argument." and exits.
# If run as python3 testing.py Alice Bob, it prints "Too many arguments. Please provide only your name as a command-line argument." and exits.
# If run as python3 testing.py "David Malan", it prints "hello, my name is David Malan".


# 👉 Using for loop to print all command-line arguments (can accept many argument) provided by the user without the program name :

import sys
if len(sys.argv) < 2: # which means the length of sys.argv is only 1 (the program name) and no other arguments. No arguments will cause IndexError.
    sys.exit("Too few arguments. Please provide your name as a command-line argument.")
for arg in sys.argv[1:]:  # start from index 1 to skip the program name at index 0.
    print("hello, my name is", arg)

# Output:
# If run as python3 testing.py Alice Bob Charlie, it prints:
# hello, my name is Alice
# hello, my name is Bob
# hello, my name is Charlie
# If run as python3 testing.py, it prints "Too few arguments. Please provide your name as a command-line argument." and exits.
    
    
    
    
