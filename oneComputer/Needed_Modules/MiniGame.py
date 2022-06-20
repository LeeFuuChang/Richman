from ursina import *
from random import randint





###########################################################################
#-------------------------MiniGame Class Template-------------------------#
###########################################################################
class GameName_MiniGame():
    def __init__(self):
        #Game Elements Initialization
        pass
    def Startup(self):
        #Startup Initialization
        pass
    def Destroy_Game(self):
        pass #Destroy game
    def Update(self): # return True or False
        return self.GameOver, self.Player.MiniGameScore





###########################################################################
#---------------------------DodgeLazer MiniGame---------------------------#
###########################################################################
class DodgeLazerPlayer(Entity):
    def __init__(self, orgin):
        self.orgin = orgin
        super().__init__(
            model="sphere",
            scale=(1, 1, 1),
            position=(self.orgin[0], self.orgin[1]+1, self.orgin[2]),
            color=color.red,
            collider="sphere"
        )
        self.Dead = False
        self.Jumping = False
        self.Gravity = 1
        self.vel = self.Gravity
        self.JumpLimit = 1
        self.MiniGameScore = 0
    def Jump_Animation(self):
        if self.Jumping:
            self.position = (
                self.position[0],
                self.position[1]+(self.vel*(time.dt*20)),
                self.position[2]
            )
            self.vel-=(time.dt*4.8)
            if self.position[1]+(self.vel*(time.dt*20)) <= self.orgin[1]:
                self.Jumping = False
                self.position = (
                    self.position[0],
                    self.orgin[1]+1,
                    self.position[2]
                )
                self.vel = self.Gravity

class DodgeLazerEnvirment():
    def __init__(self, orgin):
        self.orgin = orgin
        self.Floor = Entity(
            model="Cube",
            scale=(11, 1, 11),
            position=self.orgin,
            collider="box",
            color=color.gray
        )
        self.LazerGenater = [
            Entity(
                model="Cube",
                scale=(0.2, 0.2, 3),
                position=(self.orgin[0]+5.6, self.orgin[1]+1, self.orgin[2]),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(0.2, 0.2, 3),
                position=(self.orgin[0]-5.6, self.orgin[1]+1, self.orgin[2]),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(3, 0.2, 0.2),
                position=(self.orgin[0], self.orgin[1]+1, self.orgin[2]+5.6),
                collider="box"
            ),
            Entity(
                model="Cube",
                scale=(3, 0.2, 0.2),
                position=(self.orgin[0], self.orgin[1]+1, self.orgin[2]-5.6),
                collider="box"
            )
        ]

class LazerTop(Entity):
    def __init__(self, orgin):
        self.orgin = orgin
        super().__init__(
            model="Cube",
            scale=(11, 0.2, 0.2),
            position=(self.orgin[0], self.orgin[1]+1, self.orgin[2]+5.5),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player, LazerSpeed):
        self.position = (
            self.position[0],
            self.position[1],
            self.position[2]-LazerSpeed
        )
        if self.position[2] > Player.position[2]-self.Detect_Radius and self.position[2] < Player.position[2]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1+self.orgin[1]:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[2] < self.orgin[2]-5.5:
            destroy(self)
            self.Reached_Border = True
        return self.Reached_Border

class LazerBottom(Entity):
    def __init__(self, orgin):
        self.orgin = orgin
        super().__init__(
            model="Cube",
            scale=(11, 0.2, 0.2),
            position=(self.orgin[0], self.orgin[1]+1, self.orgin[2]-5.5),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player, LazerSpeed):
        self.position = (
            self.position[0],
            self.position[1],
            self.position[2]+LazerSpeed
        )
        if self.position[2] > Player.position[2]-self.Detect_Radius and self.position[2] < Player.position[2]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1+self.orgin[1]:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[2] > self.orgin[2]+5.5:
            destroy(self)
            self.Reached_Border = True
        return self.Reached_Border

class LazerRight(Entity):
    def __init__(self, orgin):
        self.orgin = orgin
        super().__init__(
            model="Cube",
            scale=(0.2, 0.2, 11),
            position=(self.orgin[0]+5.5, self.orgin[1]+1, self.orgin[2]),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player, LazerSpeed):
        self.position = (
            self.position[0]-LazerSpeed,
            self.position[1],
            self.position[2]
        )
        if self.position[0] > Player.position[0]-self.Detect_Radius and self.position[0] < Player.position[0]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1+self.orgin[1]:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[0] < self.orgin[0]-5.5:
            destroy(self)
            self.Reached_Border = True
        return self.Reached_Border

