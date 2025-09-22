# Implement a program that asks the user for a positive integer n and then prints "meow" exactly n times.
# → Use a function get_number() that keeps prompting the user until they provide a positive integer, then returns it. → while_loop
# → Use another function meow(n) that prints "meow" n times, one per line. → for_loop
# → Call both functions inside main().

def main():
    number = get_number()  # number variable stores get_number function.
    meow(number)           # meow function will output data from number variable data.

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n               # The positive n integer that causes the loop to break because matched the condition of loop will return / stores inside number variable.
    
def meow(n):
    for _ in range(n): # Since _ is used, order does not matter. So if n is any positive integer, it will print n number of times.
        print("meow")

main()


# Meow Program Summary :
# Goal: Ask user for a positive integer n → print "meow" exactly n times.

# 🔹 Functions:

#  main()
# → Calls get_number() → stores result in number.
# → Calls meow(number) → prints "meow" n times.

# get_number() (uses while True loop)
# → Keeps asking user for n.
# → If n > 0, loop breaks.
# → Returns valid n to main().

# meow(n) (uses for loop)
# → Loops n times.
# → Prints "meow" once per iteration.
# → _ is used as a throwaway loop variable (name doesn’t matter).

# 🔹 Key Concepts:
# → while True + break → input validation loop.
# → for _ in range(n) → repeat action n times.
# → Return values → get_number() returns n, passed into meow(n).