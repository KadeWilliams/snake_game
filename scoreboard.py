from turtle import Turtle

TOP = 0
MIDDLE = 260
ALIGNMENT = 'CENTER'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=TOP, y=MIDDLE)
        self.score = 0
        with open('high_score.txt') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
