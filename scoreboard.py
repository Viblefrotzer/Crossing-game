from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.update()

    def new_level(self):
        global LEVEL
        LEVEL += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {LEVEL}", font=FONT, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Courier", 24, "bold"), align="center")
