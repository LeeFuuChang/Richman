from ursina import *
from random import randint




#最小 正常 最大 縮放值
MIN_ZOOM_IN = 8
NORMAL_ZOOM = 10
MAX_ZOOM_IN = 30




"""---BackGround Class---"""
class BackGround(Entity):
    def __init__(self):
        super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    scale = (2, 1, 0),
                    position = (0, 0, 2),
                    color = color.gray
                )
        class CloseButton(Button):
            def __init__(self):
                super().__init__(
                            parent = camera.ui,
                            model = "quad",
                            scale = (0.05, 0.05),
                            position = (0.8, 0.4, 0),
                            text = "X",
                            color = color.red
                        )
                self.Close = False
            def input(self, key):
                if self.hovered:
                    if key == "left mouse down":
                        self.Close = True
        self.CloseButton = CloseButton()




#############################################################
"""
CloseButton
"""
class Close_Button(Button):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "quad",
            scale = 0.05,
            position = (0.8, 0.45),
            color = color.red,
            text_color = color.white,
            text = "X"
        )
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True



#############################################################
"""
ChooseTarget GUI
"""
class ChooseTargetButton(Button):
    def __init__(self, player, posX):
        super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (posX, 0, 0),
                    scale = (0.32, 0.48, 1),
                    color = player.color,
                )
        self.player = player
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True
                print("ya")
                pass

class ChooseTarget():
    def __init__(self, players):
        self.Button_Container = []
        self.players = players
        self.Built = False
    def Get_All_Player(self):
        return self.players
    def Build_GUI(self):
        if not self.Built:
            self.Result = None
            self.BackGround = BackGround()
            posX = -0.6
            for P in self.players:
                self.Button_Container.append(ChooseTargetButton(P, posX))
                posX += 0.4
            self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            for entity in self.Button_Container:
                destroy(entity)
            destroy(self.BackGround.CloseButton)
            destroy(self.BackGround)
            self.Built = False
            self.Button_Container = []
    def Check(self):
        for button in self.Button_Container:
            if button.Choosed or self.BackGround.CloseButton.Close:
                self.Destroy_GUI()
                self.Result = button.player
                return True
        return False




#############################################################
"""
ChoosePoint GUI
"""
class ChoosePointButton(Button):
    def __init__(self, Xpos, Ypos, point):
        class PointImageEntity(Entity):
            def __init__(self, parent, posX, posY):
                super().__init__(
                    parent = parent,
                    model = "circle",
                    position = (posX, posY, -1),
                    color = color.black,
                    scale = (0.25, 0.25, 0)
                )
        self.ImageCoordnates = {
            6:[(-0.25, 0.3), (-0.25, 0), (-0.25, -0.3), (0.25, 0.3), (0.25, 0), (0.25, -0.3)],
            5:[(-0.25, 0.25), (-0.25, -0.25), (0, 0), (0.25, -0.25), (0.25, 0.25)],
            4:[(-0.25, 0.25), (-0.25, -0.25), (0.25, -0.25), (0.25, 0.25)],
            3:[(-0.25, 0.25), (0, 0), (0.25, -0.25)],
            2:[(-0.25, 0.25), (0.25, -0.25)],
            1:[(0, 0)]
        }
        super().__init__(
            parent = camera.ui,
            model = "quad",
            position = (Xpos, Ypos, 0),
            color = color.white,
            scale = (0.2, 0.2, 0)
        )
        self.Container = [self]
        self.Choosed = False
        self.Point = point
        for Coordnate in self.ImageCoordnates[point]:
            self.Container.append(PointImageEntity(parent=self, posX=Coordnate[0], posY=Coordnate[1]))
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChoosePoint():
    def __init__(self):
        self.Y_Coordnates = [0.2, -0.2]
        self.X_Coordnates = [-0.4, 0, 0.4]
        self.Built = False
        self.Result = False

    def Build_GUI(self):
        if not self.Built:
            self.Built = True
            self.BackGround = BackGround()
            self.Container = [self.BackGround, self.BackGround.CloseButton]
            self.Button_Container = []
            self.Result = False

            _point=1
            for y in self.Y_Coordnates:
                for x in self.X_Coordnates:
                    _button = ChoosePointButton(Xpos=x, Ypos=y, point=_point)
                    self.Container.extend(_button.Container)
                    self.Button_Container.append(_button)
                    _point+=1

    def Destroy_GUI(self):
        if self.Built:
            for element in self.Container:
                destroy(element)
            self.Built = False

    def Check(self):
        if self.BackGround.CloseButton.Close:
            self.Destroy_GUI()
            return True
        for button in self.Button_Container:
            if button.Choosed:
                self.Result = button.Point
                self.Destroy_GUI()
                return True
        return False




