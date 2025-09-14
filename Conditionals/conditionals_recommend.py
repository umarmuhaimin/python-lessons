# In this python file, we will learn how to recommend games to users using conditional statement.

# Option 1 : 

def main():
    difficulty = input("Difficult or Casual?")
    players = input("Single-player or Multiplayer?")

    if difficulty == "Difficult":
        if players == "Single-player":
            recommend("Elden Ring")
        elif players == "Multiplayer":
            recommend("Sea of Theives")
        else:
            print("Enter a valid number of player")

    elif difficulty == "Medium":
         if players == "Single-player":
            recommend("Minecraft")
         elif players == "Multiplayer":
            recommend("Rocket League")
         else:
            print("Enter a valid number of player")

    elif difficulty == "Casual":
         if players == "Single-player":
            recommend("Pokemon Dash")
         elif players == "Multiplayer":
            recommend("Clash Royale")
         else:
            print("Enter a valid number of player")

    else:
        print("Enter a valid difficulty!")

def recommend(game):
     print(f"We recommend: {game}")

main()


# Option 2 : Simplified

def main():
    difficulty = input("Difficult or Casual?")
    if not (difficulty == "Difficult" or difficulty == "Medium" or difficulty == "Casual"):  # We do this step to simplify the system / code. No need to add command on each conditional statement {especially for "else"} from the user's input that does not meet the criteria of the system.
        print("Enter a valid difficulty!")
    players = input("Single-player or Multiplayer?")
    if not (players == "Single-player" or players == "Multiplayer"):  # We do this step to simplify the system / code. No need to add command on each conditional statement {especially for "else"} from the user's input that does not meet the criteria of the system.
        print("Enter a valid number of player")

    if difficulty == "Difficult" and players == "Single-player":
            recommend("Elden Ring")
    elif difficulty == "Difficult" and players == "Multiplayer":
            recommend("Sea of Theives")
            

    if difficulty == "Medium" and players == "Single-player":
            recommend("Minecraft")
    elif difficulty == "Medium" and players == "Multiplayer":
            recommend("Rocket League")

    if difficulty == "Casual" and players == "Single-player":
            recommend("Pokemon Dash")
    elif difficulty == "Casual" and players == "Multiplayer":
            recommend("Clash Royale")

        
def recommend(game):
     print(f"We recommend: {game}") # With f-string, you need to use curly braces and all command are inside one "".

main()


# Option 3 : Most Simplified

def main():
    difficulty = input("Difficult or Casual?")
    if not (difficulty == "Difficult" or difficulty == "Medium" or difficulty == "Casual"):
        print("Enter a valid difficulty!")
    players = input("Single-player or Multiplayer?")
    if not (players == "Single-player" or players == "Multiplayer"):
        print("Enter a valid number of player")

    if difficulty == "Difficult" and players == "Single-player":
            recommend("Elden Ring")
    elif difficulty == "Difficult" and players == "Multiplayer":
            recommend("Sea of Theives")
    elif difficulty == "Medium" and players == "Single-player":
            recommend("Minecraft")
    elif difficulty == "Medium" and players == "Multiplayer":
            recommend("Rocket League")
    elif difficulty == "Casual" and players == "Single-player":
            recommend("Pokemon Dash")
    else:   # No need to mention Multiplayer section with casual difficulty because you can just simplify it with "else" conditional statement since it is the last option / answer.
        recommend("Clash Royale")


def recommend(game): 
     print("We recommend: ", game)  # Without f-string, you can use comma.

main()
    

    

    

    


    
        
