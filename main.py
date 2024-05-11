from python_imagesearch.imagesearch import *
import pyautogui 
import time 

while True:
    button_po = imagesearch("po.jpg")
    if button_po[0] != -1:
        print("position: ", button_po[0], button_po[1])
        time.sleep(0.1)
        pyautogui.press('e')
    else: 
        print("линия не найдена")
    button_e = imagesearch("e.jpg") 
    if button_e[0] != -1: 
        print("position: ", button_e[0], button_e[1])
        time.sleep(0.1)
        pyautogui.press('e') 
    else: 
        print("E не найдена")


