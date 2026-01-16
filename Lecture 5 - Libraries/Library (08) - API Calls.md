📡 API Calls – Structured Notes (Art Institute of Chicago Example)

########################################################################################################################

1. What is an API?

• API (Application Programming Interface) = a way for one program to talk to another.
• Often used to access data over the internet.
• Allows your program to retrieve data without storing it locally.
• Example: Accessing museum artwork data from the Art Institute of Chicago.


2. Choosing an API

• The Art Institute of Chicago provides a public API.
• Their API allows access to artwork data in their collection.
• APIs are accessed through endpoints (specific URLs).

👉 Example endpoint:
→ /artworks/search

• Used to search artworks in the collection.


3. Setting Up the Python Program

• Create a Python file (e.g., api.py).
• Import the requests library to send HTTP requests.

```python
import requests
```

• Create a main() function and call it.


4. Making an API Request

• Use requests.get() to send an HTTP GET request.
• The base API URL (The Place where information is available to access):
→ https://api.artic.edu/api/v1

• To get into a particular route / access specific data in their collection / API :
→ GET /artworks/search

• Full request URL:
→ https://api.artic.edu/api/v1/artworks/search

👉 Example:
```python
response = requests.get("https://api.artic.edu/api/v1/artworks/search")
print(response)
```


5. Understanding the Response

• response 200 means:
  → The request succeeded.
  → The server responded correctly.

• APIs return data after acknowledging your request.


6. JSON Data from APIs

• API responses are usually returned in JSON format.
• JSON = JavaScript Object Notation.
• JSON structure:

{} → dictionary
[] → list

"key": value → key-value pairs


7. Converting JSON to Python Data

• response.json() converts JSON into a Python dictionary.

```python
content = response.json()
print(content)
```

• Python dictionaries and JSON look very similar, making them easy to work with.


8. Understanding the JSON Structure

• The API response contains keys and values.
• Important key from the documentation:
      data → a list of artworks.

• Each artwork in data is a dictionary with details.


9. Iterating Through API Data

• Since data is a list, use a loop.

```python
for artwork in content["data"]:
    print(artwork["title"])
```

• This prints the title of each artwork returned.


10. Why Documentation Matters

• API documentation tells you:
   → Which endpoints exist.
   → What keys are returned.
   → What parameters you can use.

• Without documentation, you wouldn’t know:
   → That data exists.
   → That title is a valid key.


11. Handling Errors (Best Practice)

• Internet requests can fail (no internet, server issues).
• Use exception handling to avoid crashes.

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError:
    print("Couldn't complete request")
    return
```

• response.raise_for_status():
  → Raises an error if the request failed.
  → Ensures you only continue if the response is valid.


12. Using API Parameters

• APIs often allow parameters to customize requests.
• Example parameter:
   q → search query.

👉 Example:

```python
requests.get(
    url,
    params={"q": "Monet"}
)
```

• This searches artworks related to Monet.


13. Adding User Input

• Let users control the search query.

```python
artist = input("Search the Art Institute of Chicago: ")

response = requests.get(
    url,
    params={"q": artist}
)
```


• Now the user can search for:
→ Monet
→ Picasso
→ Any artist supported by the API.


14. Final Outcome

• Your program flow:
   → Sends requests to an external server.
   → Receives structured JSON data.
   → Converts it into Python objects.
   → Displays meaningful information to the user.

• Why APIs matter here:
   → Access data that isn't stored locally.
   → Pull information that lives on other computers and networks.

15. Big Picture Takeaway

• Core idea: APIs let programs communicate across the internet.
• Python tool: requests makes HTTP calls simple.
• Data format: JSON bridges systems and Python dicts/lists.
• Success habit: Read docs to know endpoints, keys, and parameters.
• Result: APIs connect your code to powerful external data.


📡 SUMMARY 

• What you’re building:
   → Use requests to call an API over the internet.
   → Convert the response to JSON with response.json().
   → Read the JSON like a Python dictionary.
   → Loop through content["data"] (list of artworks) and print each "title".

• Extras to include:
   → Error handling: response.raise_for_status()
   → Parameters: params={"q": ...}
   → User input for the search query


✅ Full Code (CS50 Shorts Version) — api.py

```python
import requests


def main():
    # Base endpoint from the API docs
    url = "https://api.artic.edu/api/v1/artworks/search"

    # Let the user choose what to search
    artist = input("Search the Art Institute of Chicago: ").strip()

    try:
        # Make a GET request with parameters
        response = requests.get(url, params={"q": artist})

        # If status code is not 200 OK, raise an error
        response.raise_for_status()

    except requests.HTTPError:
        print("Couldn't complete request")
        return

    # Convert JSON response into a Python dictionary
    content = response.json()

    # "data" is a list of artworks (from the API docs)
    for artwork in content["data"]:
        # Each artwork is a dictionary; "title" is one of its keys
        print(f"• {artwork['title']}")


if __name__ == "__main__":
    main()
```


🔹 Key Notes (How it works)

• requests.get(url) sends an internet request (like a browser).
• response.status_code == 200 signals success; response.raise_for_status() throws if not.
• response.json() converts JSON → Python dict.
• content["data"] is a list of artwork dicts (keys → values, e.g., "title").
• artwork["title"] grabs each artwork’s title; other keys map to other fields (artist, etc.).



🔹 Optional “Pretty Print” Version (to see the JSON clearly)

Use this if the JSON looks messy and you want to inspect the structure.

```python
import requests
import json


def main():
    url = "https://api.artic.edu/api/v1/artworks/search"
    artist = input("Search the Art Institute of Chicago: ").strip()

    try:
        response = requests.get(url, params={"q": artist})
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request")
        return

    content = response.json()

    # Pretty print the whole JSON (easier to read)
    print(json.dumps(content, indent=2))


if __name__ == "__main__":
    main()
```


✅ Practice Section (Make API's Calls)

```python
import request

def main():

    print("Search the Art Institute of Chicago")
    artist = input("Artist: ")
    try:
        response = request.get("https://api.artic.edu/api/v1/artworks/search",
        {"q": "artist"}
        )
        response.raise_for_status()
    except request.HTTPError:               # Bila request, and kalau request leads to HTTP Error --> Terus Exception.
        print("Couldn't complete request")
        return


    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
```



IMPORTANT :
• data is a list of artworks.
• Each artwork is a dictionary (key–value pairs). So it has multiple key-value pairsfrom that dictionary.
• Those keys cover fields like title, artist_title, date_display, etc., depending on what the API includes.
• In this API response, each artwork dict pairs a key with its corresponding value. Example: for the key title, the value might be "Water Lilies". Other keys (like artist_title, date_display, etc.) have their own values (e.g., "Claude Monet", "1906"). So “value” just means the data stored for that key.


artwork = {
    "title": "Water Lilies",
    "artist_title": "Claude Monet",
    "date_display": "1906"
}

data = [
    {
        "title": "Water Lilies",
        "artist_title": "Claude Monet",
        "date_display": "1906"
    },
    {
        "title": "The Starry Night",
        "artist_title": "Vincent van Gogh",
        "date_display": "1889"
    },
    {
        "title": "Girl with a Pearl Earring",
        "artist_title": "Johannes Vermeer",
        "date_display": "c. 1665"
    }
]