class LazerLeft(Entity):
    def __init__(self, orgin):
        self.orgin = orgin
        super().__init__(
            model="Cube",
            scale=(0.2, 0.2, 11),
            position=(self.orgin[0]-5.5, self.orgin[1]+1, self.orgin[2]),
            collider="box",
            color=color.green
        )
        self.Detect_Radius = ((2**0.5)/2)
        self.Reached_Border = False
    def move(self, Player, LazerSpeed):
        self.position = (
            self.position[0]+LazerSpeed,
            self.position[1],
            self.position[2]
        )
        if self.position[0] > Player.position[0]-self.Detect_Radius and self.position[0] < Player.position[0]+self.Detect_Radius:
            if Player.position[1]-self.Detect_Radius<=1+self.orgin[1]:
                Player.Dead = True
                self.Reached_Border = True
            else:
                Player.MiniGameScore += 1
        if self.position[0] > self.orgin[0]+5.5:
            destroy(self)
            self.Reached_Border = True
        return self.Reached_Border

class DodgeLazer_MiniGame():
    def __init__(self, orgin):
        self.Lazers = [LazerTop, LazerBottom, LazerRight, LazerLeft]
        self.LazerContainer = []
        self.GameOver = True
        self.EnvBuilt = False
        self.FrameCount = 0
        self.orgin = orgin
        camera.position = (self.orgin[0], self.orgin[1]+11, self.orgin[2]-20)
        camera.rotation_x = 30
        self.SpeedCounter = 0.1

    def Startup(self):
        if not self.EnvBuilt:
            self.EnvBuilt = True
            self.FrameCount = 0
            for Lazer in self.LazerContainer:
                destroy(Lazer)
            self.Envirment = DodgeLazerEnvirment(orgin=self.orgin)
            self.Player = DodgeLazerPlayer(orgin=self.orgin)
            self.LazerContainer = []
            self.Player.MiniGameScore = 0
            self.Player.position = (self.orgin[0], self.orgin[1]+1, self.orgin[2])

    def Destroy_Game(self):
        if self.EnvBuilt:
            self.EnvBuilt = False
            destroy(self.Player)
            for Lazer in self.LazerContainer:
                destroy(Lazer)
            for Lazer_Generater in self.Envirment.LazerGenater:
                destroy(Lazer_Generater)
            destroy(self.Envirment.Floor)

    def Update(self):
        if not self.Player.Dead:
            self.LazerSpeed = (time.dt * 60 * self.SpeedCounter)

            self.FrameCount+=(time.dt * 60)
            if self.FrameCount >= 50 and len(self.LazerContainer)<=4:
                self.FrameCount = 0
                self.LazerContainer.append(self.Lazers[randint(0, 3)](orgin=self.orgin))

            self.Player.z += held_keys['w'] * time.dt * 6

            self.Player.z -= held_keys['s'] * time.dt * 6

            self.Player.x += held_keys['d'] * time.dt * 6

            self.Player.x -= held_keys['a'] * time.dt * 6

            if held_keys["space"]:
                self.Player.Jumping = True

            self.Player.Jump_Animation()
            for Lazer in self.LazerContainer:
                if Lazer.move(Player=self.Player, LazerSpeed=self.LazerSpeed):
                    if self.Player.Dead:
                        self.Destroy_Game()
                        return self.Player.Dead, self.Player.MiniGameScore
                    self.LazerContainer.remove(Lazer)
            
            self.SpeedCounter = 0.1 + (self.Player.MiniGameScore//100)*0.02

        return self.Player.Dead, self.Player.MiniGameScore





###########################################################################
#-----------------------------MiniGame System-----------------------------#
###########################################################################
class MiniGame():
    def __init__(self, orgin=(0, 0, 0)):
        self.Games = [
            DodgeLazer_MiniGame
        ]

        self.Built = False
        self.orgin = orgin

        self.GameOver = False
        self.Score = 0
    
    def Game_mode(self):
        camera.position = self.orgin
        camera.rotation_x = 0
        camera.rotation_y = 0
        camera.rotation_z = 0

    def Build_Game(self):
        if not self.Built:
            self.Built = True
            self.GameOver = False
            self.Game_mode()
            self.Game = self.Games[randint(0, len(self.Games)-1)](orgin=self.orgin)
            self.Game.Startup()

    def Destroy_Game(self):
        if self.Built:
            self.Built = False
            self.Game.Destroy_Game()

    def Play(self):
        if not self.Built:
            self.Build_Game()
            return False, False
        else:
            self.GameOver, self.Score = self.Game.Update()
            if self.GameOver:
                print(f"Final Score: {self.Score}")
                self.Destroy_Game()
        return self.GameOver, self.Score

    def Test_Game(self, Game):
        if not self.Built:
            self.Built = True
            self.Game = Game()
            self.Game.Startup()
        else:
            GameOver, Score = self.Play()
            if GameOver:
                print(f"Final Score: {Score}")
                return GameOver






if __name__ == "__main__":
    a = Ursina()
    window.borderless = False

    system = MiniGame()
    GameOver = False
    def update():
        system.Play()
    a.run()