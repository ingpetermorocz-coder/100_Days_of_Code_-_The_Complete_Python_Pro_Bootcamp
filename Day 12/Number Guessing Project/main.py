from art import logo
import random

def test(n,i):
    play = True
    while play:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        i -= 1
        if guess < n:
            print("Too low.")
        elif guess > n:
            print("Too high.")
        else:
            print(f"You got it! The answer was {guess}")
            play = False
        if i == 0 and guess != n:
            print("You've run out of guesses. Refresh the page to run again.")
            play = False

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    number_of_guesses = 10
    test(n=number, i=number_of_guesses)
else:
    number_of_guesses = 5
    test(n=number, i=number_of_guesses)
