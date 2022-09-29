import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score_Board

#create screen
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("#1E90FF")
screen.title("Snake Game")

#create snake
snake = Snake()

#create food
food = Food()

#create score board
score_board = Score_Board()

#moving options
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
    #Detect collision with food.
    if snake.snake_parts[0].distance(food.xcor(), food.ycor()) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    ##Detect collision with wall.
    if snake.snake_parts[0].xcor() > 290 or snake.snake_parts[0].xcor() < -290 or snake.snake_parts[0].ycor() > 290 or\
            snake.snake_parts[0].ycor() < -290:
        score_board.reset()
        snake.reset()
    ##Detect collision with tail.
    for part in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(part) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
