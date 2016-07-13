from Myro import *
init ("sim")

def drawE():
    penDown()
    i = 0
    while i < 140:
      
        forward (1, .01)
        motors(-.1, .25, 0.4) 
        i = i + 1

def drawO():
    penDown()
    i = 0
    while i < 360:
        forward (1, .01)
        motors(-.1, .25, 0.4) 
        i = i + 1
        
       
drawO()