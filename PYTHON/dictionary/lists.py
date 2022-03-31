import json
import random
import datetime

current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0
username = input("Enter name to play guessing game: ")

score_data = {"username": username, "attempts": attempts, "date": datetime.datetime.now, "secret_number": secret}

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"username:": username, "attempts": attempts, "date": str(datetime.datetime.now()),
                           "secret_number": secret})
        print("You've guessed it - congratulations! It's number " + str(secret))
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
            for score_dict in score_list:
                print(str(score_dict))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
