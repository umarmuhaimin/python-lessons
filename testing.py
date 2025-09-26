
def main():
    print_square(3)

def print_square(size):
    # For each brick in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        # After done with the inner loop, then it will print a new line.
        # print() indicates that it will create a new line.
        # end="" indicates no new line.
        # You can do for variable in range : i, j and k.
        print()

main()