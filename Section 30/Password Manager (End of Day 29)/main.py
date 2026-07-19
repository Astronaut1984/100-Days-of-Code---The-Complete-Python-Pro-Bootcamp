import tkinter as tk
from tkinter import messagebox
from os import SEEK_END
import random
import json
from json.decoder import JSONDecodeError

FONT = ("Roboto", 14, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(index=0, string=password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    entry = {website: {"email": email, "password": password}}

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showerror(
            title="Empty Fields",
            message="Some fields were left empty, please fill them",
        )
        return
    data = None
    try:
        with open("data.json", "+r") as f:
            data = json.load(f)
            data.update(entry)
    except FileNotFoundError:
        with open("data.json", "w+") as f:
            json.dump(entry, f, indent=2)
    else:
        with open("data.json", "+w") as f:
            json.dump(data, f, indent=2)
    finally:
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- Search Functionality ------------------------------- #
def search():
    try:
        with open("data.json", "r+") as f:
            data = json.load(f)
            try:
                entry = data[website_entry.get()]
            except KeyError:
                messagebox.showerror(
                    title="Not Found",
                    message="No email or password was found for this website",
                )
            else:
                email = entry["email"]
                password = entry["password"]
                messagebox.showinfo(
                    title=f"{website_entry.get()}",
                    message=f"Email: {email}\nPassword: {password}",
                )
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Logo
pass_image_canvas = tk.Canvas(width=200, height=200)
pass_logo = tk.PhotoImage(file="logo.png")
pass_image_canvas.create_image(100, 100, image=pass_logo)
pass_image_canvas.grid(column=1, row=0)

# Website Entry
website_label = tk.Label(text="Website: ", font=FONT)
website_entry = tk.Entry()
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, sticky="EW", padx=(0, 5))

# Search Button
search_button = tk.Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

# Email/Username
user_label = tk.Label(text="Email/Username: ", font=FONT)
user_entry = tk.Entry()
user_entry.insert(index=0, string="g@e.com")
user_label.grid(column=0, row=2)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password
password_label = tk.Label(text="Password: ", font=FONT)
password_entry = tk.Entry()
generate_button = tk.Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, sticky="EW", padx=(0, 5))
generate_button.grid(column=2, row=3, sticky="EW")

# Add Button
add_button = tk.Button(text="Add", width=35, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
