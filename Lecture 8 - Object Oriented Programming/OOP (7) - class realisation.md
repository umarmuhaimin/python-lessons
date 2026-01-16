🤯 OOP (7) – Realization: We’ve Been Using Classes All Along

########################################################################################################################

💡 The “aha” moment

• Every built-in type you’ve touched—int, str, list, dict—is a class.  
• All those handy functions (lower, append, keys) were methods on objects of those classes.  


🔍 Seeing the classes under the hood

• int is a class with a constructor; numbers like 50 are instances of int.  
• str is a class; calling "hello".lower() was using a str method.  
• list is a class; list.append(...) is a method on a list object.  
• dict is a class; dict.keys() and friends are methods on dict objects.  


🧪 Quick checks in the console

```python
print(type(50))          # int
print(type("hello"))     # str
print(type([]))          # list
print(type(list()))      # list
print(type({}))          # dict
print(type(dict()))      # dict
```

• type(...) reveals the class of each value—proving these are objects from class blueprints.  


🧭 Summing Up (capabilities unlocked)

• Object-oriented programming  
• Classes  
• raise  
• Class Methods  
• Static Methods  
• Inheritance  
• Operator Overloading  
