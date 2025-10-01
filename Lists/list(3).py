results = ["Mario", "Luigi"]
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) # Bowser and Donkey Kong Jr. finishes at the same time.
results.remove(["Bowser", "Donkey Kong Jr."]) # To remove Bowser and Donkey Kong Jr. from the list.
results.extend(["Bowser", "Donkey Kong Jr."]) # To add Bowser and Donkey Kong Jr. into the list as the. last item without "[]".

print(results)

# Output :
# → ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']

###################################################################################################################################

results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]
results.remove("Bowser") # To remove Bowser from the list.
results.insert(0, "Bowser") # To add Bowser into the list becoming the first place of index i = 0. 
print(results)
# Output :
# → ['Bowser', 'Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.']

###################################################################################################################################

results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]
results.reverse() # To reverse the order / arrangement of the list.
print(results)
# Output :
# → ['Donkey Kong Jr.', 'Bowser', 'Toad', 'Koopa Troopa', 'Yoshi', 'Princess', 'Luigi', 'Mario']