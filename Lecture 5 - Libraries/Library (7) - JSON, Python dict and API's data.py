# 📚 Simplified Explanation of JSON, Python Dictionaries, and API Data

# 🔹 1. APIs usually return data in JSON format

# → JSON = JavaScript Object Notation
# → It is a standard way to send structured data over the internet.
# → It looks similar to Python dictionaries.

# 👉 Example JSON:
{
    "resultCount": 1,
    "results": [
        {
            "trackName": "Say It Ain't So",
            "artist": "Weezer"
        }
    ]
}


# 🔹 2. What requests does

# → requests fetches the JSON data from a website or API.

# 👉 Example:
# response = requests.get(url)
# data = response.json()

# → response.json() converts the JSON into a Python dictionary.


# 🔹 3. JSON → Python Dictionary Conversion

# 👉 Python automatically converts:

# → {} JSON → {} Python dictionary
# → [] JSON → [] Python list
# → JSON strings → Python strings
# → JSON numbers → Python numbers

# 👉 So something like:

# json_data =
{
    "results": [...]
}

# Becomes 

#  python_data =
{
    "results": [...]
}

# → Meaning you can now access data like: data["results"]


# 🔹 4. Why the JSON Looks Hard to Read

# → APIs return everything in one long line, which is hard to understand.

# 👉 Example raw output:

# {"resultCount":1,"results":[{"trackName":"Say It Ain't So",...}]}

# → This is why the python introduces the json library for pretty printing which is also known as json.dumps().


# 🔹 5. json.dumps() → Pretty Print JSON

# 👉 To make the API response readable:

# import json
# print(json.dumps(data, indent=2))

# → indent=2 means indent everything nicely by 2 spaces.
# → This helps you visually understand the structure of the dictionary.


# 🔹 6. Understanding the JSON Structure

# 👉 After pretty printing, you will see:

# → Main object (a dictionary)
# → resultCount → a number.
# → results → a list.
# → Inside that list → a dictionary for each song.

# 👉 Example Python structure:

data = {
    "resultCount": 1, # The API's limit from the URL parameter. If limit=1, resultCount will be 1. if limit=50, resultCount will be 50.
    "results": [
        {
            "trackName": "Say It Ain't So",
            "artist": "Weezer"
        }
    ]
}


# 🔹 7. Extracting Useful Data from JSON

# 👉 To access all songs:

for result in data["results"]: # Loop through each dictionary in the results list. Either trackName or artist can be used here.
    print(result["trackName"]) # Print the trackName dictionary only from the results list.


# 👉 This works because:

# → data["results"] = a list
# → Loop goes through each dictionary in that list
# → Each dictionary contains trackName


# 🔹 8. Changing the API Limit

# 👉 If you change:

limit=1 
# to 
limit=50

# → The API returns 50 songs instead of 1.
# → Your loop still works because it loops through the entire list:

for result in data["results"]:
    print(result["trackName"])


# 🌟 Final Super-Simple Summary

# → APIs send JSON (text data).
# → requests.get(url).json() converts it to Python dictionary.
# → JSON structure often contains:
# → objects {} → Python dict
# → lists [] → Python list
# → json.dumps(data, indent=2) makes it readable.
# → You loop through data["results"] to print each song.
# → Changing limit= in the URL changes how many results you get.


# 🔹 Itunes API's project (Display the whole API's respsonse from the results lists which contain all data about the song) :

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=weezer" + sys.argv[1])
data = response.json()
print(json.dumps(data, indent=2))


# 🔹 Itunes API's project (Display only the trackName from the results lists) :

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
data = response.json()

# We only want to display the trackName from the results lists.
for result in data["results"]: # result is a loop variable. data stores the whole API response which is basically the converted python dictionary from json format. data["results"] accesses the list of results from the API response.
    print(result["trackName"])

# Output: If run as python3 testing.py Weezer, it prints the track names of the songs by Weezer from the API response.

