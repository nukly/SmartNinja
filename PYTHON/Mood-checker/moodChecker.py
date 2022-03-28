
mood = input("What is your mood today?")

if mood == "happy":
    print("It's great to see you happy!")
elif mood == "nervous":
    for x in range(3):
        print("Take a deep breath!")
elif mood == "sad":
    print("All will be alright!")
elif mood == "excited":
    print("Nice to see you so excited!!!")
elif mood == "relaxed":
    print("Nice to see you relaxed!!!")
else:
    print("I don't recognize this mood.")
