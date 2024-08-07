import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_answer"] = user_choice
    if question["user_answer"] == question["correct_answer"]:
        score += 1

print("-"*20)
print(f"Your score is {score} / {len(data)}")
for question in data:
    message = f"Your answer: {question['user_answer']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)
