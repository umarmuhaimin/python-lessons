📊 Reading & Writing CSVs (Python) – Structured Notes

########################################################################################################################

1. What is a CSV?

• CSV = Comma-Separated Values
• A simple text format for storing tabular data
• Commonly used for:
   → Data analysis
   → Data exchange
   → Spreadsheets
• Each row = one record; each column = one attribute (with headers)


2. Project Overview

• We are working with:
   → views.csv → original data
   → JPEG images (1.jpeg, 2.jpeg, …)
• Goal:
   → Read CSV data
   → Analyze images based on IDs
   → Compute brightness (0 → dark, 1 → bright)
   → Write results into a new CSV (analysis.csv)


3. Dataset Structure (views.csv)

• Columns:
   → id → numeric ID of the artwork
   → English title
   → Japanese title
• Example row:

1,The Great Wave off Kanagawa,神奈川沖浪裏

• Relationship:
   → id = 1 → corresponds to 1.jpeg
   → id = 2 → corresponds to 2.jpeg


4. Brightness Function (Given)

• calculate_brightness(filename)
   → Input: image filename ("1.jpeg")
   → Output: float from 0 to 1
   → 1.0 = white; 0.0 = black


5. Importing the CSV Library

python 🐍
import csv

• Python’s built-in CSV module
• Supports:
   → DictReader → read rows as dictionaries
   → DictWriter → write dictionaries as rows


6. Reading a CSV File

• Opening the File (Read Mode)

python 🐍
with open("views.csv", "r") as file:
    reader = csv.DictReader(file)

• Key ideas:
   → with automatically closes the file
   → "r" = read mode
   → DictReader converts each row into a dictionary


7. Iterating Through Rows

python 🐍
for row in reader:
    print(row)

• Example output:

{
 'id': '1',
 'English title': 'The Great Wave off Kanagawa',
 'Japanese title': '神奈川沖浪裏'
}

• Why DictReader is useful:
   → Column headers become dictionary keys
   → Cleaner and safer than using numeric indexes


8. Accessing Individual Columns

python 🐍
for row in reader:
    print(row["id"])

• Access values using header names:
   → row["id"]
   → row["English title"]


9. Calculating Brightness for Each Row

python 🐍
brightness = calculate_brightness(f"{row['id']}.jpeg")
print(brightness)

• Explanation:
   → row["id"] → "1"
   → Creates filename: "1.jpeg"
   → Passes filename to brightness function


10. Common Bug: Assignment vs Comparison

• ❌ Wrong:

brightness == calculate_brightness(...)

• ✅ Correct:

brightness = calculate_brightness(...)

• == compares values; = assigns values


11. Rounding Brightness Values

python 🐍
brightness = round(brightness, 2)

• Improves readability; example: 0.734928 → 0.73


12. Writing a New CSV File

• We now want to create analysis.csv.

• Opening Two Files at Once

python 🐍
with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
    ...

• views → read source CSV; analysis → write destination CSV


13. Creating a CSV DictWriter

python 🐍
reader = csv.DictReader(views)
writer = csv.DictWriter(
    analysis,
    fieldnames=reader.fieldnames + ["brightness"]
)

• Explanation:
   → reader.fieldnames = ["id", "English title", "Japanese title"]
   → Adds a new column: "brightness"


14. Writing the Header Row

python 🐍
writer.writeheader()

• Creates: id,English title,Japanese title,brightness


15. Writing Rows (Explicit Method)

python 🐍
for row in reader:
    brightness = round(calculate_brightness(f"{row['id']}.jpeg"), 2)

    writer.writerow({
        "id": row["id"],
        "English title": row["English title"],
        "Japanese title": row["Japanese title"],
        "brightness": brightness
    })

• Works, but repetitive.


16. Improved Design: Modify Existing Row

• Cleaner approach:

python 🐍
for row in reader:
    row["brightness"] = round(
        calculate_brightness(f"{row['id']}.jpeg"), 2
    )
    writer.writerow(row)

• Why better:
   → Avoids rewriting the same keys
   → Fewer lines
   → More readable
   → Less error-prone


17. Final Complete Program (views.py)

python 🐍
import csv
from brightness import calculate_brightness  # assumed import
from brightness import calculate_brightness  # assumed import


with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
    reader = csv.DictReader(views)
    writer = csv.DictWriter(
        analysis,
        fieldnames=reader.fieldnames + ["brightness"]
    )
    writer.writeheader()

    for row in reader:
        row["brightness"] = round(
            calculate_brightness(f"{row['id']}.jpeg"), 2
        )
        writer.writerow(row)


18. Validating Results

• Dark image → low brightness (~0.3)
• Bright image → high brightness (~0.7)
• Visual inspection confirms correctness


19. Key Concepts Learned

• Reading CSVs using DictReader
• Writing CSVs using DictWriter
• Handling multiple files with with
• Matching CSV data to filenames
• Data transformation + analysis
• Improving code design by reducing redundancy


20. Final Takeaways

• CSVs are ideal for structured data
• Python’s CSV module is powerful and safe
• Always prefer dictionaries over index-based access
• Clean design matters as much as correctness
• Reading + writing CSVs enables real data pipelines
