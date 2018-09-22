print("\nGuess the number")
guess = int(input())

if guess != 7:
    if guess < 7:
        print("Guess higher")
    else:
        print("Guess lower")

    guess = int(input())

    if guess == 7:
        print("John 117")
    else:
        print("I YIELD! ")


else:
    print("Bullseye.")
