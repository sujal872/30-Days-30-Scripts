import time

data = [
    {
        "question": "Who developed Python Programming Language?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "In which year was Python first released?",
        "options": ["1991", "1985", "2000"],
        "answer": "1991"
    },
    {
        "question": "What is the file extension of Python files?",
        "options": [".py", ".pt", ".python"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store True or False values in Python?",
        "options": ["int", "bool", "string"],
        "answer": "bool"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["echo()", "print()", "show()"],
        "answer": "print()"
    },
    {
        "question": "Which keyword is used for loops in Python?",
        "options": ["loop", "for", "iterate"],
        "answer": "for"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["object", "class", "define"],
        "answer": "class"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */"],
        "answer": "#"
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "options": ["scan()", "input()", "get()"],
        "answer": "input()"
    }
]


def main():

    score = 0
    total_questions = len(data)

    print("\n===== Python Quiz Game =====\n")

    start_time = time.time()

    for q in data:

        print("\n" + q["question"])

        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Choose option (1-3): "))
            user_ans = q["options"][choice - 1]
        except:
            print("Invalid input!")
            continue

        if user_ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! Correct answer:", q["answer"])

    end_time = time.time()
    total_time = end_time - start_time

    percentage = (score / total_questions) * 100

    print("\n===== RESULT =====")
    print("Score:", score, "/", total_questions)
    print("Incorrect:", total_questions - score)
    print("Percentage:", round(percentage, 2), "%")
    print("Time Taken:", round(total_time, 2), "seconds")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 40:
        print("Grade: C")
    else:
        print("Grade: D")


if __name__ == "__main__":
    main()