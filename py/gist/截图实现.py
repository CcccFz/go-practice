# -- coding: utf-8 --

# 方法一
from PIL import ImageGrab
bbox = (300, 300, 300+200, 300+200)
img = ImageGrab.grab(bbox)
img.save("pixel.png")
img.show()


import pyscreenshot as ImageGrab
im=ImageGrab.grab(bbox=(10,10,510,510))
im.show()