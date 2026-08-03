import random


def main():
    target = random.randint(1, 100)
    attempts = 0

    print("--- Guess the Number Game ---")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(
                    f"🎉 Spot on! You guessed it in {attempts} attempts."
                )
                break
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
