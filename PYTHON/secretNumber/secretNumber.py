# določanje spremenljivke za skrivno številko
secret = 44

# Uporabniku narekujemo, da ugane številko
guess = int(input("Guess the number and you'll be rich!"))

# pogojni stavek ob zmoti izpiše sporočilo o zmoti uporabniku
if guess != secret:
    print("Bad guess! No luck for you today!")

#pogojni stavek ob pravilnem odgovoru čestita uporabniku
elif guess == secret:
    print("Congratulations! You won!!!")

