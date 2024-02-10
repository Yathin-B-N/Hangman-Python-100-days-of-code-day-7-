class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_q(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q. {self.question_number} : {curr_question.text} (True/False):")
        self.check_ans(user_ans,curr_question.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you got it right")
            self.score += 1
        else:
            print("you got in wrong")
        print("the correct answer was:", correct_ans)
        print(f"your curr score is : {self.score}/{self.question_number}")
        print('\n')

