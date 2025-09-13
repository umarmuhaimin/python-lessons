# Match Condition : We use this condition to determine which object is inside what group.
# In match condition ; we can either use match condition itself with the combination of {case and otherwise} statement, or we can use {if,elif and else} statement to represent match condition.
# Extra info : Otherwise can also be presented as case _:


# Case (1) : Match condition using {if, elif and else}
name = input("What's your name? ")
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# Case (2) : Match condition using case and otherwise (case _:)
name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Case (3) : Match condition using "|" which is equivalent to "if" or "elif" or "else" statement.
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# The symbol "|" represents if, elif and else statement.


### We use conditional statements to verify whether the statement matches the criteria of the functions ###