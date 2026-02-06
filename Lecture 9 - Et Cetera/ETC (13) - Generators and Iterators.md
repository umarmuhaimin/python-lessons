🚰 Generators & Iterators – Structured Notes

########################################################################################################################

1. Why generators? (Definition)

• A generator yields items one at a time, on demand, instead of building a whole list.  
• Saves memory and avoids slowdowns when dealing with large or infinite sequences.  


2. Baseline: build everything (risk of big lists)

```python
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    main()
```
• Prints a growing number of sheep strings; fine for small n.  


3. With helper function returning a list

```python
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
```
Output (n=4):
```
🐑
🐑🐑
🐑🐑🐑
🐑🐑🐑🐑
```
• Builds a list (flock) first—can blow up memory for huge n (e.g., 1,000,000).  


4. Convert to a generator with yield

```python
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
```
Output (n=4):
```
🐑
🐑🐑
🐑🐑🐑
🐑🐑🐑🐑
```
• yield produces one string at a time; nothing huge is stored in memory.  


5. Iterators (concept link)

• A generator is also an iterator: it implements “get next item” semantics.  
• Any object that supports iteration protocols (like generators) works in for-loops.  


6. Takeaway

• Use yield when producing sequences that could get large—stream them instead of storing them.  
• Generators keep code simple and memory-friendly while remaining iterable.  
