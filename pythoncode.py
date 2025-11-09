import random

def choose_difficulty():
    print("Choose a difficulty:")
    print("1. Easy (1–20, 10 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 5 attempts)")
                          
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return (20, 10)
        elif choice == "2":
            return (50, 7)
        elif choice == "3":
            return (100, 5)
        else:
            print("Invalid choice. Try again.")

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    max_number, attempts_left = choose_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {attempts_left} attempts to guess it!\n")

    while attempts_left > 0:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(guess)
        attempts_left -= 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it with {attempts_left} attempts left.\n")
            break

        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}\n")
        else:
            print(f"💀 Out of attempts! The number was {secret_number}.\n")

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
