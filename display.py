from turtle import Screen, Turtle
FULL_SCORE = 50
GUESS_LIMIT = 55

class Display(object):
    def __init__(self):
        self.full_score = FULL_SCORE
        self.score = 0
        self.num_guesses = GUESS_LIMIT
        self.display = Screen()

    # create a dialogue box to ask user to guess
    def get_answer(self):
        return self.display.textinput(title=f"{self.score}/{self.full_score} states correct. You have {self.num_guesses} guesses left", prompt="Enter a state's name")

    def update_score(self):
        self.score += 1

    # increase the score of user when they guess correctly
    def update_num_guesses(self):
        self.num_guesses -= 1

    #check if the user has guessed all the states
    def check_complete_score(self):
        if self.score >= self.full_score:
            display = Turtle()
            display.hideturtle()
            display.goto(0,0)
            display.write("Well done!", align="center", font=("Arial", 50, "bold"))

    # setting the number of times that the user can input. If user has guessed too many times, then game over.
    def check_game_over(self):
        if self.num_guesses <= 0:
            display = Turtle()
            display.hideturtle()
            display.goto(0,0)
            display.write("Game Over", align="center", font=("Arial", 30, "bold"))