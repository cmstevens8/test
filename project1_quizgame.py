quiz = [
    {
        "question": "Which movie is this AI character from: HAL 9000?",
        "options": ["I, Robot", "Ex Machina", "2001: A Space Odyssey", "The Matrix"],
        "answer": "2001: A Space Odyssey"
    },
    {
        "question": "Who voiced the character of Samantha in 'Her'?",
        "options": ["Meryl Streep", "Emma Stone", "Natalie Portman", "Scarlett Johansson"],
        "answer": "Scarlett Johansson"
    },
    {
        "question": "Which AI character said the line: 'I’ll be back.'?",
        "options": ["The Terminator", "C-3PO", "V.I.K.I.", "R2-D2"],
        "answer": "The Terminator"
    },
    {
        "question": "Which AI character is known for saying, 'I find your lack of faith disturbing.'?",
        "options": ["Agent Smith", "Darth Vader", "V.I.K.I.", "HAL 9000"],
        "answer": "Darth Vader"
    },
    {
        "question": "Which movie features the AI character named 'Samantha'?",
        "options": ["The Matrix", "Blade Runner", "Her", "Ex Machina"],
        "answer": "Her"
    },
    {
        "question": "Who is the AI character in 'Ex Machina' that questions human consciousness?",
        "options": ["Samantha", "Ava", "V.I.K.I.", "C-3PO"],
        "answer": "Ava"
    }
]
score = 0
correct_answers = []
incorrect_answers = []

for q in quiz:
    question = q["question"]
    choices = q["options"]


    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    print()
    answer = input("Enter the number of your answer: ")
    
    print(f"You chose: {choices[int(answer) - 1]}\n")
    if choices[int(answer) - 1] == q["answer"]:
        score += 1
        correct_answers.append(q["question"])
    else:
        incorrect_answers.append({
            "question": q["question"],
            "user_answer": choices[int(answer) - 1],
            "correct_answer": q["answer"]
    }) 
def add_question():
    question = input("Enter your question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {i+1}: ")
        options.append(option)
    
    answer = input("Enter the correct answer: ")
    
    new_question = {
        "question": question,
        "options": options,
        "answer": answer
    }
    
    quiz.append(new_question)
    print("New question added successfully!")

print(f"Your score is {score}/{len(quiz)}") 

print("\nYour correct answers:")
for answer in correct_answers:
    print(f"- {answer}")

print("\nYour incorrect answers:")
for answer in incorrect_answers:
    print(f"- {answer['question']} (You chose: {answer['user_answer']}, Correct answer: {answer['correct_answer']})")

add_more = input("Would you like to add a new question? (yes/no): ")
if add_more.lower() == "yes":
    add_question()