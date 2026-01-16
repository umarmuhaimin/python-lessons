🧩 OOP (9) – Class Methods & Class Variables – Structured Notes

➡️ Guideline: Examples include the class definition (`class ...`) and runnable `main()` snippets so you can see how the pieces fit together.

########################################################################################################################

1. Problem Context: Food in a Video Game

• Hearts represent health; food heals hearts.  
• Goal: represent food items in Python and compute hearts healed based on ingredients.  


2. Starting Point: Food Class with Ingredients

```python
class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients
```

• Each food item has an instance variable ingredients (list passed on creation).  
• Non-CS view: each Food holds its own “shopping list”; no other Food can change it.


3. Creating an Instance of Food

```python
def main():
    mushroom_skewer = Food(["mushroom", "hearty mushroom"])

    # simple check that the instance exists
    print(mushroom_skewer.ingredients)


if __name__ == "__main__":
    main()
```

• mushroom_skewer is an instance with ingredients: "mushroom", "hearty mushroom".  
• No output yet—just confirms the code runs.  
• Why no print yet: we built the object but didn’t ask it to say anything.


4. New Requirement: Hearts Healed

• Food should heal hearts based on ingredients.  
• Options: ❌ hard-code per food; ✅ calculate from ingredients.  
• Need a function: takes ingredients, returns hearts healed.  


5. Why This Should Be a Class Method

• The calculation is the same for all food; it belongs to the class, not any single instance.  
• Perfect use case for a class method.  


6. Calling a Class Method

• Syntax: Food.calculate_hearts(ingredients) — called on the class.  


7. Defining a Class Method

• Two changes: add @classmethod and replace self with cls.  

```python
class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = 1
        for ingredient in ingredients:
            hearts += 1
        return hearts
```


8. Using the Class Method

```python
class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
```

• Why: every Food immediately figures out its healing so it’s ready for use/printing.

9. Testing the Logic

```python
def main():
    mushroom_skewer = Food(["mushroom", "hearty mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")


if __name__ == "__main__":
    main()
```

• Output: This skewer heals 3 hearts (base 1 + 1 + 1).  
• Non-CS view: start at 1 heart, add 1 per ingredient; 1 + 1 + 1 = 3.


10. Improving the Algorithm (Special Ingredients)

• Rule: ingredients containing "hearty" give 2 hearts.  

```python
@classmethod
def calculate_hearts(cls, ingredients):
    hearts = 1
    for ingredient in ingredients:
        if "hearty" in ingredient:
            hearts += 2
        else:
            hearts += 1
    return hearts
```

• Output now: 4 hearts (base 1 +1 +2).  
• Non-CS view: “hearty” is a special keyword that adds 2 hearts instead of 1.


11. Introducing Class Variables

• Base hearts = 1 applies to all food → make it a class variable.  

```python
class Food:
    base_hearts = 1
```


12. Using Class Variables in Class Methods

```python
@classmethod
def calculate_hearts(cls, ingredients):
    hearts = cls.base_hearts
    for ingredient in ingredients:
        if "hearty" in ingredient:
            hearts += 2
        else:
            hearts += 1
    return hearts
```

• Shared across all instances; easy to change globally.  
• Non-CS view: cls.base_hearts is a default knob for all Food; turn it once, everyone follows.


13. Why Class Variables Matter

• Represent shared state, avoid duplication, one source of truth, not tied to one object.  


14. Class Methods as Alternative Constructors

• Create food without ingredients; specify hearts directly.  
• Another class method: creates and returns a new instance.  


15. Creating an Alternative Constructor

```python
@classmethod
def from_nothing(cls, hearts):
    food = cls([])
    food.hearts = hearts
    return food
```

• Creates a new Food, overrides hearts, returns it.  
• Non-CS view: a shortcut to create a Food with a fixed healing value when ingredients are unknown.


16. Using the Alternative Constructor

```python
def main():
    mushroom_skewer = Food.from_nothing(2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")


if __name__ == "__main__":
    main()
```

• Output: This skewer heals 2 hearts.  
• Non-CS view: here we skipped ingredients and just set hearts to 2 directly.


17. What This Short Demonstrates

• Class Methods: belong to the class; use @classmethod; receive cls; good for shared logic, factory methods, alt constructors.  
• Class Variables: shared across instances; defined in the class body; accessed via cls.variable.  


18. Full Final Code (As Taught)

```python
class Food:
    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient:
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls([])
        food.hearts = hearts
        return food


def main():
    mushroom_skewer = Food(["mushroom", "hearty mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

    simple_food = Food.from_nothing(2)
    print(f"This skewer heals {simple_food.hearts} hearts")


if __name__ == "__main__":
    main()
```


19. Core Takeaway (CS50 Emphasis)

• Use class methods for behavior shared across all instances, and class variables for data shared across the entire class.  
• Two creation paths: with ingredients (auto-calculate) or from_nothing (set hearts directly).  
