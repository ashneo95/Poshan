import pyautogui as gui
import time
from random import randint
#time.sleep(5)
print(gui.position())
gui.PAUSE = 0.4
'''
gui.click(255,297) # Activity Select
gui.press("home")
#gui.click(691,173) # Scroll to Top
gui.click(370,324) # Home Visit selected
gui.click(326,373) # Theme
gui.press("Home")
gui.press("Down",presses =8)
gui.press("Space")
gui.press("Esc")
gui.press("Tab")
gui.press("Down")
gui.press("tab")
gui.press("down", presses=4)
gui.press("enter")
gui.press("esc")
gui.press("tab",presses=5) # Total Participants field
'''
time.sleep(5)
gui.click(x=1104, y=600)


for i in range(1500):
    male_a = 1
    female_a = randint(1,3)
    male_c = randint(1,3)
    female_c = randint(1,3)
    total = male_a+female_a+male_c+female_c
    #print(total)
    gui.typewrite(str(total))
    gui.press("tab")
    gui.typewrite(str(male_a))
    gui.press("tab")
    gui.typewrite(str(female_a))
    gui.press("tab",presses=2)
    gui.typewrite(str(male_c))
    gui.press("tab")
    gui.typewrite(str(female_c))
    gui.press("tab",presses=3) # to go to Description Field
    gui.typewrite("D-Yewalewad")
    gui.press("tab",presses=2)
    gui.press("enter")
    time.sleep(0.81)
    gui.press("enter")
    time.sleep(1.00)
    gui.click(x=1104, y=600)
    print(i)


