from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've come to the end of the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")