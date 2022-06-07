"""
載入畫面測試檔案
"""
from ursina import *


class Preloader():
    def __init__(self):
        self.Models = ["CubeModel", "hospital", "Jail", "sign", "house1", "house2", "house3", "house4", "hotel", "OilField", "Park", "ResearchCenter"]
        self.Built = False
        self.Loaded = False
    def Preload_Models(self):
        class Preload_Model(Entity):
            def __init__(self, model):
                super().__init__(
                    model=model,
                    position=(-10000000,-10000000,-10000000),
                )
        def Generate_Model(model_name):
            return Preload_Model(model_name)
        self.Preload_Container = []
        for model_name in self.Models:
            self.Preload_Container.append(Generate_Model(model_name))
            self.Bar.scale = (self.Bar.scale[0]+1.4/len(self.Models), self.Bar.scale[1], self.Bar.scale[2])
            self.Bar.position = (self.Bar.position[0]+0.7/len(self.Models), self.Bar.position[1], self.Bar.position[2])
            if model_name == self.Models[-1]:
                self.Loaded = True
            yield model_name
    def Show_Loading_Bar(self):
        self.Built = True
        self.BG = Entity(
            parent=camera.ui,
            model="quad",
            scale=(2, 1, 0),
            position=(0, 0, 2),
            color=color.gray
        )
        self.Bar_BG = Entity(
            parent=camera.ui,
            model="quad",
            scale=(1.5, 0.1, 0),
            position=(0, -0.3, 1),
            color=color.white
        )
        self.Bar = Entity(
            parent=camera.ui,
            model="quad",
            scale=(0, 0.05, 0), #MAX X 1.4
            position=(-0.7, -0.3, 1),
            color=rgb(183, 255, 191)
        )
        self.Elements = [
            self.BG,
            self.Bar_BG,
            self.Bar
        ]
    def Destory_Loading_Screen(self):
        if self.Built:
            for Ele in self.Elements:
                destroy(Ele)

            

game = Ursina()
z = Preloader()
z.Show_Loading_Bar()
Funct = z.Preload_Models()
d = 1.4/len(z.Models)
f = d/2
k=0
def update():
    global d, f, k
    if not z.Loaded:
        next(Funct)
    else:
        z.Destory_Loading_Screen()
    
game.run()