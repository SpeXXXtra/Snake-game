from turtle import Turtle
import random as rm
class Food(Turtle):#inheriting the turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)#halfing the size of the circle
        self.color("red")
        self.speed(11)#fastest speed 
        self.goto(x=rm.randint(-265,265),y=rm.randint(-265,265))
    
    def new_location(self):
        self.goto(x=rm.randint(-265,265),y=rm.randint(-265,265))