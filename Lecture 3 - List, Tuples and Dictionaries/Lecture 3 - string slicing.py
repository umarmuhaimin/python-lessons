# 🔹 String slicing method → [beginning:ending] → [starts with what index:end with what index] → [inclusive;exclusive]


def main():
    phone = "617-494-1000"
    print(phone[0:3])              # String slicing method will print the first 3 characters from index 0 to index 2.

main()

# Output : 617

# 🔹 Explaination for [0:3]
# → The first number you include will be inclusive [0]. The second number you include will be exclusive [3]. In terms of inequality : 0≤ x < 3.
# → So it will print the characters from index 0 to index 2.

#################################################################################################################################################

def main():
    phone = "617-494-1000"
    print(phone[:3])              # String slicing method will print the first 3 characters from index 0 to index 2.

main()

# Output : 617

# 🔹 Explaination for [:3]
# → If you don't include the first number (blank), it will automatically start from index 0. Python assumes you want to start from the beginning of the string from index 0.

#################################################################################################################################################

def main():
    phone = "617-494-1000"
    print(phone[8:12])              # String slicing method will print the characters from index 8 to index 11.

main()

# Output : 1000

#################################################################################################################################################

def main():
    phone = "617-494-1000"
    print(phone[8:])              # String slicing method will print the characters from index 8 to index 11.

main()

# Output : 1000

# 🔹 Explaination for [8:]
# → If you don't include the second number (blank), it will automatically go until the end of the string. Python assumes you want to go until the end of the string.
# → the length of the string is 12 characters starting from index 0 to index 11. The second number is exclusive, so we will only include the index up until index 11.
# → In terms of inequality : 8 ≤ x < 12. So it will print the characters from index 8 to index 11.
# → IMPORTANT : since there are 12 characters in the string and index always starts from 0, the range of index : 0 ≤ x ≤ 11.
# → THEREFORE: index 12 does not exist!

#################################################################################################################################################

def main():
    phone = "617-494-1000"
    print(phone[-4:])              # String slicing method will print the last 4 characters from index -4 to index -1.

main()

# Output : 1000

# 🔹 Explaination for [-4:]
# → Negative indexing starts from the end of the string. The last character is index -1, the second last character is index -2, the third last character is index -3, and so on.
# → IMPORTANT : the first character in the string starting from the left is always index 0.
# → IMPORTANT : the first character in the string starting from the right is always index -1.
# → THEREFORE : string slicing method will print index starting from i = -4 until the end of the string which is to the rightmost character until index -1.
# → In terms of inequality : -4 ≤ x < 0. So it will print the characters from index -4 to index -1.

#################################################################################################################################################