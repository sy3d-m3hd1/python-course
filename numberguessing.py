import random

secret = random.randint(1, 100)
attempts = 0

print("Welcome! I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try higher.")
    elif guess > secret:
        print("Too high! Try lower.")
    else:
        print(f"Correct! You got it in {attempts} guess{'es' if attempts > 1 else ''}!")
        break