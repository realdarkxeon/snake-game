from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_data(str(self.high_score))
        self.score = -1
        self.increment()

    def save_data(self, high_score):
        with open("data.txt", mode="r") as file:
            contents = file.read()

        with open("data.txt", mode="w") as file:
            if int(high_score) > int(contents):
                file.write(high_score)