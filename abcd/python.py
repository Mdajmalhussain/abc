import random
import pyautogui as pg
import time
animal=('kya hua','kya hua','kya hua')
time.sleep(8)
for i in range(1000): 

    a=random.choice(animal)
    pg.write(" "+a)
    pg.press('enter') 