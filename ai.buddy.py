import random

def get_response(question, mode):
    question = question.lower()

    responses = {
        "variable": {
            "kid": "A variable is like a labelled box that stores something! Like a box called 'name' that holds 'Syed'.",
            "teen": "A variable stores a value in memory. Example: age = 13 stores the number 13 with the label 'age'.",
            "adult": "A variable is a named reference to a memory location. Python is dynamically typed so the type is inferred at runtime.",
        },
        "loop": {
            "kid": "A loop is doing the same thing over and over! Like saying 'hello' 5 times without writing it 5 times.",
            "teen": "A loop repeats code. A for loop runs a set number of times, a while loop runs until a condition is false.",
            "adult": "Python has for loops (iterating over iterables) and while loops (condition-based). Use enumerate() and zip() for cleaner iteration.",
        },
        "function": {
            "kid": "A function is a mini-program with a name! You make it once and can use it anytime you like.",
            "teen": "A function is a reusable block of code. Define it with def, give it a name, and call it whenever you need it.",
            "adult": "Functions are first-class objects in Python. They support default args, *args, **kwargs, decorators, and closures.",
        },
        "list": {
            "kid": "A list is like a shopping list in Python — it holds many things in one place!",
            "teen": "A list stores multiple values in order. Example: fruits = ['apple', 'banana', 'mango']",
            "adult": "Lists are mutable ordered sequences. Use list comprehensions for clean transformations: [x*2 for x in nums]",
        },
        "if": {
            "kid": "If is like asking a question! IF it is raining, take an umbrella. Otherwise, don't!",
            "teen": "An if statement runs code only when a condition is true. Add elif and else for other cases.",
            "adult": "Conditional branching uses if/elif/else. Python also supports ternary expressions: x if condition else y",
        },
        "turtle": {
            "kid": "Turtle is a fun drawing tool! You control a little turtle that draws lines as it moves around the screen.",
            "teen": "The turtle module lets you draw shapes by moving a cursor. Use forward(), left(), and right() to control it.",
            "adult": "Turtle is a graphics module based on Logo. It uses a screen canvas and supports penup/pendown, fill, color, and speed controls.",
        },
        "python": {
            "kid": "Python is a coding language! It's one of the easiest to learn and you can make games, apps, and art with it.",
            "teen": "Python is a popular programming language known for its simple, readable syntax. It's used in web dev, AI, and data science.",
            "adult": "Python is a high-level interpreted language with dynamic typing and a large standard library. It emphasises readability via PEP 8.",
        },
    }

    for keyword, answers in responses.items():
        if keyword in question:
            return answers[mode]

    defaults = [
        "Great question! Try searching that on W3Schools or Python.org for a detailed answer.",
        "I'm not sure about that one — but keep asking questions, that's how you learn!",
        "Hmm, tricky! Break it into smaller parts and search each one separately.",
    ]
    return random.choice(defaults)


def main():
    print("=" * 40)
    print("    Welcome to AI Study Buddy!")
    print("=" * 40)
    print("\nPick your mode:")
    print("  1. Kid mode")
    print("  2. Teen mode")
    print("  3. Advanced mode")

    modes = {"1": "kid", "2": "teen", "3": "adult"}
    while True:
        choice = input("\nEnter 1, 2 or 3: ").strip()
        if choice in modes:
            mode = modes[choice]
            print(f"\n{mode.capitalize()} mode selected. Let's go!")
            break
        print("Please enter 1, 2 or 3.")

    print("\nAsk me anything! Type 'quit' to exit.")
    print("-" * 40)

    while True:
        question = input("\nYou: ").strip()

        if not question:
            continue
        if question.lower() == "quit":
            print("Goodbye! Keep learning!")
            break

        answer = get_response(question, mode)
        print(f"\nBuddy: {answer}")


main()