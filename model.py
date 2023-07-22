import controller
import model   # Use to pass a reference to this module when calling update in update_all

#Use the reference to this module to pass it to update methods

from simultons.ball      import Ball
from simultons.floater   import Floater
from simultons.blackhole import Black_Hole
from simultons.pulsator  import Pulsator
from simultons.hunter    import Hunter
from simultons.special   import Special 


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
simultons   = set()
garbage     = set()
simulton_selected = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons   = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    running = False

    cycle_count += 1
    for simulton in simultons:
        simulton.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global simulton_selected
    simulton_selected = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if simulton_selected == 'Remove':     
        remove(find(lambda s : s.distance((x,y)) <= s.get_dimension()[0] / 2))
    elif simulton_selected is not None:
        add(eval(f"{simulton_selected}({x},{y})"))


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons -= s
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {s for s in simultons if p(s)}
    


#call update for every simulton (passing model to each) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count, simultons, garbage 
    if running:
        cycle_count += 1
        for simulton in simultons:
            simulton.update(model)
        simultons -= garbage
        garbage = set()

#For animation: (1) delete every simulton from the canvas; (2) call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for simulton in simultons:
        simulton.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" balls/"+str(cycle_count)+" cycles")
