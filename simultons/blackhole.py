# Black_Hole inherits from only Simulton, updating by finding/removing
#   any Prey-derived class whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def update(self,model):
        found = model.find(lambda s: isinstance(s, Prey) and self.contains(s.get_location()))
        model.garbage.update(found)
        return found
                
        
    def display(self,canvas):
        x,y = self.get_location()
        w,h = self.get_dimension()
        canvas.create_oval(x - (w / 2), y - (h / 2), x + (w / 2), y + (h / 2), fill='#000000')
    
    def contains(self, xy):
        return ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5 < self.get_dimension()[0] / 2
