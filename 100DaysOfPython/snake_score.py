from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.hideturtle()
        self.set_score()

    def set_score(self):
        self.write(f"Score: {self.SCORE}", align='center', font=('Arial', 16, 'normal'))
        self.setposition(0, 260)
        self.color("grey")

    def add_point(self):
        self.clear()
        self.SCORE += 1
        self.set_score()
        return self

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 24, 'normal'))


