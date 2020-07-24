from PIL import Image, ImageGrab # pip install pillow
import pyautogui
from numpy import asarray
import time
import pygame
import random

def check(data):
    for i in range(120 , 123):
        for j in range(238, 241):
            if data[i, j] ==pygame.Color("#000000"):
                time.sleep(random.uniform(2,8))
                pyautogui.click(x=117, y=243)
                return

    for i in range(540, 543):
        for j in range(347, 350):
            if data[i, j] == pygame.Color("#99ff99"):
                time.sleep(random.uniform(1,4))
                pyautogui.click(x=395 ,y=323)
                return
    return

print("We'll start in 5secs.")
time.sleep(5)
print("Lets Go!!")

while True:
    image = ImageGrab.grab()
    #image.show()
    #print(image)
    data = image.load()
    #print(asarray(image))
    check(data)



'''

#use these coords for picking colors
# #060802
# #99ff99

for i in range(120 , 123):
    for j in range(250, 253):
        data[i, j] = 255

for i in range(497, 503):
    for j in range(385, 390):
        data[i, j] = 171


for a in range(318, 323):
    for b in range(325, 330):
        data[a, b] = 255

image.show()

'''
