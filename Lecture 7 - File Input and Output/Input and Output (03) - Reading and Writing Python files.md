📖 Reading & Writing Files (Python) – Structured Notes

########################################################################################################################

1. Goal of the Short

• Learn how to:
   → Open files in Python
   → Read file contents
   → Extract specific parts of a file
   → Write data to a new file
• Example project:
   → Read Alice’s Adventures in Wonderland
   → Extract Chapter 1
   → Save it into a new file


2. The Source File (Alice.txt)

• Contains the full text of the book
• Observations:
   → Chapter 1 starts at line 53
   → Chapter 2 starts around line 272
• Goal: Extract only the text for Chapter 1


3. Opening Files in Python

• Python uses:
   → open() → opens a file
   → with → context manager (automatically closes file)

• Basic Syntax

```python
with open("Alice.txt", "r") as f:
    ...
```

• Key ideas:
   → "Alice.txt" → file name
   → "r" → read mode
   → f → variable referring to the open file
   → File closes automatically when indentation ends


4. File Modes

• Common modes:
   → "r" → read (default)
   → "w" → write (overwrites file)
   → "a" → append (adds to file)
• In this short: first → read mode; later → write mode


5. Reading an Entire File (read)

```python
with open("Alice.txt", "r") as f:
    contents = f.read()
    print(contents)
```

• What happens:
   → Reads entire file at once
   → Stores everything as one large string
• Useful for small files; not ideal when you need structure (chapters, lines)


6. Reading Line by Line (readlines)

```python
with open("Alice.txt", "r") as f:
    contents = f.readlines()
```

• What readlines() returns:
   → A list of strings
   → Each item = one line from the file

• Example:
   → contents[0]   # first line
   → contents[1]   # second line

• Why this is useful: lets you access specific lines, slice sections, extract chapters


7. Understanding Indexing

• Files show line numbers starting at 1
• Python lists use 0-based indexing
• Example:
   → Line 53 in file → index 52 in list
   → Line 272 in file → index 271


8. Extracting Chapter 1 Using List Slicing

```python
chapter1 = contents[52:272]
```

• Explanation:
   → 52 → start of Chapter 1
   → 272 → start of Chapter 2 (not included)
• Result: chapter1 is a list of strings; each string is one line of Chapter 1


9. Writing to a New File

• To create a new file:

```python
with open("chapter1.txt", "w") as f:
    ...
```

• Key points:
   → "w" → write mode
   → File is created if it doesn’t exist
   → Existing file is overwritten


10. Writing a Single String (write)

```python
with open("chapter1.txt", "w") as f:
    f.write("Chapter 1")
```

• write() writes one string; does not automatically add a newline


11. Writing Multiple Lines (writelines)

• Since chapter1 is a list of strings, we use:

```python
with open("chapter1.txt", "w") as f:
    f.writelines(chapter1)
```

• What this does:
   → Writes each string in the list
   → Preserves original line breaks
   → Perfect for writing extracted chapters


12. Full Example Program (book.py)

```python
with open("Alice.txt", "r") as f:
    contents = f.readlines()

chapter1 = contents[52:272]

with open("chapter1.txt", "w") as f:
    f.writelines(chapter1)
```


13. Why with Is Important

• Using with:
   → Automatically closes files
   → Prevents file corruption
   → Avoids forgetting close()
   → Cleaner and safer code


14. Context Managers Explained

• This is safe:

```python
with open("file.txt") as f:
    ...
```

• This is riskier:

```python
f = open("file.txt")
...
f.close()
```

• Reason: with guarantees cleanup even if errors occur


15. Key Takeaways

• open() prepares a file
• read() → entire file as one string
• readlines() → file as a list of lines
• Lists allow slicing for extraction
• write() → write a single string
• writelines() → write a list of strings
