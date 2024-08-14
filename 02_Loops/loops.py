# LOOPS --> The block of code that is going to repeat code for as many times as we want.

#1. WHILE LOOP
 # break  Use BREAK to terminate the while loop started if the condition is met.

mobNo = input("Please enter your mobile No. ")

while len(mobNo) != 10:
    mobNo = input("Invalid mobile number. Please enter a valid 10-digit mobile number: ")

print("You have entered a correct mobile number.")

#---------------+---------------
print("meow\n"*3, end="")

#2. FOR LOOP
#Lists --> List of values stored eg. [0, "vsam", true] is a list
#A list is a ordered collection of items that can hold elements of different data types.

