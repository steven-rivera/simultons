# Hunter inherits from the Pulsator (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import random, math

class Hunter(Pulsator, Mobile_Simulton):
    vision = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, random.random()*math.pi*2, 5)
    
    
    def update(self, model):
        Pulsator.update(self, model)
        target = model.find(lambda s: isinstance(s, Prey) and self.distance(s.get_location()) <= Hunter.vision)
        
        if len(target) != 0:
            distance = None
            for s in target:
                if distance != None:
                    if self.distance(s.get_location()) < distance:
                        prey = s
                        distance = self.distance(s.get_location()) 
                else:
                    prey = s
                    distance = self.distance(s.get_location())
            
            prey_x, prey_y = prey.get_location()
            x, y = self.get_location()
            dif_x, dif_y = prey_x - x, prey_y - y
            
            self.set_angle(atan2(dif_y, dif_x))
        
        self.move()
                    
