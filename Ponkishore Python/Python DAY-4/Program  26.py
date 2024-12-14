import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1,100)

    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess:"))
          except ValueError: 
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                    else:
                        guessed_correctly = true
                        print(f"Congratulations! You've guessed the correct number {secret_number}!")
                        print(f"It took you {attempts} attempts.")

                        play_again = input("Do you want to play again? (yes/no):") lower()
                        if play_again == "yes":
                            number_guesssing_games()
                            else:
                                print("Thanks for playing! Goodbye.")

                                if__name__ == "__main":
                                    number_guessing_game()
                                    
