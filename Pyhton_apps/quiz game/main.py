from question_model import question
from data import question_data
from quiz_brain import quizbrain
question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer =item["answer"]
    new_question = question(question_text,question_answer)
    question_bank.append(new_question)
quiz = quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You completed the quiz")
print(f"Your final score is : {quiz.current_score}/{quiz.question_number}")   