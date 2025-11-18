# 🔹 Method (1) of sending letters : 
def main():
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    ---------------------------------------------
       Dear {receiver},

       Your are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    ---------------------------------------------
    """

main()

# 🔹 Method (2) of sending letters :

# 👉 RECALL : 
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
        print(i) 

# OUTPUT :
# → 0
# → 1
# → 2
# → 3

# 👉 RECALL : 
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
        print(names[i]) 

# OUTPUT :
# → Mario
# → Luigi
# → Daisy
# → Yoshi

# 👉 Using for_loop (1) :
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
        print(write_letter(names[i], "Princess Peach"))
    

def write_letter(receiver, sender):
    return f"""
    ---------------------------------------------
       Dear {receiver},

       Your are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    ---------------------------------------------
    """

main()

# 👉 Using for_loop (2) :
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))
    

def write_letter(receiver, sender):
    return f"""
    ---------------------------------------------
       Dear {receiver},

       Your are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    ---------------------------------------------
    """

main()