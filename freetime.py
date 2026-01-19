import random

print("===================================")
print("Welcome to Gym & Boxing Tracker")
print("===================================")

# List of exercises
exercises = ["Push-ups", "Squats", "Sit-ups", "Burpees"]
punches = ["Jab", "Cross", "Hook", "Uppercut"]

# Logs
exercise_log = {}
boxing_log = {}
score = 0
round_num = 8

while True:
    print("\n------------------------------")
    print(f"Round {round_num}")
    print("Choose an option:")
    print("1. Do Gym Exercise")
    print("2. Do Boxing Combo")
    print("3. Show Logs")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("\nGym Exercises:")
        for i, ex in enumerate(exercises, 1):
            print(f"{i}. {ex}")
        ex_choice = input("Pick an exercise: ")
        
        if ex_choice.isdigit() and 1 <= int(ex_choice) <= len(exercises):
            reps = input(f"How many reps of {exercises[int(ex_choice)-1]}? ")
            if reps.isdigit():
                ex_name = exercises[int(ex_choice)-1]
                exercise_log[ex_name] = exercise_log.get(ex_name, 0) + int(reps)
                score += int(reps)
                print(f"Added {reps} reps to {ex_name}. Total score: {score}")
            else:
                print("Please enter a number.")
        else:
            print("Invalid choice.")
    
    elif choice == "2":
        combo = random.choices(punches, k=3)
        print("Do this combo: " + " - ".join(combo))
        
        for punch in combo:
            reps = input(f"How many {punch}s did you do? ")
            if reps.isdigit():
                boxing_log[punch] = boxing_log.get(punch, 0) + int(reps)
                score += int(reps)
            else:
                print("Please enter a number.")
        print(f"Combo complete. Total score: {score}")
    elif choice == "3":
        print("\nGym Exercise Log:")
        for ex, total in exercise_log.items():
            print(f"{ex}: {total} reps")
        print("\nBoxing Log:")
        for punch, total in boxing_log.items():
            print(f"{punch}: {total} reps")
        print(f"\nTotal Score: {score}")
    
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")

    round_num += 1

print("\n===================================")
print("Final Workout Summary")
print("\nGym Exercises Done:")
for ex, total in exercise_log.items():
    print(f"{ex}: {total} reps")
print("\nBoxing Punches Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")
print("===================================")
print("Keep training and stay strong!")
print("Next step is to login and surther information regrds the website or any sort of feed backs are really appreicted lollllll----------"
)for ex, total in exercise_log.items():
    print(f"{ex}: {total} reps")
print("\nBoxing Punches Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")for ex, total in exercise_log.items():
 Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")for ex, total in exercise_log.items():
    print(f"{ex}: {total} reps")
print("\nBoxing Punches Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")for ex, total in exercise_log.items():
    print(f"{ex}: {total} reps")
print("\nBoxing Punches Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")for ex, total in exercise_log.items():
    print(f"{ex}: {total} reps")
print("\nBoxing Punches Done:")
for punch, total in boxing_log.items():
    print(f"{punch}: {total} reps")
print(f"\nTotal Score: {score}")for ex, total in exercise_log.items():
   username = input("What's your name: ")
print(f"Nice to meet you, {username}3nigg")

age = input("How old are you: ")
print(f"Wow, {age} years old")

ethnicity = input("What's your ethnicity: ")
print(f"Cool, {ethnicity}")

hobby = input("What's your favourite hobby: ")
print(f"Nice {hobby} sounds fun")

city = input("Which city are you from: ")
print(f"lovely, {username} from {city}")
username = input("What's your name: ")
print(f"Nice to meet you, {username}3nigg")
printuusername = input("What's your name: ")
print(f"Nice to meet you, {username}3nigg")

age = input("How old are you: ")
print(f"Wow, {age} years old")

ethnicity = input("What's your ethnicity: ")
print(f"Cool, {ethnicity}")

hobby = input("What's your favourite hobby: ")
print(f"Nice {hobby} sounds fun")

city = input("Which city are you from: ")
print(f"lovely, {username} from {city}")
username = input("What's your name: ")
print(f"Nice to meet you, {username}3nigg")

age = input("How old are you: ")
print(f"Wow, {age} years old")

ethnicity = input("What's your ethnicity: ")
print(f"Cool, {ethnicity}")

hobby = input("What's your favourite hobby: ")
print(f"Nice {hobby} sounds fun")

city = input("Which city are you from: ")
print(f"lovely, {username} from {city}")
username = input("What's your name: ")
print(f"Nice to meet you, {username}3nigg")

age = input("How old are you: ")
print(f"Wow, {age} years old")

ethnicity = input("What's your ethnicity: ")
print(f"Cool, {ethnicity}")

hobby = input("What's your favourite hobby: ")
print(f"Nice {hobby} sounds fun")

city = input("Which city are you from: ")
print(f"lovely, {username} from {city}")
 
age = input("How old are you: ")
print(f"Wow, {age} years old")

ethnicity = input("What's your ethnicity: ")
print(f"Cool, {ethnicity}")

hobby = input("What's your favourite hobby: ")
print(f"Nice {hobby} sounds fun")

city = input("Which city are you from: ")
print(f"lovely, {username} from {city}")
