# user inputs a range A, B
# machine will pick a random number within range(A, B) and store as the variable 'random_num'
# user makes their first guess within within range(A, B) and is stored as the variable 'guess' (if outside then an error message is displayed)
# user will be displayed feedback based on their input guess whether it is higher or lower than 'random_num'
# number of guesses will be displayed each guess and will be asked to input another guess
# when user guesses the 'random_num' correctly a congratulations message will be displayed as well as the total number of guesses

print("Welcome to the guessing game! Please input a range when asked and the machine will pick a number at random and you will guess the correct number with feedback displayed on whether your guess was too low or too high and will track the number of guesses. Good luck!")
A = int(input(print("Please choose the starting number of the range")))
B = int(input(print("Please choose the ending number of the range")))
print(f"You have picked the range {A}-{B}")
print(input("Please enter your first guess"))