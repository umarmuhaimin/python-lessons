# 🔹 Common way of storing data using variables :
def main():
    latitude = 42.376
    longitude = -71.115
    print("Latitude:", latitude)
    print("Longitude:", longitude)

main()

# Output : 
# → Latitude: 42.376
# → Longitude: -71.115

#################################################################################################################################################

# 🔹 Storing data using tuples : 
def main():
    coordinates = (42.376, -71.115)
    (x, y) = coordinates
    print(coordinates)

main()

# Output :
(42.376, -71.115)

#################################################################################################################################################

def main(): 
    coordinates = (42.376, -71.115)
    (x, y) = coordinates
    (latitude, longitude) = coordinates
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")

main()

# Output : 
# → Latitude: 42.376
# → Longitude: -71.115

# 👉 IMPORTANT : Tuple is just like a list but it is immutable. It means that the tuple_list items cannot be modified, added or removed.
# 👉 You can still access items using index positions, just like lists. 
# 👉 The first item on the tuple_list will always starts with index 0 and so on.

#################################################################################################################################################

def main(): 
    coordinates = (42.376, -71.115)
    (x, y) = coordinates
    (latitude, longitude) = coordinates       # The return value {} inside f"" string can either be (x, y), (latitude, longitude) or using position indexes.
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

main()

# Output : 
Latitude: 42.376
Longitude: 71.115

# 👉 Difference between list and tuple :
# → Lists are mutable (can be changed: items can be modified, added and removed), while tuples are immutable (cannot be changed: items can't be modified and etc).
# → Lists use square brackets [ ], while tuples use parentheses ( ).
# → Tuples are generally faster than lists for certain operations due to their immutability.
# → Tuples can be used as keys in dictionaries, while lists cannot.
# → Tuples are often used for fixed collections of items, while lists are used for collections that may change.
# → Tuples support tuple unpacking, allowing multiple variables to be assigned in one line (e.g., x, y = coordinates).
# → Lists have more built-in methods for modification (like append, remove), while tuples have fewer methods due to their immutability.

# 👉 Benefits of using tuples:
# → You want faster performance (tuples are slightly faster than lists because it takes less memory and more efficient).
# → In order to use tuple, you need to have a fixed data that should not be changed because tuple is immutbale (once a tuple is created, the elements/items cannot be modified, added, or removed).
