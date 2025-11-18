import sys
if len(sys.argv) < 2: # which means the length of sys.argv is only 1 (the program name) and no other arguments. No arguments will cause IndexError.
    print("Too few arguments. Please provide your name as a command-line argument.")
else:
    print("hello, my name is", sys.argv[1])