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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(arg=f"Score : {self.score}  High Score: {self.high_score}", move=False,align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score: {self.high_score}", move=False,align=ALIGNMENT, font=FONT)

    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
        self.write(arg=f"Score : {self.score}  High Score: {self.high_score}", move=False,align=ALIGNMENT, font=FONT)


    def gameover(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center",font=("Monospaced", 20, "normal"))

