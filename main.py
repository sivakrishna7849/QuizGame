from question_bank import QuestionBrain

from data import question_bank
from question import Question
question_bank1 = []
for i in question_bank:
    question_bank1.append(Question(i["category"],i["type"],i["difficulty"],i["question"],i["correct_answer"]))
quiz=QuestionBrain(question_bank1)
while(quiz.question_still_there()):
    quiz.ques()
print("All the questions have ended")