ninja_file = open("ninja.txt", "r") # ninja file open with read permission ("r")

contents = ninja_file.read()
print(contents)

ninja_file.close()


# with keyword

with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    print(contents)

# read line by line

with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines()

    for line in ninja_lines:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello from second text file!!!") # write to ninja_file_2 with write permission ("w")
