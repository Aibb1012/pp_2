# guessGame
import random
def guessGame():
    guessNumber = random.randint(1, 20)
    total = 0
    you_num = 0
    name = input("Hello! What is your name? ")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    while(you_num!=guessNumber):
        you_num = int(input("Take a guess\n"))
        total+=1
        if you_num<guessNumber:
            print("\nYour guess is too low.")
        if you_num>guessNumber:
            print("\nYour guess is too big.")
    
    print(f"Good job, {name}! You guessed my number in {total} guesses!")
guessGame()