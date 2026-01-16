🧪 pytest (Complete & Structured Notes)

########################################################################################################################

1. What Is pytest?

• pytest is a Python module used for automated testing.
• It allows you to test your code more thoroughly than manual testing.
• It replaces repeatedly:
   → Running a program
   → Entering inputs
   → Checking outputs by hand
• pytest automates this process using code that tests code.


2. Example Program: convert.py

• Purpose: convert astronomical units (AU) into meters.
• 1 AU ≈ 149,597,870,700 meters.

👉 convert.py (from the lecture)
```python
def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700
```


3. Why Manual Testing Is Not Enough

• Manual testing example:

```
python convert.py
```

• Enter values like 1; visually check output; repeat for different values.

• Problems:
   → Slow
   → Error-prone
   → Not scalable
   → Easy to miss edge cases

👉 This is why pytest exists.


4. pytest Naming Conventions

• pytest discovers tests automatically if:
   → Test files start with: test_
   → Test functions start with: test_

• Example test file: test_convert.py


5. Creating the Test File

👉 test_convert.py
```python
import pytest
from convert import convert

# pytest must be imported
# Import the function under test (convert)
# Tests are written as functions


6. First Unit Test: Integer Conversion

• Testing 1 AU
def test_conversion():
    assert convert(1) == 149597870700

• Explanation:
   → assert checks if the condition is true
   → If false → pytest reports failure
   → If true → test passes silently


7. Running pytest

• Run in terminal:

pytest

• Output:
   → A . means the test passed
   → 1 passed means the test function succeeded


8. Adding More Assertions (Still One Test Function)

```python
def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000
```

• Important:
   → pytest counts test functions, not assertions
   → All assertions must pass for the test to pass


9. Testing for Errors (Exceptions)

• Why? convert() raises a TypeError if input is invalid; we must test that behavior too.

👉 Testing TypeError with pytest.raises
```python
def test_error():
    with pytest.raises(TypeError):
        convert("1")
```

• Explanation:
   → pytest.raises(TypeError) expects a TypeError
   → If the error is raised → test passes
   → If not → test fails


10. Testing Floating-Point Values

• Problem: floating-point precision; floats cannot always be represented exactly; comparing floats directly is unreliable.

👉 Example Float Test (Without Tolerance)
```python
def test_float_conversion():
    assert convert(0.001) == 149597870.691
```

• ⚠️ This may fail due to precision issues.


11. Using pytest.approx (Correct Approach)

```python
def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691)
```

• pytest.approx() allows small differences; uses sensible default tolerance.


12. Custom Tolerance with abs

```python
def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
```

• Meaning: accepts values within ±0.1; useful when exact precision is not required.


13. Tightening the Tolerance

• Example (too strict):

pytest.approx(149597870.691, abs=1e-5)

• Result: ❌ Test fails; returned value is outside tolerance.

• Adjusting Tolerance

pytest.approx(149597870.691, abs=1e-2)

• Test passes; demonstrates how tolerance affects correctness.


14. Important Lesson on Tolerance

• ❌ Do not loosen tolerance just to make tests pass.
• ✅ Decide acceptable tolerance first; then fix code if it fails.
• Especially critical in scientific applications.


15. Final test_convert.py (Lecture-Complete)

```python
import pytest
from convert import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    with pytest.raises(TypeError):
        convert("1")


def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
```


16. Features of pytest Demonstrated

• assert for correctness
• Multiple assertions
• Testing exceptions
• Testing floats with tolerance
• Automated test discovery
