class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number].question
        correct_answer = self.question_list[self.question_number].answer

        user_answer = input(f"Q.{self.question_number+1}: {current_question} (True/False)?: ")
        self.question_number += 1

        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is correct!")
            self.score += 1
        else:
            print(f"Your answer is wrong. The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print()