from turtle import Turtle

FONT = ("Arial",15,"normal")
ALIGNMENT = "center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.write(arg=f"Score : {self.score}", move=False,align=ALIGNMENT, font=FONT)

    def update(self):
        self.write(arg=f"Score : {self.score}", move=False,align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center",font=("Monospaced", 20, "normal"))

