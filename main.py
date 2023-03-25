import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Loop until the player guesses the correct number
while True:
    # Ask the player to guess a number
    guess = int(input("Guess a number between 1 and 100: "))
    # Increment the number of guesses
    num_guesses += 1
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses!")
        break
    # If the guess is incorrect, give a hint to the player
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
