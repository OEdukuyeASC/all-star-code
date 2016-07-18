from Myro import *

pic = makePicture(pickAFile())
show(pic)
Obama_DarkBlue = makeColor(0,51,76)

Obama_Red = makeColor(217, 26, 33)

Obama_Blue = makeColor(112,150,158)

Obama_Yellow = makeColor(252, 227, 166)

for pixel in getPixels(pic):
    
    getRed(pixel)
    getGreen(pixel)
    getBlue(pixel)
    gray = getGray(pixel)
    
    if gray > 180:
        setColor (pixel,Obama_DarkBlue)
    elif gray > 120: 
        setColor (pixel,Obama_Red)
    elif gray > 60: 
        setColor (pixel, Obama_Blue)
    else:
        setColor (pixel, Obama_Yellow)
        
      
        
        
# makeColor(RE)

 #setColor(PIXEL, COLOR)

    
    
    