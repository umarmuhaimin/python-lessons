➕ OOP (6) – Operator Overloading – Structured Notes

########################################################################################################################

🧠 Plain-language view (non-CS)

• Operator overloading: teaching an operator (like +) how to work with my own objects, not just numbers.  
• Analogy: instead of adding only dollar bills, I define how to add stacks of coins (Vaults) so + knows what to do.  


✨ Why bother

• It makes code feel natural: potter + weasley sums vaults just like numbers.  
• Keeps logic inside the class, so I don’t repeat ad-hoc addition code elsewhere.  


🏦 Vault example (overloading +)

```python
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
```

• __str__ returns a readable string; lets me print vaults directly.  
• __add__ defines how to add two Vaults: self is left side of +, other is right side.  
• Returning Vault(...) ensures the result is another Vault with summed coin counts.  


🧾 Step-by-step rationale

• __init__: I default coins to 0 so Vault() is valid; parameters allow custom balances.  
• __str__: I want human-readable output for debugging and printing.  
• __add__: I want + to combine two vaults cleanly; I sum like fields and return a new Vault to preserve immutability of inputs.  
• Usage: potter + weasley looks simple, but routes through __add__ for the actual logic.  


📚 Further reading

• Python docs on operator overloading (__add__, __sub__, __eq__, etc.) cover more operators and patterns.  
