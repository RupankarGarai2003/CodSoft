class QuizQuestion:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

def load_questions():
    questions = [
        QuizQuestion("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Rome"], "B"),
        QuizQuestion("What is 2 + 2?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
        QuizQuestion("What is the largest planet in our solar system?", ["A. Venus", "B. Mars", "C. Saturn", "D. Jupiter"], "D"),
        # QuizQuestion("What is the chemical symbol for gold?", ["A. Go", "B. Gd", "C. Au", "D. Ag"], "C"),
        # QuizQuestion("Which famous scientist developed the theory of relativity?", ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"], "B"),
        # QuizQuestion("Which gas do plants use for photosynthesis?", ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"], "B"),
        # QuizQuestion("What is the largest mammal?", ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"], "B"),
        # QuizQuestion("What is the tallest mountain in the world?", ["A. Mount Kilimanjaro", "B. Mount Everest", "C. Mount Fuji", "D. Mount McKinley"], "B"),
        # QuizQuestion("What is the currency of Japan?", ["A. Yen", "B. Won", "C. Rupee", "D. Dollar"], "A"),
        # QuizQuestion("Which famous playwright wrote Romeo and Juliet?", ["A. William Shakespeare", "B. Oscar Wilde", "C. George Bernard Shaw", "D. Samuel Beckett"], "A")
    ]
    return questions

def display_question(question, question_num):
    print(f"Question {question_num}: {question.question}")
    for choice in question.choices:
        print(choice)

def evaluate_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def main():
    print("Welcome to the Quiz Game!")
    print("Rules:")
    print("- You will be presented with multiple-choice questions.")
    print("- Choose the correct answer by typing the corresponding letter.")
    print("- Your final score will be displayed at the end.\n")

    questions = load_questions()
    total_questions = len(questions)
    score = 0

    for idx, question in enumerate(questions, start=1):
        display_question(question, idx)
        user_answer = input("Your answer: ")
        if evaluate_answer(user_answer, question.correct_choice):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question.correct_choice}.\n")

    print("Quiz completed!")
    print(f"Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    main()
    play_again = input("Do you want to play again? (yes/no): ")
    while play_again.lower() == "yes":
        main()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thank you for playing!")
