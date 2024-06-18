import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(0,50)
    
    print("Welcome to the Number Guessing Game!")
    print("Can you read minds?")
    print()

    while True:
        # Ask the user to guess the number
        guess = int(input("I am thinking of a number between 0 and 50. Can you guess it?"))
        
        # Compare the user's guess with the secret number
        if guess == secret_number:
            print("Congratulations! You have a brilliant brain.")
            break
        elif guess < secret_number:
            print("Higher!")
        else:
            print("Lower!")

if __name__ == "__main__":
    guess_number()
