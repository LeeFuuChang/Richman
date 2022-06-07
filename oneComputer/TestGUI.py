"""
測試介面用檔案
"""
from ursina import *
import os
from time import sleep
from threading import Thread
from Needed_Modules.Classes import *
from Needed_Modules.MapClasses import *
app = Ursina()


class Broken_Animation():
    def __init__(self):
        self.Original_v = 0.02
        self.v = -0.02
        self.UI = None
    def play_Broken_Animation(self):
        if not self.UI:
            self.UI = Entity(
                parent=camera.ui,
                model="quad",
                texture="assets\Others\Win",
                scale=(2, 1),
                position=(0, 5),
                color=color.white
            )
        elif int(str(self.Original_v)[0]) <= 0:
            if self.UI.y+self.v>0:
                self.UI.y += self.v
            else:
                self.Original_v*=0.5
                self.v = self.Original_v
            self.v -= 0.0005

k = Broken_Animation()
start = False
def update():
    global k, start
    if held_keys["g"]:
        start = True
    elif start:
        k.play_Broken_Animation()
    pass

app.run()