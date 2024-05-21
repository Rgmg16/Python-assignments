import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    
    print("Welcome to the guessing game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get the user's guess and convert it to an integer
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {secret_number}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the guessing game
guessing_game()
