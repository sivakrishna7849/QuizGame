class QuestionBrain():
    def __init__(self,qlist):
        self.question_number=0
        self.question_list=qlist
        self.score=0

    def check_answer(self,answer,ans):
        if(answer==ans):
            self.score+=1
            print("That's Right!")
        else:
            print("That's Wrong!")
        print(f"Your score is {self.score}/{self.question_number}")
        print(f"The right answer is {ans}")
        print("\n")
    def ques(self):
        ques1=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q {self.question_number}. {ques1.qtext} (True/False)(Difficulty:{ques1.qdifficulty}) (Category:{ques1.qcategory}):  ")
        self.check_answer(answer,ques1.qans)



    def question_still_there(self):
        return self.question_number < len(self.question_list)
