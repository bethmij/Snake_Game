from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')
CENTER_FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.set_highest_score()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score : {self.score}   Highest Score : {self.highest_score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGN, font=CENTER_FONT)

    def refresh(self):
        self.score += 5
        self.update_score_board()

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_score_board()

        with open("highest_score_count", mode="w") as file:
            file.write(str(self.highest_score))

    def set_highest_score(self):
        with open("highest_score_count") as file:
            self.highest_score = int(file.readline())
