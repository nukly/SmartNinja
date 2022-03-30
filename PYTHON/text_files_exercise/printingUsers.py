
with open("users.csv", "r") as users_data:
    users_lines = users_data.readlines()

    firstLine = users_lines[0]
    secondLine = users_lines[1]
    thirdLine = users_lines[2]
    print(firstLine[0:4] + " is " + firstLine[5:7] + " years old and " + firstLine[8:14])
    print(secondLine[0:5] + " is " + secondLine[6:8] + " years old and " + firstLine[9:13])
    print(thirdLine[0:7] + " is " + thirdLine[8:10] + " years old and " + thirdLine[11:17])


