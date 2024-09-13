# user inputs a range A, B
# machine will pick a random number within range(A, B) and store as the variable 'random_num'
# user makes their first guess within within range(A, B) and is stored as the variable 'guess' (if outside then an error message is displayed)
# user will be displayed feedback based on their input guess whether it is higher or lower than 'random_num'
# number of guesses will be displayed each guess and will be asked to input another guess
# when user guesses the 'random_num' correctly a congratulations message will be displayed as well as the total number of guesses

# for random library
import random
#welcome message and description
print("Welcome to the guessing game! Please input a range when asked and the machine will pick a number at random and you will guess the correct number with feedback displayed on whether your guess was too low or too high and will track the number of guesses. Good luck!")
# range input
A = int(input("Please choose the starting number of the range: "))
B = int(input("Please choose the ending number of the range: "))
# range
print(f"You have picked the range {A}-{B}")
# random library
random_num = random.randint(A, B)
# num_of_guesses
num_of_guesses = 0
# first guess
guess = int(input("Please enter a guess: "))
num_of_guesses += 1
# while loop for guesses
while guess != random_num:
    if guess > random_num:
        print("That is too high! Guess again")
    elif guess < random_num:
        print("That is too low! Guess again")
# number of guesses
    print(f"Total number of guesses: {num_of_guesses}")

    num_of_guesses += 1
    guess = int(input("Please enter a guess: "))
# congratulations message
print("Congratulations, you have won!")
print(f"Total number of guesses: {num_of_guesses}")
