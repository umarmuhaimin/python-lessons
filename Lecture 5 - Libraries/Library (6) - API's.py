# 📚 API's = Application Programming Interface

# ✅ Simplified Explanation of APIs

# → APIs are services created by other people or companies that your program can talk to.
# → Most APIs are on the internet, and your Python code can connect to them just like a browser does.

# 🔹 Your code:
# → connects to the API
# → asks for some data
# → downloads the data
# → and then uses it inside your own program

# In simple terms:
# → An API lets your program get information from another website automatically so that you can use it inside your own program.
# → Example: Using the requests library to access a web API.



# ✅ Simplified Explanation of the requests Library

# → Python has a very popular third-party library called requests.
# → You install it using: pip install requests

# 🔹 This library lets your Python code act like a web browser.

# 👉 It can:
# → connect to websites
# → send HTTP/HTTPS requests
# → download information from URLs
# → retrieve data automatically

# In simple terms:
# → requests lets your program access websites and APIs without you opening a browser.
# → This library is extremely popular because:
# • It is easy to use
# • It solves a very common problem (fetching data from the internet)
# • It has a large community and lots of support
# • It is part of a huge ecosystem of Python packages that make coding easier
# • This is one big reason Python is so popular— there are many ready-made libraries that already solve the problems you're going to face.


# 🔹 Itunes API's project :

import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer" + sys.argv[1])
data = response.json()
print(data)