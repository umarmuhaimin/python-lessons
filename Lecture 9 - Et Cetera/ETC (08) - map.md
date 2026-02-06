📣 map – Structured Notes

########################################################################################################################

1. What is map? (Definition)

• map applies a function to every item in an iterable and yields the results.  
• It’s a functional-programming helper to avoid manual loops when transforming data.  

2. Baseline: yell one string

```python
def main():
    yell("This is CS50")


def yell(word):
    print(word.upper())


if __name__ == "__main__":
    main()
```
Output:
```
THIS IS CS50
```


2. Yell a list (manual loop)

```python
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
```
Output:
```
THIS IS CS50
```
• Accumulate uppercase words, then unpack with *.  


3. Yell variadic args (*words)

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
```
Output:
```
THIS IS CS50
```
• *words captures any number of arguments.  


4. Using map to apply a function

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
```
Output:
```
THIS IS CS50
```
• map takes a function and an iterable, applying the function to each element.  
• Here, str.upper is applied to every word in words.  
