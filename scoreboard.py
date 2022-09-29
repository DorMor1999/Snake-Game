from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.goto(0, 270)
        self.update_score_board()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score_board()

    def save_high_score(self):
        with open("high_score_file.txt", mode="w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open("high_score_file.txt") as file:
            return int(file.read())