#############################################################
"""
CleanBot Class
"""
class CleanBot(Entity):
    def __init__(self , Owner, map, mapWidth, mapHeight, Walkable_Bindings, direction, start=(0, 0, 0), speed=1):
        super().__init__(
            model = self.__class__.__name__,
            scale = .5,
            position = (start[0], start[1]+0.25, start[2]),
            color = Owner.color
        )
        self.MAP = map
        self.Walkable_Bindings = Walkable_Bindings
        self.MapWidth = mapWidth
        self.MapHeight = mapHeight
        self.MapPosZ = int(self.MapHeight-self.position[2])
        self.MapPosX = int(self.position[0])
        self.SPEED = speed
        self.direction = direction

        self.Walkable = ["Lott","Game",
        "Add1C","Add2C","Add3C","Magic","Road","Bank",
        "Add2","Add5","Add10","Add20","Mis2","Mis5","Mis10","Mis20",
        "News","Shop"]

        self.points_Left = 10

    def Camera_Follow(self):
        camera.position = (self.position[0]-6, MIN_ZOOM_IN, self.position[2]-NORMAL_ZOOM)

    def move(self):
        if self.points_Left > 0:
            x, _, z = self.position
            z = int(self.MapHeight-z)
            x = int(x)

            #移動
            if True not in self.direction:
                self.direction = [False, False, False, False]
                self.direction[randint(0, 3)] = True
            direction_index = self.direction.index(True)
            if direction_index == 0: #現在正在往上
                if self.MAP[z-1][x] in self.Walkable: #檢查再往上還有沒有路
                    self.position = (self.position[0], self.position[1], self.position[2]+self.SPEED)
                else:
                    self.direction[direction_index] = False
                    if self.MAP[z][x-1] in self.Walkable: #往左找路
                        self.direction[2] = True
                        self.position = (self.position[0]-self.SPEED, self.position[1], self.position[2])
                    elif self.MAP[z][x+1] in self.Walkable: #往右找路
                        self.direction[3] = True
                        self.position = (self.position[0]+self.SPEED, self.position[1], self.position[2])

            elif direction_index == 1: #現在正在往下
                if self.MAP[z+1][x] in self.Walkable: #檢查再往前還有沒有路
                    self.position = (self.position[0], self.position[1], self.position[2]-self.SPEED)
                else:
                    self.direction[direction_index] = False
                    if self.MAP[z][x+1] in self.Walkable: #往右找路
                        self.direction[3] = True
                        self.position = (self.position[0]+self.SPEED, self.position[1], self.position[2])
                    elif self.MAP[z][x-1] in self.Walkable: #往左找路
                        self.direction[2] = True
                        self.position = (self.position[0]-self.SPEED, self.position[1], self.position[2])


            elif direction_index == 2: #現在正在往左
                if self.MAP[z][x-1] in self.Walkable: #檢查再往前還有沒有路
                    self.position = (self.position[0]-self.SPEED, self.position[1], self.position[2])
                else:
                    self.direction[direction_index] = False
                    if self.MAP[z+1][x] in self.Walkable: #往下找路
                        self.direction[1] = True
                        self.position = (self.position[0], self.position[1], self.position[2]-self.SPEED)
                    elif self.MAP[z-1][x] in self.Walkable: #往上找路
                        self.direction[0] = True
                        self.position = (self.position[0], self.position[1], self.position[2]+self.SPEED)

            elif direction_index == 3: #現在正在往右
                if self.MAP[z][x+1] in self.Walkable: #檢查再往前還有沒有路
                    self.position = (self.position[0]+self.SPEED, self.position[1], self.position[2])
                else:
                    self.direction[direction_index] = False
                    if self.MAP[z-1][x] in self.Walkable: #往上找路
                        self.direction[0] = True
                        self.position = (self.position[0], self.position[1], self.position[2]+self.SPEED)
                    elif self.MAP[z+1][x] in self.Walkable: #往下找路
                        self.direction[1] = True
                        self.position = (self.position[0], self.position[1], self.position[2]-self.SPEED)
                
            self.Camera_Follow()

        self.points_Left -= 1

        x, _, z = self.position
        self.MapPosZ = int(self.MapHeight-z)
        self.MapPosX = int(x)

        GetBindingInformation = self.Walkable_Bindings.get((self.MapPosZ, self.MapPosX), False)
        if GetBindingInformation:
            if GetBindingInformation.Stop:
                destroy(GetBindingInformation.Stop)
                GetBindingInformation.Stop = False
            elif GetBindingInformation.Bomb:
                destroy(GetBindingInformation.Bomb)
                GetBindingInformation.Bomb = False
        
        if self.points_Left == -1:
            destroy(self)
            return 1
        else:
            return False