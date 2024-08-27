def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
            "answer": "A"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"],
            "answer": "C"
        }
    ]

    # Define the prize money for each question
    prize_money = [1000, 2000, 3000, 5000, 10000]

    total_amount = 0

    for i, q in enumerate(questions):
        # Display the question and options
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get the user's answer
        user_answer = input("Choose your answer (A, B, C, or D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == q['answer']:
            total_amount += prize_money[i]
            print(f"Correct! You've won ${prize_money[i]}.")
        else:
            print(f"Incorrect. The correct answer was '{q['answer']}'.")
            break

    # Display the final amount
    print(f"Game over. You are taking home ${total_amount}.")

if __name__ == "__main__":
    main()
