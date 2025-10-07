# 🔹 Error 1 : Printing pyramid with height of n. In the case of height = 3.
# 👉 Actual Answer :
# → #    [0]
# → ##   [1]
# → ###  [2]

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

main()

# Output : 
# →     [0]
# → #   [1]
# → ##  [2]

# 👉 Solution : 
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * ( i + 1 ))

main()

# Output :
# → #    [0]
# → ##   [1]
# → ###  [2
