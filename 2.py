quiz = [
    ("What is 5 + 3?", "8"),
    ("What is 10 - 4?", "6"),
    ("What is 2 * 6?", "12"),
    ("What is 15 / 3?", "5"),
    ("What is 7 squared?", "49"),
    ("What is the square root of 64?", "8"),
    ("What is 3 + 2 * 4?", "11"),
    ("What is (12 - 5) * 3?", "21"),
    ("What is 18 divided by 6?", "3"),
    ("What is 20 + 30 - 10?", "40"),
    ("What is 4 * 5 - 2?", "18"),
    ("What is 15 / 5 + 1?", "4"),
    ("What is 9 squared?", "81"),
    ("What is the square root of 100?", "10"),
    ("What is 7 + 2 * 3?", "13"),
    ("What is (20 - 6) / 7?", "2"),
    ("What is 24 divided by 4?", "6"),
    ("What is 25 - 12 + 8?", "21"),
    ("What is 6 * 3 - 4?", "14"),
    ("What is 18 / 3 + 2?", "8"),
    ("What is 5 squared?", "25"),
    ("What is the square root of 144?", "12"),
    ("What is 8 + 4 * 2?", "16"),
    ("What is (15 - 3) * 2?", "24"),
    ("What is 30 divided by 5?", "6"),
    ("What is 35 - 17 + 9?", "27"),
    ("What is 10 * 2 - 5?", "15"),
    ("What is 16 / 4 + 1?", "5"),
    ("What is 3 cubed?", "27"),
    ("What is the cube root of 27?", "3"),
    ("What is 9 + 6 - 2?", "13"),
    ("What is (25 - 10) / 5?", "3"),
    ("What is 28 divided by 7?", "4"),
    ("What is 40 - 15 + 7?", "32"),
    ("What is 5 * 4 - 3?", "17"),
    ("What is 21 / 7 + 3?", "6"),
    ("What is 7 squared minus 3?", "46"),
    ("What is the square root of 81?", "9"),
    ("What is 6 + 2 * 5?", "16"),
    ("What is (18 - 6) / 3?", "4"),
    ("What is 27 divided by 9?", "3"),
    ("What is 22 - 9 + 4?", "17"),
    ("What is 9 * 3 - 6?", "21"),
    ("What is 20 / 4 + 2?", "7"),
    ("What is 8 squared?", "64"),
    ("What is the square root of 196?", "14"),
    ("What is 9 + 3 * 4?", "21"),
    ("What is (30 - 12) / 6?", "3"),
    ("What is 36 divided by 6?", "6"),
    ("What is 42 - 15 + 6?", "33"),
    ("What is 7 * 4 - 2?", "26"),
    ("What is 24 / 6 + 4?", "8"),
    ("What is 10 squared?", "100"),
    ("What is the square root of 169?", "13"),
    ("What is 6 + 4 * 3?", "18"),
    ("What is (16 - 8) / 4?", "2"),
    ("What is 32 divided by 8?", "4"),
    ("What is 38 - 18 + 9?", "29"),
    ("What is 9 * 2 - 5?", "13"),
    ("What is 12 / 3 + 2?", "6"),
    ("What is 7 squared plus 2?", "51"),
    ("What is the square root of 121?", "11"),
    ("What is 5 + 3 * 2?", "11"),
    ("What is (14 - 7) / 3?", "2"),
    ("What is 18 divided by 9?", "2"),
    ("What is 23 - 10 + 5?", "18"),
    ("What is 8 * 3 - 6?", "18"),
    ("What is 30 / 6 + 3?", "8"),
    ("What is 11 squared?", "121"),
    ("What is the square root of 225?", "15"),
    ("What is 12 + 2 * 5?", "22"),
    ("What is (20 - 8) / 4?", "3"),
    ("What is 25 divided by 5?", "5"),
    ("What is 28 - 14 + 7?", "21"),
    ("What is 8 * 4 - 2?", "30"),
    ("What is 36 / 6 + 4?", "10"),
    ("What is 11 * 3 - 4?", "29"),
    ("What is 16 / 2 + 3?", "11"),
    ("What is 9 squared plus 3?", "84"),
    ("What is the square root of 144?", "12"),
    ("What is 6 + 3 * 4?", "18"),
    ("What is (18 - 9) / 3?", "3"),
    ("What is 27 divided by 3?", "9"),
    ("What is 32 - 12 + 6?", "26"),
    ("What is 10 * 3 - 5?", "25"),
    ("What is 15 / 5 + 2?", "5"),
    ("What is 7 squared plus 4?", "53"),
    ("What is the square root of 196?", "14"),
    ("What is 8 + 2 * 3?", "14"),
    ("What is (12 - 6) / 3?", "2"),
    ("What is 24 divided by 8?", "3"),
    ("What is 30 - 16 + 6?", "20"),
    ("What is 9 * 4 - 7?", "29"),
    ("What is 40 / 5 + 3?", "11"),
    ("What is 11 squared plus 1?", "122"),
    ("What is the square root of 169?", "13"),
    ("What is 6 + 5 * 2?", "16"),
    ("What is (15 - 6) / 3?", "3"),
    ("What is 20 divided by 10?", "2"),
    ("What is 22 - 12 + 5?", "15"),
]

def conduct_quiz(quiz):
    score = 0
    user_answers = []

    print("Welcome to the MathQuiz!")
    print()
    print("Grab your pen and paper and let's get solving!")
    print()
    print("Please type your answer and press Enter to submit.")

    
    for i, (question, answer) in enumerate(quiz, 1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ")

        # Check if the answer is correct
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

        user_answers.append((question, user_answer))

    print("\nQuiz completed!")
    print(f"You scored {score} out of {len(quiz)}")


    review_answers = input("Would you like to review your answers? (yes/no): ")
    if review_answers.lower() == "yes":
        print("\nReviewing your answers:")
        for i, (question, user_answer) in enumerate(user_answers, 1):
            print(f"\nQuestion {i}: {question}")
            print(f"Your answer: {user_answer}")

conduct_quiz(quiz)
