import time
import random
import os

# Meme/funny sentences for the typing game
sentences = [
    "When you see your code works on the first try.",
    "I told my computer a joke, now it has a bug.",
    "Me: I'll sleep early tonight. Also me: 3 AM gaming.",
    "Why did the programmer quit his job? He didn't get arrays.",
    "404: Sleep not found. Keep typing.",
    "Debugging: Being the detective in a crime movie where you are also the murderer."
]

# High score file
highscore_file = "highscore.txt"

def get_highscore():
    if not os.path.exists(highscore_file):
        return 0
    with open(highscore_file, "r") as file:
        score = file.read()
        return float(score) if score else 0

def set_highscore(score):
    with open(highscore_file, "w") as file:
        file.write(str(score))

# Fancy ASCII title
print("🎉✨ WELCOME TO MEME TYPERUSH! ✨🎉")
print("Type these hilarious sentences as fast as you can and beat your high score!\n")

score = 0
while True:
    sentence = random.choice(sentences)
    print("\nType this sentence:")
    print(f"➡ {sentence}")

    input("Press Enter when ready...")

    start_time = time.time()
    typed = input("\nYour input: ")
    end_time = time.time()

    # Time and speed
    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    # Accuracy
    accuracy = sum(1 for a, b in zip(sentence, typed) if a == b) / len(sentence) * 100

    # Round score
    round_score = wpm * (accuracy / 100)
    score += round_score

    # Display results
    print(f"\n⏱ Time: {time_taken:.2f}s | ⚡ WPM: {wpm:.2f} | ✅ Accuracy: {accuracy:.2f}%")
    print(f"💯 Round Score: {round_score:.2f} | 🏆 Total Score: {score:.2f}")

    # High score
    highscore = get_highscore()
    if score > highscore:
        set_highscore(score)
        print("🎊 NEW HIGH SCORE! 🎊")

    # Play again?
    play_again = input("\nPlay another round? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing Meme TypeRush! 😎")
        print(f"Your final score: {score:.2f}")
        print(f"High score: {get_highscore():.2f}")
        break
