# 🔹 Error : Calculating pace for a marathon in minutes per mile. In the case of minutes ≤ 0. We can solve the problem by raising an Exception handlings.

# ❌ Wrong Solution :

def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in{round(pace, 2)} minutes.")

def get_pace(miles, minutes): 
    return minutes / miles

main()

# Output : 
# → You need to run each mile in 0.0 minutes (Incorrect output)

####################################################################################################################################################

# ✅ Correct Solution (1):

def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in{round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise Exception()
    
    return minutes / miles

main()

# Output :
# → Exception

##################################################################################################

# ✅ Correct Solution (2):

def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in{round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value for minutes.")
    
    return minutes / miles

main()

# Output :
# → ValueError: Invalid value for minutes.

##################################################################################################

# ✅ Correct Solution (3):

def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in{round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.")
    
    return minutes / miles

main()

# Output : 
# → ValueError: Minutes must be greater than 0.

####################################################################################################################################################

# ✅ Summary of Exception handlings :
# → We use exception handlings to alert the user / programmer that something is wrong with the input value.
# → It's important to be specific about what went wrong when raising an exception. Therefore, you can include a message when raising an exception.
# → Use ValueError when the value of the input is not valid because it's not within the range of acceptable values.
# → In this case, minutes must be greater than 0. Therefore, we will raise a ValueError with a message "Minutes must be greater than 0."
# → Use Exception when you want to raise a general exception without specifying the type of exception.
# → You can choose to use either Exception or ValueError in this case. However, it's generally better to be specific about the type of exception you're raising.
# → Raising an exception will stop the program from executing further. Therefore, the return statement will not be executed if an exception is raised.
# → The program will terminate with an error message if an exception is raised. This is useful for alerting the user / programmer that something went wrong with the input value.
# → Therefore, use exception as a general rule to handle errors in your program. If you want to be more specific about the type of error, you can use ValueError or other specific exception types.