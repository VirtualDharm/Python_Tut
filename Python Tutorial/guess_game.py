import random
RandNumber = random.randint(1, 100)
Guess = None
Guesses = 0

while (Guess != RandNumber):
    Guess = int(input("Enter your guess: "))
    Guesses += 1
    if(Guess == RandNumber):
        print("You are right!")
    else:
        if(Guess < RandNumber):
            print("You have to guess higher")
        else:
            print("You have to guess lower")

print(f"You guessed the right answer {Guess} in {Guesses} turns.")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(Guesses < hiscore):
    print("You have broken the best score!")
    with open("hiscore.txt","w") as f:
        f.write(str(Guesses))



