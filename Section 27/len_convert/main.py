import tkinter as tk

MILES_COEFFICIENT = 1.609344


def main():
    window = tk.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    # input for miles
    miles_val = tk.Entry()
    miles_label = tk.Label(text="Miles")

    miles_val.grid(column=1, row=0, padx=10, pady=10)
    miles_label.grid(column=2, row=0, padx=10, pady=10)

    # Second Row: Conversion
    equal_to = tk.Label(text="is equal to")
    km_val = tk.Label(text="0")
    km = tk.Label(text="Km")

    equal_to.grid(column=0, row=1, padx=10, pady=10)
    km_val.grid(column=1, row=1, padx=10, pady=10)
    km.grid(column=2, row=1, padx=10, pady=10)

    # Button
    btn = tk.Button(
        text="Calculate",
        command=lambda: convert(
            miles_val=miles_val.getdouble(miles_val.get()), km_label=km_val
        ),
    )
    btn.grid(column=1, row=2, padx=10, pady=10)

    window.mainloop()


def convert(km_label: tk.Label, miles_val: float):
    km_label.config(text=f"{miles_val * MILES_COEFFICIENT:.2f}")


if __name__ == "__main__":
    main()
