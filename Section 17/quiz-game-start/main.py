import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def main():
  question_bank = [Question(question["text"], question["answer"]) for question in question_data]
  random.shuffle(question_bank)
  quiz = QuizBrain(question_bank)
  while quiz.still_has_questions():
    quiz.next_question()
  print("You've completed the quiz")
  print(f"Your final score is {quiz.score} / {quiz.question_number}")

if __name__ == "__main__":
  main()