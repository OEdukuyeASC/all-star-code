from random import *

def setup ():
    size ( 400, 400)
    noStroke()  
    background(255)
    global ffImage
    ffImage = requestImage("noctis.png")
 
def draw():
    x = 150
    y = -150
    
    image(ffImage, mouseX, mouseY, x, y)