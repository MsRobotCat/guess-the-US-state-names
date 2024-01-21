import turtle
import pandas as pd
from names_on_image import NameTag
from display import Display

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
display = Display()

game_is_on = True
while game_is_on:

    display.check_game_over()
    if display.num_guesses <= 0:
        game_is_on = False
        break

    answer_state = display.get_answer().title()
    display.update_num_guesses()

    if answer_state in all_states:
        x_cor = data[data.state == answer_state].iloc[0]['x']
        y_cor = data[data.state == answer_state].iloc[0]['y']
        name_tag = NameTag(answer_state, x_cor, y_cor)
        display.update_score()
        display.check_complete_score()
        if display.score >= display.full_score:
            game_is_on = False



turtle.mainloop()