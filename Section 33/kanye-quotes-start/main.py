from tkinter import *
import requests as rq


def get_font_size(quote_len, min_size=14, max_size=40, base_len=65, base_size=30):
    font_size = (base_size * base_len) // max(quote_len, 1)
    return max(min_size, min(max_size, font_size))


def get_quote():
    response = rq.get("https://api.kanye.rest/").json()
    quote = response["quote"]
    font_size = get_font_size(len(quote))
    canvas.itemconfig(quote_text, text=quote, font=("Arial", font_size, "bold"))
    pass


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
