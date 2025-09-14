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


    

    

    

    


    
        
