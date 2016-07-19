from time import *
from random import *
x = 200
y = 20
speedX = 2
speedY = -2
ballX = 0
ballY = 0

def setup():
    size(400,400)
    background (255)
 
    
def draw():
    background(255)
    global x, y, ballY, ballX, speedX, speedY
    x = x + speedX
    y = y + speedY
    fill(255,0,0)
    ball = ellipse(x, y, 40, 40)
    
    if x >= 380:
        speedX = -2 
    if x <= 20:
        speedX = 2
    if y >= 400:
        speedY = -2
        print ("game over")
        
    if y <= 20:
        speedY = 2
    rect(mouseX,360,40,40)
        #ellipse(x,y , 40, 40)
    
    
    
   