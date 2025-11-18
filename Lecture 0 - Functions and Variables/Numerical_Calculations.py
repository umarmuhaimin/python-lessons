### In this python file, we will learn all of the possible operations that can be performed as calculation in Python using data types such as integer, float and round ###

# Integer is a whole number, positive or negative, without decimals, of unlimited length.
# Float is a number, positive or negative, containing one or more decimals.
# Round is a function that rounds off a floating point number to a specified number of decimal places


# Method 1 of Addition :
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print (z)

# Method 2 of. Addition :
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# Method 3 of Addition :
print(int(input("What's x? ")) + int(input("What's y? ")))


# Method 1 of Subtraction :
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x - y)

# Method 2 of Subtraction :
print(int(input("What's x? ")) - int(input("What's y? ")))


# Method 1 of Multiplication :
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x * y)

# Method 2 of Multiplication :
print(int(input("What's x? ")) * int(input("What's y? ")))


# Method 1 of Division :
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x / y)

# Method 2 of Division :
print(int(input("What's x? ")) / int(input("What's y? ")))

# Method 3 of Division :
print(float(input("What's x? ")) / float(input("What's y? ")))

# Method 4 of Division :
print(round(float(input("What's x? ")) / float(input("What's y? ")), 2)) # Rounds off the answer to 2 decimal places.

# Method 5 of Division :
print(round(int(input("What's x? ")) / int(input("What's y? ")), 2)) # Rounds off the answer to 2 decimal places

# Method 6 of Division :
print(round(int(input("What's x? ")) / int(input("What's y? ")))) # Rounds off the answer to the nearest whole number. Since there is no {, 2} at the end of the code, it rounds off to the nearest whole number by default.

# Method 7 of Division :
print(round(float(input("What's x? ")) / float(input("What's y? ")))) # Rounds off the answer to the nearest whole number. Since there is no {, 2} at the end of the code, it rounds off to the nearest whole number by default.

### // is called Floor Division. It gives the largest integer value that is less than or equal to the actual division result ###

