import random
import os

def get_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 50, "easy"
    elif choice == "2":
        return 100, "medium"
    elif choice == "3":
        return 200, "hard"
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 100, "medium"


def load_high_score(level):
    if not os.path.exists("score.txt"):
        return None

    with open("score.txt", "r") as f:
        scores = f.readlines()

    for line in scores:
        name, value = line.strip().split(":")
        if name == level:
            return int(value)

    return None


def save_high_score(level, attempts):
    scores = {}

    if os.path.exists("score.txt"):
        with open("score.txt", "r") as f:
            for line in f:
                name, value = line.strip().split(":")
                scores[name] = int(value)

    scores[level] = attempts

    with open("score.txt", "w") as f:
        for name, value in scores.items():
            f.write(f"{name}:{value}\n")


def play_game():
    max_range, level_name = get_difficulty()
    secret_number = random.randint(1, max_range)
    max_attempts = 7
    attempts = 0

    print(f"\nYou have {max_attempts} attempts to guess the number (1-{max_range})")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 You Won in {attempts} attempts!")

            high_score = load_high_score(level_name)

            if high_score is None or attempts < high_score:
                print("🔥 New High Score!")
                save_high_score(level_name, attempts)
            else:
                print(f"High Score for {level_name} level: {high_score}")

            break

        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")

        print(f"Attempts Left: {max_attempts - attempts}")

    else:
        print(f"\n❌ Game Over! The number was {secret_number}")


def main():
    print("====== NUMBER GUESSING GAME ======")

    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()