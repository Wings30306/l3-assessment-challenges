"""
Quiz
"""

questions = [{
    "question": "What is the capital of Spain?",
    "answers": [
        "Dublin",
        "Buenos Aires",
        "Madrid",
        "San Juan"
    ],
    "correctIndex": 2
}, {
    "question": "What is the capital of Argentina?",
    "answers": [
        "Dublin",
        "Buenos Aires",
        "Madrid",
        "San Juan"
    ],
    "correctIndex": 1
}, {
    "question": "What is the capital of Ireland?",
    "answers": [
        "Dublin",
        "Buenos Aires",
        "Madrid",
        "San Juan"
    ],
    "correctIndex": 0
}]


def quiz(score)
    """
    Play quiz:
    - get user's name
    - trigger the ask_question function
    - print result when every question has been asked
    """
    name = input("Hello, what is your name? ")
    print(f"Hi {username}! Welcome to the quiz. Good luck!")
    for question_dict in questions:
        score = ask_question(question_dict, score)
    print(f"{name}, you scored {score} out of {len(questions)}")


def ask_question(dictionary, score):
    """
    Ask question:
    - display question
    - display answers
    - check answer
    - give feedback
    - update score
    - return score to pass back to quiz function for next iteration
    """
    print(dictionary["question"])
    answer_number = 1
    for answer in dictionary["answers"]:
        print(f"{answer_number} {answer}")
        answer_number += 1
    user_answer = input("Your answer (please enter a number): ")
    if user_answer - 1 == dictionary["correctIndex"]:
        print("Well done, that was the correct answer!")
    esle:
        print("Sorry, that was not the correct answer.")
        score += 1
    return score


quiz(0)
