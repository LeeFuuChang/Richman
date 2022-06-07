"""
測試用檔案二
"""
from ursina import *
from Cards import *
from Systems import*
a = Ursina()


class DodgeLazerPlayer(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            scale=(1, 1, 1),
            position=(0, 1, 0),
            color=color.red,
            collider="sphere"
        )
        self.Dead = False
        self.Jumping = False
        self.Gravity = 1
        self.vel = self.Gravity
        self.JumpLimit = 1
        self.MiniGameScore = 0
    def Jump(self):
        self.Jumping = True
    def Jump_Animation(self):
        if self.Jumping:
            self.position = (
                self.position[0],
                self.position[1]+(self.vel*0.3),
                self.position[2]
            )
            self.vel-=0.08
            if self.position[1]+(self.vel*0.3) <= 0:
                self.Jumping = False
                self.position = (
                    self.position[0],
                    1,
                    self.position[2]
                )
                self.vel = self.Gravity
                

class DodgeLazerEnvirment():
    def __init__(self):
        self.Floor = Entity(
            model="Cube",
            scale=(11, 1, 11),
            position=(0, 0, 0),
            collider="box",
            color=color.gray
        )
        self.LazerGenater = [
            Entity(
                model="Cube",
                scale=(0.2, 0.2, 3),
                position=(5.6, 1, 0),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(0.2, 0.2, 3),
                position=(-5.6, 1, 0),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(3, 0.2, 0.2),
                position=(0, 1, 5.6),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(3, 0.2, 0.2),
                position=(0, 1, -5.6),
                collider="box"
            )
        ]


class LazerTop(Entity):
    def __init__(self):
        super().__init__(
            model="Cube",
            scale=(11, 0.2, 0.2),
            position=(0, 0.8, 5.5),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player):
        self.position = (
            0,
            0.8,
            self.position[2]-0.1
        )
        if self.position[2] > Player.position[2]-self.Detect_Radius and self.position[2] < Player.position[2]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[2] < -5.5:
            self.Reached_Border = True
        return self.Reached_Border

class LazerBottom(Entity):
    def __init__(self):
        super().__init__(
            model="Cube",
            scale=(11, 0.2, 0.2),
            position=(0, 1, -5.5),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player):
        self.position = (
            0,
            1,
            self.position[2]+0.1
        )
        if self.position[2] > Player.position[2]-self.Detect_Radius and self.position[2] < Player.position[2]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[2] > 5.5:
            self.Reached_Border = True
        return self.Reached_Border

class LazerRight(Entity):
    def __init__(self):
        super().__init__(
            model="Cube",
            scale=(0.2, 0.2, 11),
            position=(5.5, 1, 0),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player):
        self.position = (
            self.position[0]-0.1,
            1,
            0
        )
        if self.position[0] > Player.position[0]-self.Detect_Radius and self.position[0] < Player.position[0]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1.1:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[0] < -5.5:
            self.Reached_Border = True
        return self.Reached_Border

class LazerLeft(Entity):
    def __init__(self):
        super().__init__(
            model="Cube",
            scale=(0.2, 0.2, 11),
            position=(-5.5, 1, 0),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player):
        self.position = (
            self.position[0]+0.1,
            1,
            0
        )
        if self.position[0] > Player.position[0]-self.Detect_Radius and self.position[0] < Player.position[0]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1.1:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[0] > 5.5:
            self.Reached_Border = True
        return self.Reached_Border

class MiniGame():
    def __init__(self):
        self.Camera = camera
        self.Env = DodgeLazerEnvirment()
        self.Player = DodgeLazerPlayer()

    def Startup(self):
        self.Player.position = (0, 1, 0)
        self.Camera.position = (0, 11, -20)
        self.Camera.rotation_x = 30

pp=MiniGame()
pp.Startup()
pp.Player.Dead = False
f = r = j = 0
Lazers = [LazerTop, LazerBottom, LazerRight, LazerLeft]
LazerContainer = []
def Start():
    global pp, f, r, j, LazerContainer, Lazers
    for Lazer in LazerContainer:
        destroy(Lazer)
    pp.Startup()
    pp.Player.Dead = False
    f = r = j = 0
    Lazers = [LazerTop, LazerBottom, LazerRight, LazerLeft]
    LazerContainer = []

Start()

class ggButton(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(2, 1, 0),
            position=(0, 0, 0),
            text="Game Over",
            text_color=color.red,
            text_size=3,
            color=color.gray
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
                print("Restart")
                Start()


def update():
    global f, r, j, LazerContainer, Lazers
    if not pp.Player.Dead:
        j+=1
        if j%50==0 and len(LazerContainer)<=4:
            LazerContainer.append(Lazers[randint(0, 3)]())

        if held_keys["w"]:
            f+=0.1
            pp.Player.position = (pp.Player.position[0], pp.Player.position[1], f)
        if held_keys["s"]:
            f-=0.1
            pp.Player.position = (pp.Player.position[0], pp.Player.position[1], f)

        if held_keys["d"]:
            r+=0.1
            pp.Player.position = (r, pp.Player.position[1], pp.Player.position[2])
        if held_keys["a"]:
            r-=0.1
            pp.Player.position = (r, pp.Player.position[1], pp.Player.position[2])

        if held_keys["space"]:
            pp.Player.Jump()

        pp.Player.Jump_Animation()
        if LazerContainer:
            for Lazer in LazerContainer:
                if Lazer.move(pp.Player):
                    if pp.Player.Dead:
                        ggButton()
                        print(f"Final Score: {pp.Player.MiniGameScore}")
                        break
                    destroy(Lazer)
                    LazerContainer.remove(Lazer)
a.run()