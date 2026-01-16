def main():
    history = []

    while True:
        action = input("Action: ")
        
        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        elif action == "Exit":
            print("Goodbye!")
            break
        else:
            history.append(action)
            print(history)

main()

# 🔹 Target of this project:

# → To keep track of a list of actions (History).
# → To let you undo the last action or restart (clear) all actions.
# → It’s a simple way to learn how to use lists, .append(), .pop(), and .clear() in Python.

# 👉 Starts with an empty list called history.
# → Keeps asking the user for an action.
# → If you type something (like "Jump" or "Run"), it adds that action to the history list and prints the list.
# → If you type "Undo", it removes the last action from the list and tells you what was undone.
# → If you type "Restart", it clears all actions from the list.
# → The loop keeps going forever (until you stop the program) by inputing Exit where it will break the loop.