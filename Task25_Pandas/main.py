import turtle
import pandas

USA_STATES_NUMBER = 50

# States with a turtle screen and guess which one are known

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

guessed_states = []

# Change screen to the image shape
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

states_guessed = 0
missing_states = []


def write_state():
    new_state = turtle.Turtle("square")
    new_state.hideturtle()
    new_state.color("black")
    new_state.penup()
    # It is needed to use the .item() to wrap the first element
    new_state.goto(int(state_data.x.item()), int(state_data.y.item()))
    new_state.write(state_data.state.item(), font=("Courier", 10, "normal"))


# Keep going until all are guessed
while states_guessed < USA_STATES_NUMBER:
    # Pop up boxes
    answer_state = screen.textinput(title=f"{states_guessed}/{USA_STATES_NUMBER} guessed USA states",
                                    prompt="Write the name of a state")

    # Check if user wants to exit
    if answer_state.lower() == "exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                # States missing added into a file
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("missing_countries.csv")
        break

    # Check if the state is found
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # Save data of the guessed state
        state_data = data[data.state == answer_state]
        # Write the guess in the map
        write_state()
        states_guessed += 1
    else:
        print("This is not the name of a country")


# Keep the window forever
turtle.mainloop()
