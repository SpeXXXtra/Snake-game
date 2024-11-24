from turtle import Turtle,Screen
itr =0
starting_postions = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    def create_snake(self):
            global itr
            for i in starting_postions:
                if itr ==0:
                    snake = Turtle(shape="turtle")
                    snake.pu()
                    snake.color("green")
                    snake.goto(i)
                    self.snake_body.append(snake)
                    itr+=1
                snake = Turtle(shape="square")
                snake.pu()
                snake.color("white")
                snake.goto(i)
                self.snake_body.append(snake)
    
    def extend(self):
        snake = Turtle(shape="square")
        snake.pu()
        snake.color("white")
        self.last = self.snake_body[-1].pos()
        snake.goto(self.last)
        self.snake_body.append(snake)
        
    def up(self):
        if self.head.heading()!= 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!= 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!= 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!= 180:
            self.head.setheading(0)
    def move_snake(self):
        for snake in range(len(self.snake_body)-1,0,-1):
            previous_snake = self.snake_body[snake-1].pos()
            self.snake_body[snake].goto(previous_snake)
        
        self.head.forward(MOVE_DISTANCE) 