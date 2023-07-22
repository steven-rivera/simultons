#Special is the anti-matter of Prey; acts like a ball 
#but annihilates itself and Prey when they come 
#into contact with each other 
 
from prey import Prey
import random
from math import pi


class Special(Prey): 
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, random.random()*pi*2, 5)    
    
    def update(self,model):
        bounce = model.find(lambda s: isinstance(s, Prey) and not isinstance(s, Special) and self.distance(s.get_location()) < 10)
        
        if len(bounce) != 0:
            bounce.add(self)
            model.garbage.update(bounce)
            
        self.move()
        
    
    def display(self,canvas):
        x,y = self.get_location()
        canvas.create_oval(x-Special.radius, y-Special.radius,
                                x+Special.radius, y+Special.radius,
                                fill='#ff9d00')
    