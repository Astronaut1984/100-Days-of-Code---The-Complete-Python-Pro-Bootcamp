from question_model import Question


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list: list[Question] = question_bank

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)
        self.print_score()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct):
        if answer.strip().lower() == correct.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer is: {correct}")

    def print_score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
