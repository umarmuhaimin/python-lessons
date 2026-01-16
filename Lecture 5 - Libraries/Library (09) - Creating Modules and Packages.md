📦 Creating Modules & Packages – Structured Notes

########################################################################################################################

✅ Goal

• Move reusable functions out of one big file.
• Put them into modules (separate .py files).
• Group related modules into a package (folder with __init__.py).


1. Starting Point: Everything in one file (search.py)

👉 search.py (original: function inside same file)

python 🐍
import requests


def get_artworks(query, limit):
    url = "https://api.artic.edu/api/v1/artworks/search"
    response = requests.get(url, params={"q": query, "limit": limit})
    response.raise_for_status()
    content = response.json()
    return content["data"]


def main():
    query = input("Search artworks: ").strip()
    results = get_artworks(query, 3)

    for artwork in results:
        print(f"• {artwork['title']}")


if __name__ == "__main__":
    main()

• Works, but get_artworks() is stuck in this file only.


2. Creating a Module (move function into its own file)

• Create a new file: artwork.py

👉 artwork.py (module)

python 🐍
import requests


def get_artworks(query, limit):
    url = "https://api.artic.edu/api/v1/artworks/search"
    response = requests.get(url, params={"q": query, "limit": limit})
    response.raise_for_status()
    content = response.json()
    return content["data"]

• Update search.py to import from the module.

👉 search.py (using the module)

python 🐍
from artwork import get_artworks


def main():
    query = input("Search artworks: ").strip()
    results = get_artworks(query, 3)

    for artwork in results:
        print(f"• {artwork['title']}")


if __name__ == "__main__":
    main()

• Now get_artworks() is reusable in other files.


3. Adding Another Module (artists)

• Create: artists.py (different endpoint: artists/search).

👉 artists.py

python 🐍
import requests


def get_artists(query, limit):
    url = "https://api.artic.edu/api/v1/artists/search"
    response = requests.get(url, params={"q": query, "limit": limit})
    response.raise_for_status()
    content = response.json()
    return content["data"]

• Update search.py to use both modules.

👉 search.py (artworks + artists)

python 🐍
from artwork import get_artworks
from artists import get_artists


def main():
    artist_query = input("Search artists: ").strip()
    artists = get_artists(artist_query, 3)

    for artist in artists:
        print(f"• {artist['title']}")

    artwork_query = input("Search artworks: ").strip()
    artworks = get_artworks(artwork_query, 3)

    for artwork in artworks:
        print(f"• {artwork['title']}")


if __name__ == "__main__":
    main()


4. Alternative Import Style (and why it can fail)

👉 Using import module

python 🐍
import artists
import artwork


def main():
    query = input("Search: ")
    results = artwork.get_artworks(query, 3)

    for r in results:
        print(r["title"])


⚠️ Watch out: if you name a variable artists, you shadow the module.

Example (bad):

python 🐍
artists = input("Search artists: ")   # now artists is a string, not the module


5. Creating a Package (group modules into a folder)

• Target folder structure:

search.py
museum/
    __init__.py
    artwork.py
    artists.py

• museum/__init__.py can be empty; it marks museum as a package.
• Move artwork.py → museum/artwork.py
• Move artists.py → museum/artists.py

• Update imports in search.py to use the package.

👉 search.py (import from package)

python 🐍
from museum.artwork import get_artworks
from museum.artists import get_artists


def main():
    artist_query = input("Search artists: ").strip()
    artists = get_artists(artist_query, 3)

    for artist in artists:
        print(f"• {artist['title']}")

    artwork_query = input("Search artworks: ").strip()
    artworks = get_artworks(artwork_query, 3)

    for artwork in artworks:
        print(f"• {artwork['title']}")


if __name__ == "__main__":
    main()

• Now modules are neatly organized under one umbrella package: museum.


⚠️ IMPORTANT ⚠️

- if user inputs Claude Monet, the process will be :

First prompt searches artists and prints their names. 
Then the second prompt asks what artworks to search; if you type “Claude Monet” again there, it will search the artworks endpoint for Claude Monet and print the titles of matching Monet works --> [Water Lilies, Haystacks, and The Artist's Garden at Vétheuil]

👉 two separate inputs and two different endpoints:

• artist['title']: comes from the artists/search endpoint; the title field is the artist’s name (e.g., “Claude Monet”).
• artwork['title']: comes from the artworks/search endpoint; the title field is the artwork’s name (e.g., “Water Lilies”).
So same key name (title), but different resources and meanings (artist name vs artwork name).



✅ Key Learning Points

• Module = any Python file you can import (artwork.py, artists.py).
• Package = folder of modules + __init__.py.
• from module import function keeps calls short; import module needs module.function().
• Avoid naming variables the same as your module names (shadowing).
• Packages organize and share code professionally.
