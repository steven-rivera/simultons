# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from simultons.blackhole import Black_Hole


class Pulsator(Black_Hole): 
    hunger = 30
    
    def __init__(self, x, y):
        self.counter = 0
        Black_Hole.__init__(self, x, y)
        
    def update(self,model):
        s = Black_Hole.update(self, model)
        
        if len(s) == 0:
            self.counter += 1
            if self.counter == Pulsator.hunger:
                w,h = self.get_dimension()
                if w == 1 and h == 1:
                    model.garbage.add(self)
                else:    
                    self.set_dimension(w-1, h-1)
                    self.counter = 0
        else:
            self.counter = 0
            for _ in range(len(s)):
                w,h = self.get_dimension()
                self.set_dimension(w+1, h+1)
    
    def display(self,canvas):
        x,y = self.get_location()
        w,h = self.get_dimension()
        canvas.create_oval(x - (w / 2), y - (h / 2), x + (w / 2), y + (h / 2), fill='#00FF00')
                     
    