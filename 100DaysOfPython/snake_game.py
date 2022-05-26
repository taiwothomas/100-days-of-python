from turtle import Screen
from snake import Snake
from food import Food
from snake_score import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
score.set_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_point()
        snake.grow()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.switch_side()

    for vert in snake.snake[1:]:
        # if vert == snake.head:
        #     pass
        if snake.head.distance(vert) < 10:
            score.game_over()
            game_is_on = False



screen.exitonclick()
