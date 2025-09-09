def get_guess():
    guess = str(input("Enter a guess:")) # The variable guess here is only applicable for this function.
    return guess

def main():
    guess = get_guess() # The variable guess here is only applicable for this function.
    if guess == "fifty":
        print("Correct")
    else:
        print("Incorrect")

main()