# Method 8 of Division :
print(int(input("What's x? ")) // int(input("What's y? "))) # This is called Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 7 and y = 3, then the actual division result is 2.3333, but floor division will give 2 as the answer.
# if x = 4 and y = 5, then the actual division result is 0.8, but floor division will give 0 as the answer.

# Method 9 of Division :
print(float(input("What's x? ")) // float(input("What's y? "))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 7.5 and y = 3.2, then the actual division result is 2.34375, but floor division will give 2.0 as the answer.

# Method 10 of Division :
print(round(float(input("What's x? ")) // float(input("What's y? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 7.5 and y = 3.2, then the actual division result is 2.34375, but floor division will give 2.0 as the answer and then rounds it off to 2.

# Method 11 of Division :
print(round(int(input("What's x? ")) // int(input("What's y? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 7 and y = 3, then the actual division result is 2.3333, but floor division will give 2 as the answer and then rounds it off to 2.

# Method 12 of Division :
print(int(input("What's x? ")) / int(input("What's y? ")) // int(input("What's z? "))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 20, y = 3 and z = 2, then the actual division result is 3.3333, but floor division will give 3 as the answer.
# Note : In this method, there are 3 inputs. The first two inputs (variables) of x and y are divided normally and then the result of the normal division is floor divided by the third input.

# Method 13 of Division :
print(float(input("What's x? ")) / float(input("What's y? ")) // float(input("What's z? "))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 20.5, y = 3.2 and z = 2.1, then the actual division result is 3.203125, but floor division will give 3.0 as the answer.
# Note : In this method, there are 3 inputs. The first two inputs (variables) of x and y are divided normally and then the result of the normal division is floor divided

# Method 14 of Division :
print(round(float(input("What's x? ")) / float(input("What's y? ")) // float(input("What's z? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 20.5, y = 3.2 and z = 2.1, then the actual division result is 3.203125, but floor division will give 3.0 as the answer and then rounds it off to 3.

# Method 15 of Division :
print(round(int(input("What's x? ")) / int(input("What's y? ")) // int(input("What's z? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 20, y = 3 and z = 2, then the actual division result is 3.3333, but floor division will give 3 as the answer and then rounds it off to 3.
# Note : In this method, there are 3 inputs. The first two inputs (variables) of x and y are divided normally and then the result of the normal division is floor divided by the third input.

# Method 16 of Division :
print(int(input("What's x? ")) // int(input("What's y? ")) // int(input("What's z? "))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 20, y = 3 and z = 2, then the actual division result is 3.3333, but floor division will give 3 as the answer.
# Note : In this method, there are 3 inputs. The first input (variable) of x is floor divided by the second input (variable) of y and then the result of the floor division is again floor divided by the third input (variable) of z.

# Method 17 of Division :
print(float(input("What's x? ")) // float(input("What's y? ")) // float(input("What's z? "))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result.
# for example : if x = 20.5, y = 3.2 and z = 2.1, then the actual division result is 3.203125, but floor division will give 3.0 as the answer.
# Note : In this method, there are 3 inputs. The first input (variable) of x is floor divided by the second input (variable) of y and then the result of the floor division is again floor divided by the third input (variable) of z.

# Method 18 of Division :
print(round(float(input("What's x? ")) // float(input("What's y? ")) // float(input("What's z? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 20.5, y = 3.2 and z = 2.1, then the actual division result is 3.203125, but floor division will give 3.0 as the answer and then rounds it off to 3.
# Note : In this method, there are 3 inputs. The first input (variable) of x is floor divided by the second input (variable) of y and then the result of the floor division is again floor divided by the third input (variable) of z.

# Method 19 of Division :
print(round(int(input("What's x? ")) // int(input("What's y? ")) // int(input("What's z? ")))) # This is also Floor Division. It gives the largest integer value that is less than or equal to the actual division result and then rounds it off to the nearest whole number.
# for example : if x = 20, y = 3 and z = 2, then the actual division result is 3.3333, but floor division will give 3 as the answer and then rounds it off to 3.
# Note : In this method, there are 3 inputs. The first input (variable) of x is floor divided by the second input (variable) of y and then the result of the floor division is again floor divided by the third input (variable) of z.


### Special Case ###

# Float and Round cannot be used in Floor Division (//) when there are 3 inputs. It will give an error.

# For example, the following code will give an error :
# print(float(input("What's x? ")) // float(input("What's y? ")) // float(input("What's z? "))) 
# print(round(float(input("What's x? ")) // float(input("What's y? ")) // float(input("What's z? ")))) 

# The error will be : ValueError: invalid literal for int() with base 10: '3.2'
# The reason is that Floor Division (//) gives the largest integer value that is less than or equal to the actual division result. Therefore, it cannot be used with float or round when there are 3 inputs.# However, Float and Round can be used in Floor Division (//) when there are only 2 inputs. It will not give an error.

# For example, the following code will not give an error :
# print(float(input("What's x? ")) // float(input("What's y? "))) 
# print(round(float(input("What's x? ")) // float(input("What's y? "))) 

# The reason is that Floor Division (//) gives the largest integer value that is less than or equal to the actual division result. Therefore, it can be used with float or round when there are only 2 inputs.
# However, Integer can be used in Floor Division (//) when there are 3 inputs. It will not give an error. 


### Additional Information ###

# Summary of Calculations :
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x // y) # Floor Division
print(round(x + y)) # Rounds off the answer to the nearest whole number.
print(round(x + y, 2)) # Rounds off the answer to 2 decimal places.
print(round(x - y)) # Rounds off the answer to the nearest whole number.
print(round(x - y, 2)) # Rounds off the answer to 2 decimal
print(round(x * y)) # Rounds off the answer to the nearest whole number.
print(round(x * y, 2)) # Rounds off the answer to 2 decimal
print(round(x / y)) # Rounds off the answer to the nearest whole number.
print(round(x / y, 2)) # Rounds off the answer to 2 decimal places.
print(round(x // y)) # Rounds off the answer to the nearest whole number.
print(round(x // y, 2)) # Rounds off the answer to 2 decimal places.


# For large value outputs, we can use (f"{z:,}") code to include commas in the output so that it is easier to read large numbers.
# z is just a variable. It can be any variable name.
# This code uses an f-string to format the output.
# {z:,} means: print the value of z with commas as thousands separators.
# For example, if z = 12345, the output will be 12,345.
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")


# Rounding off value to n decimal places using F-string method (f"{z:.2f}").
# .2f means "format as a floating-point number with 2 digits after the decimal point".
# For example, if z = 3.14159, the output will be 3.14.
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(f"{z:.2f}")




