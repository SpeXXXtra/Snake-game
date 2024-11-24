from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

#event listenrs to control the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on =True

while game_is_on:
    #movement of the snake
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    #collison check with food
    if snake.head.distance(food) <15: #15 because the food is 10X10 so it is a buffer
        food.new_location()
        score.update()
        snake.extend()
    
    #collision with wall
    if snake.head.xcor() >288 or snake.head.ycor() >288 or snake.head.xcor()<-288 or snake.head.ycor()<-288:
        game_is_on = False
        score.game_over()
        
    #detect collison with snake body
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            score.game_over()
        
#close the window when the game is over
screen.exitonclick()