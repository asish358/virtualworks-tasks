import random

def guess_the_number():
    target = random.randint(1, 100)
    attempts = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < target:
                print("Too low! Try higher. ⬆️")
            elif guess > target:
                print("Too high! Try lower. ⬇️")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    guess_the_number()
