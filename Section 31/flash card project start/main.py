import tkinter as tk
import pandas as pd
from pathlib import Path
from pprint import pprint
import random as rng

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

DATA = []
CURRENT_WORD = {}
timer = None
window = tk.Tk("Flashy")
DATA_FILE = Path(__file__).resolve().parent / "data" / "french_words.csv"
WORDS_TO_LEARN_FILE = Path(__file__).resolve().parent / "data" / "words_to_learn.csv"


def load_words():
    global DATA
    if WORDS_TO_LEARN_FILE.exists():
        DATA = pd.read_csv(WORDS_TO_LEARN_FILE).to_dict(orient="records")
    else:
        DATA = pd.read_csv(DATA_FILE).to_dict(orient="records")
    pprint(DATA)


def save_words():
    global DATA
    columns = ["French", "English"]
    pd.DataFrame(DATA, columns=columns).to_csv(WORDS_TO_LEARN_FILE, index=False)


def show_translation(*args):
    canvas, title_text, word_text, flash_card_image, translation, back_image = args
    canvas.itemconfigure(flash_card_image, image=back_image)
    canvas.itemconfigure(title_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=translation, fill="white")
    pass


def next_word(**kwargs):
    global timer
    global window
    global CURRENT_WORD
    if not DATA:
        canvas = kwargs["canvas"]
        word_text = kwargs["word_text"]
        title_text = kwargs["title_text"]
        flash_card_image = kwargs["flash_card_image"]
        canvas.itemconfigure(word_text, text="No more words", fill="black")
        canvas.itemconfigure(title_text, text="Done", fill="black")
        canvas.itemconfigure(flash_card_image, image=kwargs["front_image"])
        return

    word = rng.choice(DATA)
    CURRENT_WORD = word
    canvas = kwargs["canvas"]
    word_text = kwargs["word_text"]
    title_text = kwargs["title_text"]
    front_image = kwargs["front_image"]
    back_image = kwargs["back_image"]
    flash_card_image = kwargs["flash_card_image"]

    canvas.itemconfigure(word_text, text=word["French"], fill="black")
    canvas.itemconfigure(title_text, text="French", fill="black")
    canvas.itemconfigure(flash_card_image, image=front_image)
    if timer:
        window.after_cancel(timer)
    timer = window.after(
        3000,
        show_translation,
        canvas,
        title_text,
        word_text,
        flash_card_image,
        word["English"],
        back_image,
    )


def know_word(**kwargs):
    global DATA
    global CURRENT_WORD
    if CURRENT_WORD in DATA:
        DATA.remove(CURRENT_WORD)
        save_words()
    next_word(**kwargs)


def main():
    # Load Words CSV
    load_words()

    # Config window
    global window
    window.config(bg=BACKGROUND_COLOR, width=900, height=800, padx=50, pady=50)

    # Flashcard
    flash_card_canvas = tk.Canvas(
        width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR
    )
    front_image = tk.PhotoImage(file="./images/card_front.png")
    back_image = tk.PhotoImage(file="./images/card_back.png")
    flash_card_image = flash_card_canvas.create_image(400, 263, image=front_image)
    title_text = flash_card_canvas.create_text(400, 150, text="French", font=TITLE_FONT)
    word_text = flash_card_canvas.create_text(400, 263, text="Word", font=WORD_FONT)
    next_word(
        canvas=flash_card_canvas,
        word_text=word_text,
        title_text=title_text,
        flash_card_image=flash_card_image,
        front_image=front_image,
        back_image=back_image,
    )
    flash_card_canvas.grid(row=0, column=0, columnspan=2)

    # Button
    wrong_image = tk.PhotoImage(file="./images/wrong.png")
    right_image = tk.PhotoImage(file="./images/right.png")
    wrong_button = tk.Button(
        image=wrong_image,
        highlightthickness=0,
        background=BACKGROUND_COLOR,
        command=lambda: next_word(
            canvas=flash_card_canvas,
            word_text=word_text,
            title_text=title_text,
            flash_card_image=flash_card_image,
            front_image=front_image,
            back_image=back_image,
        ),
    )
    right_button = tk.Button(
        image=right_image,
        highlightthickness=0,
        background=BACKGROUND_COLOR,
        command=lambda: know_word(
            canvas=flash_card_canvas,
            word_text=word_text,
            title_text=title_text,
            flash_card_image=flash_card_image,
            front_image=front_image,
            back_image=back_image,
        ),
    )

    wrong_button.grid(row=1, column=0)
    right_button.grid(row=1, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
