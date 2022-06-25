import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Welcome to the 90's Snake Game")
screen.tracer(0)

pissy = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(pissy.up,"Up")
screen.onkey(pissy.down,"Down")
screen.onkey(pissy.left,"Left")
screen.onkey(pissy.right,"Right")

game_over = False

while not game_over:
    time.sleep(0.05)
    screen.update()
    pissy.move()
    if(pissy.head.distance(food) < 15):
        food.generate()
        score.score += 1
        score.update()
        pissy.extend()
    if(pissy.head.xcor() > 290 or pissy.head.xcor() < -290 or pissy.head.ycor() > 290 or pissy.head.ycor() < -290 ):
        score.reset()
        pissy.reset()

    for seg in pissy.segments[1:]:
        if(pissy.head.distance(seg) < 10):
            score.reset()
            pissy.reset()













screen.exitonclick()