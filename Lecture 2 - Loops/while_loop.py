# While Loop Summary

# Definition: 
# → A while loop repeats a block of code as long as a condition is True. 
# → While the condition is true, continue repeating the block of code/loop unitl it reaches a false condition.


# Basic structure of while_loop
# while condition:
      # code to repeat


# Key Points :
# → The condition is checked before every loop iteration.
# → If the condition is True → loop runs.
# → If the condition is False → loop stops.
# → Be careful: if the condition never becomes False, you get an infinite loop.
# When the condition becomes true, {loops continue} → it skips the rest of the current iteration and goes back to check the condition.
# When the condition becomes false, {loops break} → immediately stops the loop.
# In one line : Use while loops for repetition with a condition, especially when the number of iterations is uncertain.
# repetition with a condition → while_loop

# When to Use While Loops :
# → When you don’t know beforehand how many times you need to loop.
# → Example: keep asking user for input until they type something valid.


# Common while_loop examples :

# 1. Reduction from i = 3 to i = 1 :
#    i = 3                               # the variable i stores the data of integer 3.
#    while i != 0:                       # while i is not equivalent to 0, then loop continue. If i = 0, then loop breaks.
#        print("meow")
#.       i = i - 1

# 2. Addition from i = 1 to i = 3       {Increment Process}
#    i = 1
#    while i <= 3:                       # while i is always lesser or equal to 3, then loop continues. From the increment process, If i > 3, then loop breaks.
#       print("meow")                    # inequality matters.
#       i = i + 1

#    i = 0
#    while i < 3:                        # Condition : i is lesser than 3 {i < 3}, then loop continues. integer of 3 is not included.
#       print("meow")                    # From the increment process, if i equals to 3, then loop breaks.
#       i = i + 1

# {i = i + 1} is equivalent to {i += 1} → it is used to increment an integer value that is stored inside a variable.

# 3. Positive and Negative condition
#    while True:
#        n = int(input("What's n? "))
#        if n < 0:                       # while n is always negative and not equal to 0, it will keep continue asking question / return back to check whether the new input match the condition.
#            continue                    
#        else:                           # If the user's input is equal to 0 or any positive number, the loop will break (immidiately exit the loop).
#            break

# Explanation 
# 1. while True: → infinite loop until you explicitly break.
# 2. Asks the user: "What's n? ".
# 3. If input is a negative number → continue (skips back to the top of the loop and asks again).
# 4. If input is 0 or positive → break (exits the loop).
# ✅ Loop ends after you enter 0 (or any positive number).

# 👉 Notice:
# If you keep typing negative numbers, the loop never stops.
# First non-negative number makes the loop exit.

# 4. while_loop with for_loop :

# while True:
#     n = int(input("What's n? "))
#     if n > 0:                         # if n is equal to any positive number, the loop will break. 
#         break                         # Then, it will print n numbers of meow. n is a positive integer inputed by user. 
             
# for _ in range(n):                    # If n is equal to 0 or any negative number, the loop will continue asking questions.
#     print("meow")                     

# In this case, if n match the condition : the loop will break. Otherwise, if n does not match the condition : the loop continues.

# If any data match the condition, then continue will occur. This process will also occur for break.
# If any data match the condition, then break will occur. All of these process depends on the scenario.

# Summary :
# if n is equal to 0 or any negative number, the loop will continue keep asking questions.
# Until there is an input (positive integer) which match the condition, the loop will break.

####################################################################################################################################################################

