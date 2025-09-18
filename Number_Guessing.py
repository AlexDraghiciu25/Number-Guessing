import number_guessing_art
import random

print(number_guessing.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
ok_difficulty = 0

if difficulty == "easy" or difficulty == "hard":
    ok_difficulty = 1

while ok_difficulty == 0:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy" or difficulty == "hard":
        ok_difficulty = 1

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

num_between_1_and_100 = random.randint(1, 100)
# print(num_between_1_and_100)

finish = 0  # We suppose that the game is not finished yet
while attempts > 0 and finish == 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > num_between_1_and_100:
        print("Too high.")
    elif guess < num_between_1_and_100:
        print("Too low.")
    else:
        finish = 1      # We found the number

    attempts -= 1
    if finish == 1:
        print(f"You got it! The answer was {num_between_1_and_100}.")
    else:
        if attempts != 0:
            print("Guess again.")

if attempts == 0 and finish == 0:
    print(f"You've run out of guesses. You lost the game!"

          f"The answer was {num_between_1_and_100}")
