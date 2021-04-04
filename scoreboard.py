from turtle import Turtle

TOP = 0
MIDDLE = 260
ALIGNMENT = 'CENTER'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=TOP, y=MIDDLE)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
