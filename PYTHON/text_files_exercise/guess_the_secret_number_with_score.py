import random

secret = random.randint(1, 100)
attempts = 0

with open("score.txt", "r") as score_file:
    top_score = int(score_file.read())
    print("Top score: " + str(top_score))

while True:
    # asks player to guess the secret number
    guess = int(input("Guess the secret number between 1 and 100: "))

    # add one for each attempt
    attempts += 1

    if guess == secret:
        print("Well done! You guessed it - congratulations!!! It is number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < top_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        with open("score.txt", "r") as score_file:
            score_file.readline()

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
