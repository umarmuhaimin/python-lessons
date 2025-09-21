# Common for_loop examples :

# 1. Printing / Output with storing data :

# for i in [0, 1, 2]:      # Since the sequence has 3 orders starting from 0 → 1 → 2 ; It will print : meow [0], meow [1], meow [2]
#     print("meow")
# Output : meow, meow, meow

# for i in range(10):      # sequence has 10 orders. Therefore, arrangement starts from 0 → 9 {10 orders}. It will print : meow [0] → meow [9]
#     print("meow")
# Output : meow {10 times}

#########################################################################################################

# 2. Printing / Output without storing data :

# for _ in range(2):      # _ underscore indicates no storing data but still has sequence without any arrangement/order.
#     print("meow")
# Output : meow, meow

#########################################################################################################

# 3. Simpified way to print something with large numbers and printed downwards 

# With default print() : 

# print("meow\n" * 3)
# "meow\n" * 3 → will output : "meow\nmeow\nmeow\n".
# "/n" will print the data downwards.
# Output :
#          meow⏎
#          meow⏎
#          meow⏎
#          ⏎
# By default, print() will add → end="\n" (a newline/default line) at the end.
# That is why there are 4 newlines total → the last one is just a blank/empty line.


# print("meow\n" * 3, end="")
# "meow\n" * 3 → repeats "meow\n" 3 times → "meow\nmeow\nmeow\n".
# "/n" will print the data downwards.
# Output :
#          meow⏎
#          meow⏎
#          meow⏎
# end="" → tells Python not to add an extra newline at the end of the print(). 
# That is why there are only 3 newlines in total → the last default line is removed by end="" prompt.

#########################################################################################################

# 4. Creating meow as a function :

# def main ():
#     meow(3)

# def meow(n):
#     for _ in range(n):     # Since arrangement/order dosen't matter ; the system will print/output meow 3 times using for_loops.
#         print("meow")
# main()

# Output :
#          meow⏎
#          meow⏎
#          meow⏎
#          ⏎                 # Since there is no end="", it will also print default line.


