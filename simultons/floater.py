# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import math


class Floater(Prey): 
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x,y, 10, 10, random.random()*math.pi*2, 5)    
    
    def update(self,model):
        if random.random() <= 0.3:
            speed_change = random.random() - 0.5 
            angle_change = random.random() - 0.5
            self.set_velocity(self.get_speed() + speed_change if 3 <= self.get_speed() + speed_change <= 7 else self.get_speed(), 
                              self.get_angle() + angle_change)
        self.move()
        
    
    
    def display(self,canvas):
        x,y = self.get_location()
        canvas.create_oval(x-Floater.radius, y-Floater.radius,
                                x+Floater.radius, y+Floater.radius,
                                fill='#ff0000')
