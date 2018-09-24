import random

highest = 1000
answer = random.randint(1, highest)


correct = False
noob = False

print("please guess a number between 1 and {}".format(highest))
guess = 1
guessCounter = 0

while guess != answer:

    guess = int(input())
    if guess == 0:
        print("Program terminated")
        break
    if guess < answer:
        guessCounter += 1
        print("please guess higher, amount of guesses thus far: " + str(guessCounter))
    elif guess > answer:
        guessCounter += 1
        print("please guess lower, amount of guesses thus far: " + str(guessCounter))
    else:
        print("yay, amount of total guesses: " + str(guessCounter))

