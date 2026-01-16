🎨 Style in Python (PEP 8 & Formatters) – Structured Notes

########################################################################################################################

1. What Is “Style” in Programming?

• Style = how your code looks, not just whether it works.
• Code can be correct and well-designed but poorly styled.
• Poor style makes code hard to read, hard to maintain, and bug-prone.


2. Why Style Matters

• Code is read far more than it’s written.
• Others (and future you) need to understand it.
• Like essays: clear spacing, structure, consistency → fewer bugs.


3. PEP 8 (Python Enhancement Proposal 8)

• PEP = Python Enhancement Proposal; PEP 8 is the official style guide.
• Purpose: standardized, consistent Python code.
• Core idea: “Readability counts.”


4. Style Guides & Consistency

• Style guides are guidelines, not strict laws.
• Consistency layers:
   → With PEP 8.
   → Within a project.
   → Within a file/function (most important).


5. Key PEP 8 Rules to Know

🔹 Indentation
• 4 spaces per level; no tabs (editors usually convert tabs → spaces).

🔹 Line Length
• Aim for ~79 characters; avoid lines running off the screen.

🔹 Blank Lines & Whitespace
• Separate functions/sections; avoid “walls of code.”

🔹 Imports
• At the top; grouped logically; follow ordering/spacing conventions.


6. Style Is Learned Through Practice

• You don’t memorize PEP 8 line by line.
• You pick it up by reading good code and writing more Python.
• Over time, good style becomes natural.


7. Tools That Check Style (Linters & Formatters)

🔹 Linters
• Analyze code without running it; flag style issues, possible bugs, bad practices.
• Example: pylint (powerful but chatty for beginners).


8. Automatic Code Formatters

🔹 pycodestyle
• Formerly pep8; checks against PEP 8; can auto-fix formatting.

🔹 black (recommended)
• Opinionated formatter; makes decisions for you; no style debates.
• Philosophy: “Any color you want, as long as it’s black.”
• Lets you focus on correctness, design, and problem solving.


9. Example: Formatting with black

❌ Before (poor style)
python 🐍
students={"Harry":"Gryffindor","Hermione":"Gryffindor","Ron":"Gryffindor","Padma":"Ravenclaw"}
for student in students:
 print(student)

✅ After running black students.py
python 🐍
students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Padma": "Ravenclaw",
}

for student in students:
    print(student)

• Fixes: clean indentation, one pair per line, trailing comma, readable layout.


10. Trailing Commas (Why They’re OK)

• Trailing comma after the last item is valid.
• Easier to add items later; fewer syntax errors.
• black adds them intentionally.


11. Big Takeaways

• Style ≠ correctness, but both matter.
• PEP 8 standardizes style; readability reduces bugs.
• Tools like black automate formatting—don’t fight them.
• Let formatters handle style so you can focus on logic.


12. Final Advice from CS50

• Learn PEP 8 gradually.
• Use formatters early.
• Write readable code.
• Let automation handle the boring details.
