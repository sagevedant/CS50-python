# INPUTS
usersName = input("What is your name? ")
print("Hello, " + usersName)

#But other way to do so is...
print("Hello,",usersName)
#So when you pass a multiple arguments in print it auto generates a extra space for you so no need of preceeding space
usersHeight = float(input("Enter your Height in meters? "))
heightForBMI = usersHeight*usersHeight
usersWeight = float(input("Enter your weight in Kgs? "))
BMI = usersWeight/heightForBMI

if BMI < 18.5:
    print("You are Underweight, BulkUpp Dude!!")
elif 18.5 <= BMI <= 25:
    print("You have a perfect height and weight my friend continue!!")
else:
    print("You are overweight, Hit GYM!!")