🧪 Unit Tests (Lecture 5) — Full Notes

########################################################################################################################

✅ 1. What Happens Without Unit Tests

• Before using testing tools, students typically test manually (e.g., print outputs).
• Manual testing is slow, inconsistent, error-prone, and doesn’t scale. 
• edX


✅ 2. What Are Unit Tests?

• A unit test is a small piece of code that checks one unit of our code (usually a function).
• It verifies that your function behaves as expected for specific inputs.
• Helps catch bugs early and makes refactoring safe. 
• edX


✅ 3. Using assert

• Python has a built-in statement assert which checks a condition.
• If the condition is true, nothing happens. If false, an AssertionError is raised.
• Example:

python 🐍
assert square(2) == 4

• If the test fails, you’ll see an AssertionError. 
• edX


⭐ 4. Introducing pytest

• pytest is a popular framework for running unit tests. 
• YouTube
• Install it using:

pip install pytest

• pytest automatically discovers test files and test functions:
   → File name must start with test_
   → Test functions must start with test_ 
• edX


🧩 5. Basic Calculator Example

calculator.py
python 🐍
def square(n):
    return n * n

Test file — test_calculator.py
python 🐍
from calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9

• With pytest, run:

pytest test_calculator.py

• py.test will report pass/fail and show details on failure. 
• edX


🔸 6. Splitting Test Cases

• Better practice is to separate tests into multiple functions:

python 🐍
def test_square_2():
    assert square(2) == 4


def test_square_3():
    assert square(3) == 9


def test_square_negative():
    assert square(-1) == 1

• pytest executes each test independently.
• If one fails, others still run. 
• edX


🧠 7. Testing for Errors / Exceptions

• When your code should raise an error, use pytest.raises:

python 🐍
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

• This checks that divide() raises the right exception. 
• edX


🔹 8. Testing Functions That Return Values

• If a function prints output instead of returning it, pytest cannot easily test it.
• Example (not testable):

python 🐍
def hello(name):
    print("hello,", name)

• Better style (testable):

python 🐍
def hello(name):
    return f"hello, {name}"

• Now tests for both default and argument forms:

python 🐍
def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"

• By using return instead of print, functions become testable. 
• edX


🗂 9. Organizing Tests into Folders (Good for testing)

• If you have multiple test files, you can place them in a folder:

test/
 ├── __init__.py
 ├── test_hello.py
 └── test_calculator.py

• pytest needs __init__.py so the folder is treated as a test package.
• Run all tests in the folder:

pytest test
``` :contentReference[oaicite:10]{index=10}


⚙️ 10. Categories of Tests (Lecture Video Outline)

• The video’s contents show a walkthrough over:
   → Basic asserts
   → AssertionError demonstration
   → Using pytest
   → Grouping tests
   → Testing for exceptions
   → Side effects vs return values
   → Collections of tests
• (This corresponds to the playlist’s table of contents). 
• YouTube


📌 11. Side Effects and Unit Testing

• A side effect is when a function does something other than return a value (e.g., printing, modifying global variables).
• Functions with side effects are harder to test because pytest’s assertions check return values, not printed output.
• Best practice:
   → Break code into functions that return values
   → Have a separate main program that handles printing/user I/O 
• edX


🧮 12. Example: Testing Strings (Hello)

• Before change (not testable):

python 🐍
def hello(to="world"):
    print("hello,", to)

• After change:

python 🐍
def hello(to="world"):
    return f"hello, {to}"

• test_hello.py:

python 🐍
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"

• Splitting tests into multiple functions makes failures clearer. 
• edX


✅ 13. Good Test Practices

✔ Write simple tests
✔ Test a single case per test function
✔ Use descriptive test function names
✔ Test edge cases (e.g., zero, empty string, negative values)
✔ Prefer functions that return values (so tests can check results) 
✔ edX


📊 14. Why Unit Testing Matters (Summary)

✔ Catch bugs early
✔ Simplify debugging
✔ Increase confidence in code
✔ Enable safe refactoring
✔ Serve as documentation for expected behavior
✔ Useful in teams and large codebases 
✔ YouTube


🛠 15. Running Tests With pytest

• Run all tests:

pytest

• Run a specific file:

pytest test_calculator.py

• Run tests in a folder:

pytest test/


🧩 16. Edge Cases & Return Values

• Always design functions to return values instead of printing where possible.
• Example:
   → Function prints output → can’t be tested directly.
   → Function returns a string → testable. 
• edX


🧠 17. Conclusion / Recap

• Unit tests verify individual functions.
• assert checks conditions.
• pytest is the recommended framework.
• Split tests into separate functions.
• Use exceptions testing for error cases.
• Organize tests in folders with __init__.py.
• Return values are preferable to prints for testability.
