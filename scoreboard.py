from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.points =0
        self.color("White")
        self.sety(270)
        self.write(f"Score:{self.points}", align=ALIGNMENT, font=FONT)
    
    def update(self):
        self.points+=1
        self.clear()
        self.write(f"Score:{self.points}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        
        self.gameover = Turtle()
        self.gameover.color("white")
        self.gameover.write(f"GAMEOVER!!!", align=ALIGNMENT, font=FONT)
        