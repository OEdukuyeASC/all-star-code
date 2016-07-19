from random import *

def setup ():
    size ( 400, 400)
    background(255)
    noStroke()
    
    
def draw (): 
    z = randint (0,255)
    y = randint(0,255)
    x = randint(0, 255)
    fill(x, y, z)
    ellipse(mouseX, mouseY, x, y)
    randint(0,255)
    
    ellipse(mouseX + 120, mouseY, 25, 25)
    ellipse(mouseX 120, mouseY, 25, 25) 
    ellipse(mouseX + 120, mouseY, 25, 25)
    ellipse(mouseX + 120, mouseY, 25, 25)
     

     