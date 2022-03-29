# Program asks user to enter a number between 1 and 100
number = int(input("Please enter a number between 1 and 100: "))

# Program prints selected number
print(str(number))

# Loop between 0 and selected number
for num in range(number):
    if num == 0: # if zero prints space
        print(str(" "))
    elif num % 3 == 0: # if num modulo 3 equals zero num is divisible by 3 and prints fizz
        print("fizz")
    elif num % 5 == 0: # if num modulo 5 equals zero num is divisible by 5 and prints buzz
        print("buzz")
    else:
        print(str(num)) # printing other numbers

