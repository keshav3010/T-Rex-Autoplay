from PIL import ImageGrab, ImageOps
import pyautogui 
import time
from numpy import *
class coordinates():
    restartbutton=(480,505)
    dino=(180,515)
    #xcord 210
    #ycord 547
def restartgame():
    pyautogui.click(coordinates.restartbutton)
def press():
    #pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('wooowwwww')
    pyautogui.keyUp('space')
def imageGrab():
    box=(coordinates.dino[0]+210,coordinates.dino[1],coordinates.dino[0]+257,coordinates.dino[1]+33)
    image=ImageGrab.grab(box)
    grayimg=ImageOps.grayscale(image)
    a= array(grayimg.getcolors())
    print(a.sum())
    return a.sum()
    
def main():
       restartgame()
       while True :
           if(imageGrab()!=1798):
               press()
               
       #exit()
main()
  
