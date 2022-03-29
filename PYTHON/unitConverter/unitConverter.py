# Greeting and program description
print("Welcome to unit converter. This program converts kilometers to miles.")

# Program ask user to insert number of kilometers
kilometers = float(input("Enter kilometers to convert it into miles: "))

# Calculation from kilometers to miles
miles = kilometers * 0.621371

# Printing calculated miles

print(str(kilometers) + " kilometers is " + str(miles) + " miles")

# Program asks user if he would want to do another conversion
anotherConversionQuestion = input("Do you want to do another conversion? Y for yes or N for no: ")

# If user want to do another conversion program repeats until he enters N or wrong letter
while anotherConversionQuestion == "Y":
    kilometers = float(input("Enter kilometers to convert it into miles:"))
    miles = kilometers * 0.621371
    print(str(kilometers) + " kilometers is " + str(miles) + " miles")
    anotherConversionQuestion = input("Do you want to do another conversion? Y for yes or N for no: ")
if anotherConversionQuestion == "N":
    print("Goodbye!")
else:
    print("You have probably entered wrong letter. Goodbye!")




