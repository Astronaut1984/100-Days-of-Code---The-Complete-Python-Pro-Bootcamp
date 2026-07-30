import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizl")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = tk.Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 15, "normal"),
        )
        self.score_board.grid(column=1, row=0, sticky="NE")

        self.question = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.question.create_text(
            150,
            125,
            width=290,
            text="Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.question.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="./images/true.png")
        self.true = tk.Button(image=true_image, pady=20, command=self.check_if_true)
        self.true.grid(column=0, row=2)

        false_image = tk.PhotoImage(file="./images/false.png")
        self.false = tk.Button(image=false_image, pady=20, command=self.check_if_false)
        self.false.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=question_text)
        else:
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def update_score(self):
        self.score_board.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, right: bool):
        answers = {True: "green", False: "red"}
        self.question.config(bg=answers[right])
        self.window.after(1000, self.reset_question_field)

    def reset_question_field(self):
        self.question.config(bg="white")
        self.update_score()
        self.next_question()
