from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
WIDTH = 600
HEIGHT = 600
X_BOUND = (WIDTH / 2) - 10
Y_BOUND = (HEIGHT / 2) - 10

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
level = screen.textinput(title='Level', prompt='Enter your level (easy, medium, hard):')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard(HEIGHT)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Difficulty option as dictionary
difficulty = {
    "hard": 0.05,
    "medium": 0.1,
    "easy": 0.12
}

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(difficulty[level])

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if (snake.head.xcor() > X_BOUND or snake.head.xcor() < - X_BOUND or
            snake.head.ycor() > Y_BOUND or snake.head.ycor() < -Y_BOUND):
        print(snake.head.position())
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
