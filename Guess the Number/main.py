import random

# Generates any random number between 1 to 1000
randNo = random.randint(1, 1000)

#intialization
yourGuess = None
guesses = 0

# Run loop till your guess equals to random number
while(yourGuess != randNo):
    yourGuess = int(input("Enter your guess: "))
    guesses += 1
    if(yourGuess==randNo):
        print("You guessed it right!")
    else:
        if(yourGuess>randNo):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

# Prints the number of attempt you takes to guess correct number
print(f"You guessed the number in {guesses} guesses")

# Saves the number of attempt as your new highscore in the highscore.txt file
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

#updates the highcore.txt file
if(guesses<highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
