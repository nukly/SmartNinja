# Uporabnika vpraša za vnos dveh številk in operacije
numberOne = float(input("Insert first number for calculation: "))
operation = input("Insert + for addition, - for subtraction, * for multiplication or / for division: ")
numberTwo = float(input("Insert second number for calculation:"))

# če je operacija + izpiše vsoto
if operation == "+":
    print(numberOne + numberTwo)

# če je operacija - izpiše razliko
elif operation == "-":
    print(numberOne - numberTwo)

# če je operacija * izpište produkt
elif operation == "*":
    print(numberOne * numberTwo)

# če je operacija / izpiše kvocient
elif operation == "/":
    print(numberOne / numberTwo)
else:
    print("Operation not found!")
