"""
This is claude's version implemented using OOP principles, it serves as an example of why OOP is better than functional programming in GUI applications.
"""

import tkinter as tk
import pandas as pd
from pathlib import Path
import random as rng

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
CARD_FLIP_DELAY_MS = 3000

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_FILE = DATA_DIR / "french_words.csv"
WORDS_TO_LEARN_FILE = DATA_DIR / "words_to_learn.csv"

IMAGE_DIR = Path(__file__).resolve().parent / "images"


class WordBank:
    """Owns the list of words still to learn: loading, saving, and picking."""

    def __init__(self, data_file: Path, progress_file: Path):
        self.data_file = data_file
        self.progress_file = progress_file
        self.words: list[dict] = []
        self.current_word: dict | None = None
        self.load()

    def load(self):
        source = self.progress_file if self.progress_file.exists() else self.data_file
        self.words = pd.read_csv(source).to_dict(orient="records")

    def save(self):
        pd.DataFrame(self.words, columns=["French", "English"]).to_csv(
            self.progress_file, index=False
        )

    @property
    def is_empty(self) -> bool:
        return not self.words

    def pick_next(self) -> dict | None:
        if self.is_empty:
            self.current_word = None
            return None
        self.current_word = rng.choice(self.words)
        return self.current_word

    def mark_known(self):
        """Remove the current word for good and persist progress."""
        if self.current_word in self.words:
            self.words.remove(self.current_word)
            self.save()


class FlashCardApp:
    """Owns the window, canvas, images, and the flip timer."""

    def __init__(self, word_bank: WordBank):
        self.word_bank = word_bank
        self.timer: str | None = None

        self.window = tk.Tk()
        self.window.title("Flashy")
        self.window.config(bg=BACKGROUND_COLOR, width=900, height=800, padx=50, pady=50)

        # Images must be kept as attributes or Tkinter garbage-collects them
        self.front_image = tk.PhotoImage(file=str(IMAGE_DIR / "card_front.png"))
        self.back_image = tk.PhotoImage(file=str(IMAGE_DIR / "card_back.png"))
        self.wrong_image = tk.PhotoImage(file=str(IMAGE_DIR / "wrong.png"))
        self.right_image = tk.PhotoImage(file=str(IMAGE_DIR / "right.png"))

        self._build_canvas()
        self._build_buttons()

        self.next_word()

    def _build_canvas(self):
        self.canvas = tk.Canvas(
            width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR
        )
        self.flash_card_image = self.canvas.create_image(
            400, 263, image=self.front_image
        )
        self.title_text = self.canvas.create_text(
            400, 150, text="French", font=TITLE_FONT
        )
        self.word_text = self.canvas.create_text(400, 263, text="Word", font=WORD_FONT)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def _build_buttons(self):
        wrong_button = tk.Button(
            image=self.wrong_image,
            highlightthickness=0,
            background=BACKGROUND_COLOR,
            command=self.next_word,
        )
        right_button = tk.Button(
            image=self.right_image,
            highlightthickness=0,
            background=BACKGROUND_COLOR,
            command=self.know_word,
        )
        wrong_button.grid(row=1, column=0)
        right_button.grid(row=1, column=1)

    def next_word(self):
        if self.timer:
            self.window.after_cancel(self.timer)

        word = self.word_bank.pick_next()
        if word is None:
            self.canvas.itemconfigure(
                self.word_text, text="No more words", fill="black"
            )
            self.canvas.itemconfigure(self.title_text, text="Done", fill="black")
            self.canvas.itemconfigure(self.flash_card_image, image=self.front_image)
            return

        self.canvas.itemconfigure(self.word_text, text=word["French"], fill="black")
        self.canvas.itemconfigure(self.title_text, text="French", fill="black")
        self.canvas.itemconfigure(self.flash_card_image, image=self.front_image)

        self.timer = self.window.after(
            CARD_FLIP_DELAY_MS, self.show_translation, word["English"]
        )

    def know_word(self):
        self.word_bank.mark_known()
        self.next_word()

    def show_translation(self, translation: str):
        self.canvas.itemconfigure(self.flash_card_image, image=self.back_image)
        self.canvas.itemconfigure(self.title_text, text="English", fill="white")
        self.canvas.itemconfigure(self.word_text, text=translation, fill="white")

    def run(self):
        self.window.mainloop()


def main():
    word_bank = WordBank(DATA_FILE, WORDS_TO_LEARN_FILE)
    app = FlashCardApp(word_bank)
    app.run()


if __name__ == "__main__":
    main()
