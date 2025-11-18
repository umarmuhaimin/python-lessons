# 🔹 Basic structure of dict.
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft):      # create_report is a function to print out data from the dictionary in formal report format.
    return f"""
    ========= REPORT ========

    Name : {spacecraft["name"]}
    Distance : {spacecraft["distance"]} AU 


    =========================
    """
main()

# Output :
#    ========= REPORT ========
#
#    Name : Voyager 1
#    Distance : 163 AU             # AU → Astronomical Units
#
#
#    =========================

# 👉 Here’s a simple explanation:
# → You have a dictionary called spacecraft with two pieces of information: its name and its distance.
# → The function create_report(spacecraft) makes a nicely formatted report using those details.
# → The f"""...""" lets you put the values from the dictionary right into the report.
# → When you run the program, it prints out the report showing the name and distance of the spacecraft.
# 👉 In short:
# → Your code takes info about a spacecraft and prints it out in a neat report format.

##########################################################################################################################################

# 🔹 Addition of keys_and_values into a dictionary without chaing the main/original dict.
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
  # dictionary["key"] = value         → This prompt will add the new key_and_value into the main dictionary.
    print(create_report(spacecraft))

def create_report(spacecraft):      # create_report is a function to print out data from the dictionary in formal report format.
    return f"""
    ========= REPORT ========

    Name : {spacecraft["name"]}
    Distance : {spacecraft["distance"]} AU 


    =========================
    """
main()


# Output :
#    =========================
#    
#
#    ========= REPORT ========
#
#    Name : James Webb Space Telescope
#    Distance : 0.01 AU 
#
#
#    =========================

##########################################################################################################################################

# 🔹 Dictionary using .get() method : Basically an alternate way of applying dictionary. Use .get() to obtain the key_and_value from the dict BUT if data does not exist, you can alter any value as unknown data.
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))

def create_report(spacecraft):      # create_report is a function to print out data from the dictionary in formal report format.
    return f"""
    ========= REPORT ========

    Name : {spacecraft.get("name", "Unknown")}            
    Distance : {spacecraft.get("distance", "Unknown")} AU 


    =========================
    """
main()

# Output :
#    =========================
#    
#
#    ========= REPORT ========
#
#    Name : James Webb Space Telescope
#    Distance : Unknown AU              → If there is no data of keys_and_values inside the dict : It will output the unknown key name and its value as "NONE". If there is keys_data inside the dict, it will output its values, otherwise "NONE" or "Unknown".
#                                       → You can alter it by adding any phrase/word that you want after the unknown key name @ spacecraft.get("distance", "Unknown").
#
#    =========================

##########################################################################################################################################

# 🔹 Update / Addition of keys_and_values into the main dict.
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):      # create_report is a function to print out data from the dictionary in formal report format.
    return f"""
    ========= REPORT ========

    Name : {spacecraft["name"]}
    Distance : {spacecraft["distance"]} AU 
    Orbit : {spacecraft["orbit", "Unknown"]}


    =========================
    """
main()

# Output :
#    =========================
#    
#
#    ========= REPORT ========
#
#    Name : James Webb Space Telescope
#    Distance : 0.01 AU             
#    Orbit : Sun
#    =========================

##########################################################################################################################################

# 🔹 Print keys_and_values in order / index :

# dictionary = {"key": "value"}
distances = {"Voyager 1": 163,
             "Voyager 2": 136,
             "Pioneer 10": 80,
             "New Horizons": 58,
             "Pioneer 11": 44
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")

main()

# Output :
# Voyager 1 is 163 AU from Earth [0]
# Voyager 2 is 136 AU from Earth [1]
# Pioneer 10 is 80 AU from Earth [2]
# New Horizons is 58 AU from Earth [3]
# Pioneer 11 is 44 AU from Earth [4]

# 👉 .keys() gives you a list of all the keys in a dictionary. It will only go through the keys from the dict.
# 👉 Simple example:
# → If you have distances = {"Voyager 1": 163, "Voyager 2": 136},
# → then distances.keys() gives you ["Voyager 1", "Voyager 2"].
# 👉 In your code:
# → It lets you loop through all the spacecraft names in the dictionary.


# 👉 values are outputted using distances[name].
# → for name in distances.keys(): loops through each key (spacecraft name) in the dictionary.
# → For each name, distances[name] gets the value (distance) for that spacecraft.
# → print(f"{name} is {distances[name]} AU from Earth") prints both the name and its distance.
# → In short : print(f"{spacecraft name keys} is {distance of spacecraft values} AU from Earth")
# 👉 Example:
# → For "Voyager 1", distances["Voyager 1"] gives 163, so it prints:
# → Voyager 1 is 163 AU from Earth

# 👉 In short :
# → [name] = key from distances dict
# → distances[name] = value of the key from distances dict
# → distances[name] gives you the value for that key from the distances dictionary.
# → For example, if name is "Voyager 1", then distances["Voyager 1"] is 163.
# → for name in distances.keys() ----> name is a loop variable so process will be outputed one by one / index by index from i = 0.

##########################################################################################################################################

# 🔹 We want to display the distance of each spacecraft from the earth planet in metres s.i unit.
# dictionary = {"key": "value"}

distances = {"Voyager 1": 163,
             "Voyager 2": 136,
             "Pioneer 10": 80,
             "New Horizons": 58,
             "Pioneer 11": 44
}

def main():
    for distance in distances.values():         # .values() will only go through values of keys inside the dict. Loop variable can be anything, just suite it with the scenario.
        print(f"{distance} AU is {convert(distance)} metres from Earth")  
        # both distance above equal in value. First it will input {distance}, and then it will convert {distance}. Finally, output distance in metres.

def convert(au):
    return au * 149597870700       # To convert 1 AU into metres, anything related to multiplication : use return function.

main()

# Output :
# # → 163 AU is 24384452924100 metres from Earth
# # → 136 AU is 20345310415200 metres from Earth
# # → 80 AU is 11967829656000 metres from Earth
# # → 58 AU is 8676676500600 metres from Earth
# # → 44 AU is 6582306310800 metres from Earth

# 👉 Steps :
# 1. since this system will only go through the values from the dict --> It will go from index [0] which is 163 AU until index [4] which is 44 AU.
# 2. distance = values of keys from the dict.
# 3. We are converting the distance from i = 0 --> i = 4 using the convert function.
# 4. We will output the conversions in order.

# 👉 Process and Output
# Process :
# # → print(f"{163} AU is {convert(163)} metres from Earth")  | from i = 0 which equivalent to 163.
# Output : 
# # → 163 AU is 24384452924100 metres from Earth
