import random

# List of questions, options, and answers
questions = [
    {
        "question": "Who is the current Prime Minister of India?",
        "options": ["A) Narendra Modi", "B) Rahul Gandhi", "C) Manmohan Singh", "D) Arvind Kejriwal"],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Lisbon"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the epic Mahabharata?",
        "options": ["A) Valmiki", "B) Ved Vyas", "C) Kalidas", "D) Tulsidas"],
        "answer": "B"
    },
    {
        "question": "Which is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "answer": "B"
    }
]

# Game function
def kbc_game():
    print("Welcome to Kaun Banega Crorepati!\n")
    score = 0
    question_number = 1
    
    random.shuffle(questions)  # Randomize the question order

    for q in questions:
        print(f"Question {question_number}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get the user's answer
        answer = input("\nYour answer (A, B, C, or D): ").upper()
        
        # Check if the answer is correct
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}\n")

        question_number += 1

    # Final score
    print(f"Game Over! Your final score is: {score}/{len(questions)}")

# Start the game
if __name__ == "__main__":
    kbc_game()
