import turtle as tr
import pandas as pd

NUM_STATES = 50
FONT = ("roboto", 7, "bold")


def write_state(x, y, state):
    tim = tr.Turtle()
    tim.hideturtle()
    tim.teleport(x, y)
    tim.write(arg=state, align="center", font=FONT)


def main():

    # Setup Screen
    screen = tr.Screen()
    screen.title("US States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    tr.shape(image)

    # Setup Data
    states_df = pd.read_csv("50_states.csv")

    answers = []
    i = 0
    correct = 0
    while i < NUM_STATES:
        title = f"{correct} / 50 Correct" if i > 0 else "Guess the state"
        answer = screen.textinput(title=title, prompt="Enter a state")

        if answer in states_df.state.values:
            if answer not in answers:
                x = states_df[states_df.state == answer].x.item()
                y = states_df[states_df.state == answer].y.item()
                write_state(x, y, answer)
                answers.append(answer)
                i += 1
                correct += 1
            else:
                print("Already Guessed")
                tr.TK.messagebox.showinfo(
                    title="Already Guessed",
                    message="You have already guessed this state",
                )
        else:
            i += 1

    screen.mainloop()


if __name__ == "__main__":
    main()
