import tkinter as tk


def main():
    window = tk.Tk()

    window.title("This is how to set up the title")
    window.minsize(width=600, height=600)
    window.config(padx=40, pady=40)

    # This will show a label
    label = tk.Label(text="Original Text", font=("Consolas", 24, "bold"))
    label.grid(
        column=0, row=0
    )  # This will put the label at the center of the screen by default, but we can specify the side which we want the element to be shown

    # label.config(text="New") # We can change the values of the attributes in the element using config or square_notation['attr']

    button = tk.Button(text="Hello", command=lambda: click(label=label, input=input))
    button.grid(column=1, row=1)

    button2 = tk.Button(
        text="Hello V2.0", command=lambda: click(label=label, input=input)
    )
    button2.grid(column=2, row=0)

    input = tk.Entry(width=30)
    input.grid(column=3, row=2)

    # This is always at the end of the program
    window.mainloop()


def click(label: tk.Label, input: tk.Entry):
    label.config(text=input.get())


if __name__ == "__main__":
    main()
