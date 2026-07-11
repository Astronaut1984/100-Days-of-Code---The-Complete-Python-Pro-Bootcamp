import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
padding = {
    "pady": (0, 10),
}
timer_fun = None
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    window.after_cancel(timer_fun)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer.config(fg=RED, text="Break")
        count_down(int(LONG_BREAK_MIN * 60))
        return
    if REPS % 2 == 1:
        timer.config(fg=GREEN, text="Work")
        count_down(int(WORK_MIN * 60))
    else:
        timer.config(fg=PINK, text="Break")
        count_down(int(SHORT_BREAK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer_fun
    if count < 0:
        start_timer()
        global REPS
        checks = ""
        for _ in range(math.floor(REPS / 2)):
            checks += "✔"
        check_mark.config(text=checks)
        return
    mins, secs = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{mins:02d}:{secs:02d}")
    timer_fun = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
timer = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.grid(row=0, column=1, **padding)

# Tomato Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1, **padding)

# Start and Reset button
start_btn = tk.Button(text="Start", command=start_timer)
reset_btn = tk.Button(text="Reset", command=reset_timer)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

# Checkmark label
check_mark = tk.Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
