from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for i in question_data:
    text = i["text"]
    ans = i["answer"]
    new_question = Question(text, ans)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
while quiz.still_has_q():
    quiz.next_question()
print("you have completed")
print(f"your final score was : {quiz.score}/{len(question_bank)} ")
