# 🔹 Error :

distances = { 
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "88 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    m = convert(distances[spacecraft])
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()

# Output : 
# → Error : TypeError: can't multiply sequence by non-int of type 'str'

# 👉 Solution : 

distances = { 
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "88 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in distances dictionary.")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float.")
        return
         
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()

# → Input : Voyager 1 | Output : 24393037861000.0 m away
# → Input : Pioneer 10 | Output : Can't convert '88 AU' to a float.
# → Input : Voyager 3 | Output : 'Voyager 3' is not in distances dictionary.

