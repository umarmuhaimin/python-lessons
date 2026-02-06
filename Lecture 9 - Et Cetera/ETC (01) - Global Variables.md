🌐 Global Variables (and a Better Alternative) – Structured Notes

########################################################################################################################

1. What’s a global variable?

• A name defined at the top level of a module that every function can see.  
• Example:  
```python
balance = 0


def main():
    print("Balance:", balance)


if __name__ == "__main__":
    main()
```
Output:
```
Balance: 0
```


2. The problem when mutating globals

```python
balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()
```
Output (truncated):
```
Balance: 0
Traceback (most recent call last):
  ...
UnboundLocalError: local variable 'balance' referenced before assignment
```
Why this happens (plain English):
• Inside deposit/withdraw, Python sees an assignment to balance, so it assumes balance is a new local variable for that function.  
• Because it thinks balance is local, the earlier global value isn’t used, and there’s no local value yet—so it complains you’re referencing a local variable before it exists.  
• Using global balance tells Python “use the one defined at the top,” avoiding this error.  


3. Using the global keyword (works, but be careful)

```python
balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
```
Output:
```
Balance: 0
Balance: 50
```
• global tells the function to modify the module-level balance instead of making a new local.  


4. A cleaner approach: use a class

```python
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
```
Output:
```
Balance: 0
Balance: 50
```
• account = Account() holds its own balance; methods mutate that state via self.  
• Encapsulation avoids global state and UnboundLocalError headaches.  


5. Takeaway

• You can mutate globals with global, but prefer encapsulating state in classes (or other structures) for cleaner, safer code.  
