#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value

number = input("Please enter in an integer value")




try:
    number = int(number)
except:
    print("nope")
    number = 43


print(number)

