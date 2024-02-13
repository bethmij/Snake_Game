from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGN, font=FONT)

    def refresh(self):
        self.score += 1
        self.update_score_board()
