"""
GUI系統物件導向
"""
from time import sleep
from random import randint
from ursina import *
from .Cards import *
from .MapClasses import *
from threading import Thread


def Make_After(dic, key, value, delay):
    def Make_var():
        wait(delay)
        dic[key] = value
    T(target=Make_var).start()


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
PreStart Menu and Game Room class
"""
#############################################
# Start Game Button
class Join_Game_Button(Button):
    def __init__(self, BG):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.2, 0.1),
            texture = "assets/MainGUI/Join",
            position = (0, -0.25, -1),
            color = color.white
        )
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

#############################################
# Choose Map
class GO_ChooseMap_GUI_Button(Button):
    def __init__(self, BG, Map):
        if Map == "Random":
            super().__init__(
                parent = BG,
                model = "quad",
                texture = "assets/ChooseMapTexture/Random",
                scale = (0.25, 0.35),
                position = (-0.225, 0.225, -1),
                color = color.white
            )
        else:
            super().__init__(
                parent = BG,
                model = "quad",
                texture = f"assets/ChooseMapTexture/{Map.__name__}",
                scale = (0.25, 0.35),
                position = (-0.225, 0.225),
                color = color.white
            )
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

class ChooseMap_Button(Button):
    def __init__(self, BG, Represent, position):
        if Represent == "Random":
            super().__init__(
                parent = BG,
                model = "quad",
                scale = (0.36, 0.1, 0),
                position = position,
                texture = f"assets/ChooseMapTexture/Random.png",
                color = color.white
            )
        else:
            super().__init__(
                parent = BG,
                model = "quad",
                scale = (0.36, 0.1, 0),
                position = position,
                texture = f"assets/ChooseMapTexture/{Represent.__name__}",
                color = color.white
            )
        self.Choosed = False
        self.Represent = Represent
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class Close_ChooseMap_Button(Button):
    def __init__(self, BG):
        width, height = BG.scale[1]/BG.scale[0], BG.scale[1]
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (width/16, height/16, 0),
            position = (0.4, 0.4, -2),
            text_color = color.white,
            text = "X",
            color = color.red
        )
        self.Choosed = False
        self.Represent = "Old"
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseMap(Entity):
    def __init__(self, BG, MapList):
        self.BG = BG
        self.width, self.height = self.BG.scale[1]/self.BG.scale[0], self.BG.scale[1]
        self.MapList = MapList
        self.Built = False
    def Build_GUI(self):
        if not self.Built:
            super().__init__(
                parent = self.BG,
                model = "quad",
                scale = (self.width, self.height*2, 0),
                position = (0, -0.5, -1),
                color = color.light_gray
            )
            self.Button_Container = []
            self.Button_Container.append(
                Close_ChooseMap_Button(BG=self.BG)
            )
            self.Button_Container.append(
                ChooseMap_Button(BG=self, Represent="Random", position=(-0.225, 0.4375, -2))
            )
            nowPlacingAt = [0.225, 0.4375]
            for Map in self.MapList:
                if nowPlacingAt[0] < 0:
                    self.Button_Container.append(
                        ChooseMap_Button(BG=self, Represent=Map, position=(nowPlacingAt[0], nowPlacingAt[1]))
                    )
                    nowPlacingAt[0] = 0.225
                else:
                    self.Button_Container.append(
                        ChooseMap_Button(BG=self, Represent=Map, position=(nowPlacingAt[0], nowPlacingAt[1]))
                    )
                    nowPlacingAt[0] = -0.225
                    nowPlacingAt[1] -= 0.125
            self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            destroy(self.Button_Container[0])
            destroy(self)
    def input(self, key):
        if -0.5 < mouse.position[0] < 0.5:
            if key == "scroll up":
                if self.y > -0.5:
                    self.y -= 0.1
            if key == "scroll down":
                if self.y < 0.5:
                    self.y += 0.1
        if self.y > 0.5:
            self.y = 0.5
        elif self.y < -0.5:
            self.y = -0.5
    def Check(self):
        for button in self.Button_Container:
            if button.Choosed:
                self.Destroy_GUI()
                return button.Represent
        return False

#############################################
# Choose Default Balance / Bank and Price_Rising
class DraggableEntity(Button):
    def __init__(self, parent, model, scale, color, position, default_Xpos=0):
        super().__init__(
            parent = parent,
            model = model,
            scale = scale,
            color = color,
            position = position
        )
        self.x = default_Xpos
        self.Dragging = False
    def input(self, key):
        if self.hovered and key == "left mouse down":
            self.Dragging = True
        if self.Dragging and key == "left mouse up":
            self.Dragging = False
    def update(self):
        Mx = mouse.position.x
        if self.Dragging:
            if Mx < -0.68:
                self.x = -0.45
            elif Mx > -0.23:
                self.x = 0.45
            else:
                self.x = (Mx + 0.23)*2+0.45
    def GetPersentage(self, Number=1):
        Persentage = int((((self.x+0.45)/0.9)+0.003)*100)
        return int(Number/100*Persentage)

class slider(DraggableEntity):
    def __init__(self, BG, default_Xpos):
        self.TrackBar = Entity(
            parent = BG,
            model = "quad",
            scale = (0.9, 0.15),
            color = color.light_gray,
            position = (0, -0.2, -2)
        )
        super().__init__(
            parent = BG,
            model = "circle",
            scale = (0.075, 0.375),
            color = color.black,
            position = (0, -0.2, -3),
            default_Xpos = default_Xpos
        )

class ChooseDefaults(Button):
    def __init__(self, BG, DefaultXpos=[-0.18, -0.18, -0.27]):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.25, 0.4),
            disabled = True,
            position = (-0.225, -0.2, -1),
            color = color.gray
        )
        self.ChooseDefaultBalance = Button(
            parent = self,
            model = "quad",
            scale = (1, 0.25),
            disabled = True,
            position = (0, 0.375, -2),
            color = color.white,
            text_color = color.black,
            text_origin = (0.4, 0.3),
            text = "1",
            texture = "assets/MainGUI/DefaultBalance"
        )
        self.ChooseDefaultBalanceSlider = slider(BG=self.ChooseDefaultBalance, default_Xpos=DefaultXpos[0])
        
        self.ChooseDefaultBank = Button(
            parent = self,
            model = "quad",
            scale = (1, 0.25),
            disabled = True,
            position = (0, 0, -2),
            color = color.white,
            text_color = color.black,
            text_origin = (0.4, 0.3),
            text = "1",
            texture = "assets/MainGUI/DefaultBank"
        )
        self.ChooseDefaultBankSlider = slider(BG=self.ChooseDefaultBank, default_Xpos=DefaultXpos[1])
        
        self.ChooseDefaultPriceRising = Button(
            parent = self,
            model = "quad",
            scale = (1, 0.25),
            disabled = True,
            position = (0, -0.375, -2),
            color = color.white,
            text_color = color.black,
            text_origin = (0.4, 0.3),
            text = "1",
            texture = "assets/MainGUI/DefaultPriceRising"
        )
        self.ChooseDefaultPriceRisingSlider = slider(BG=self.ChooseDefaultPriceRising, default_Xpos=DefaultXpos[2])
    def Get_Defaults(self):
        return [self.ChooseDefaultBalanceSlider.x, self.ChooseDefaultBankSlider.x, self.ChooseDefaultPriceRisingSlider.x]
    def update(self):
        self.Default_Balance_Result = self.ChooseDefaultBalanceSlider.GetPersentage(Number=59)*10000 + 10000
        self.Default_Bank_Result = self.ChooseDefaultBankSlider.GetPersentage(Number=59)*10000 + 10000
        self.Default_PriceRising_Result = self.ChooseDefaultPriceRisingSlider.GetPersentage(Number=59) + 1

        self.ChooseDefaultBalance.text = str(self.Default_Balance_Result)
        self.ChooseDefaultBank.text = str(self.Default_Bank_Result)
        self.ChooseDefaultPriceRising.text = str(self.Default_PriceRising_Result)

#############################################
# Choose Player Color
class PlayerClone(Button):
    def __init__(self, BG, Xpos, Color):
        super().__init__(
            parent = BG,
            model = "circle",
            scale = (0.15, 0.3),
            position = (Xpos, 0.07, -2),
            color = Color
        )
        self.Choosed = False
    def BindClones(self, Clones):
        self.CloneList = Clones.copy()
        self.CloneList.remove(self)
    def updateChoosed(self):
        if not self.Choosed:
            self.scale = (0.2, 0.4)
            self.y = 0.1
            self.Choosed = True
        else:
            self.scale = (0.15, 0.3)
            self.y = 0.07
            self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.updateChoosed()
                for OtherClone in self.CloneList:
                    OtherClone.Choosed = True
                    OtherClone.updateChoosed()

class Choose_Color_Button(Button):
    def __init__(self, BG, Xpos, Color):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.08, 0.65),
            position = (Xpos, 0, -2),
            color = color.black
        )
        self.Color_Icon = Entity(
            parent = self,
            model = "quad",
            scale = (0.85, 0.85),
            position = (0, 0, -3),
            color = Color
        )
        self.disabled = False
        self.Choosed = False
        self.Represent = Color
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if not self.disabled:
                    self.Choosed = True

class ChooseColorBar(Entity):
    def __init__(self, BG, PlayerClone, CurrentColor, ColorList):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.4, 0.1),
            position = (0.15, -0.15, -1),
            color = color.white
        )
        self.PlayerCloneList = PlayerClone
        stX = 0.425
        self.Button_Container = []
        for i in range(8):
            Color_button = Choose_Color_Button(BG=self, Xpos=stX, Color=ColorList[i])
            if ColorList[i] in CurrentColor:
                Color_button.color = color.gray
                Color_button.disabled = True
            self.Button_Container.append(Color_button)
            stX -= 0.12

        self.Container = [self]
    def update(self):
        for color_button in self.Button_Container:
            if color_button.Choosed:
                for PlayerClone in self.PlayerCloneList:
                    if PlayerClone.Choosed:
                        PlayerClone.color = color_button.Represent
                        break
                color_button.color = color.gray
                color_button.disabled = True
                color_button.Choosed = False
                continue
            elif not any(PlayerClone.color == color_button.Represent for PlayerClone in self.PlayerCloneList):
                color_button.color = color.black
                color_button.disabled = False
                continue

class ChoosePlayerColors(Entity):
    def __init__(self, BG, CurrentColor, ColorList):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.4, 0.4),
            texture = "assets/MainGUI/PlayerAreaBG",
            position = (0.15, 0.15, -1),
            color = color.white
        )

        self.p1 = PlayerClone(BG=self, Xpos=-0.36, Color=CurrentColor[0])
        self.p2 = PlayerClone(BG=self, Xpos=-0.12, Color=CurrentColor[1])
        self.p3 = PlayerClone(BG=self, Xpos=0.12, Color=CurrentColor[2])
        self.p4 = PlayerClone(BG=self, Xpos=0.36, Color=CurrentColor[3])
        self.CloneList = [self.p1, self.p2, self.p3, self.p4]
        for Clone in self.CloneList:
            Clone.BindClones(Clones=self.CloneList)

        self.Bar = ChooseColorBar(BG=BG, PlayerClone=self.CloneList, CurrentColor=CurrentColor, ColorList=ColorList)

        self.Container = [self, self.Bar]
    def Get_Player_Colors(self):
        return [playerClone.color for playerClone in self.CloneList]

#############################################
# Start & Leave Button
class StartButton(Button):
    def __init__(self, BG):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.15, 0.1),
            position = (0.275, -0.3, -1),
            texture = "assets/MainGUI/Start",
            color = color.white
        )
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class LeaveButton(Button):
    def __init__(self, BG):
        super().__init__(
            parent = BG,
            model = "quad",
            scale = (0.15, 0.1),
            position = (0.025, -0.3, -1),
            texture = "assets/MainGUI/Leave",
            color = color.white
        )
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

#############################################
# Main Start System
class Start_RichMan_System(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "quad",
            scale = (2, 1, 0),
            position = (0, 0, 0),
            color = color.gray
        )

        self.ChooseMap_System = ChooseMap(BG=self, MapList=Maps().All_Maps)
        self.Choosed_Map_Result = "Random"

        self.ChooseDefaultsDraggerPositions = [-0.18, -0.18, -0.27]

        self.Player_Color_Result = [color.black, color.black, color.black, color.black]
        self.PlayerColorList = [color.red, color.white, color.orange, color.yellow, color.green, color.magenta, color.brown, color.azure]

        self.Container = []
        self.Room_Built = False
        self.Welcome_Built = True
        self.Build_Welcome_GUI()

    def Destroy_Current_Element(self):
        destroy(self.ChooseDefaults)
        for element in self.Container:
            destroy(element)
            self.Container = []
        self.Room_Built = False
        if self.Welcome_Built:
            destroy(self.Welcome_Button)

    def Build_ChooseMap_GUI(self):
        super().__init__(
            parent = camera.ui,
            model = "quad",
            scale = (2, 1, 0),
            position = (0, 0, 0),
            color = color.gray
        )
        self.ChooseMap_System.Build_GUI()
        
    def Build_Room_GUI(self):
        if not self.ChooseMap_System.Built and not self.Welcome_Built:
            self.Container = []
            self.Choose_Map_Button = GO_ChooseMap_GUI_Button(BG=self, Map=self.Choosed_Map_Result)
            self.Container.append(self.Choose_Map_Button)

            self.ChooseDefaults = ChooseDefaults(BG=self, DefaultXpos=self.ChooseDefaultsDraggerPositions)
            self.Container.append(self.ChooseDefaults)

            self.Player_Stuff_Area = ChoosePlayerColors(BG=self, CurrentColor=self.Player_Color_Result, ColorList=self.PlayerColorList)
            self.Container.extend(self.Player_Stuff_Area.Container)

            self.StartButton = StartButton(BG=self)
            self.LeaveButton = LeaveButton(BG=self)
            self.Container.extend([self.StartButton, self.LeaveButton])

            self.Room_Built = True

    def Build_Welcome_GUI(self):
        if not self.ChooseMap_System.Built and not self.Room_Built:
            self.Welcome_Built = True

            self.Welcome_Button = Join_Game_Button(BG=self)
            self.Container.append(self.Welcome_Button)

            self.ChooseMap_System = ChooseMap(BG=self, MapList=Maps().All_Maps)
            self.Choosed_Map_Result = "Random"

            self.Player_Color_Result = [color.black, color.black, color.black, color.black]
    
    def StartGame(self):
        if self.Choosed_Map_Result == "Random":
            self.Choosed_Map_Result = Maps().SelectRandomMap()
        else:
            self.Choosed_Map_Result = self.Choosed_Map_Result()

        UnChoosed_Player_Colors = [Color for Color in self.PlayerColorList if Color not in self.Player_Color_Result]
        for x, PlayerColor in enumerate(self.Player_Color_Result):
            if PlayerColor.name == "black":
                print(f"Player_{x+1} Color Randomed")
                self.Player_Color_Result[x] = UnChoosed_Player_Colors.pop(randint(0, len(UnChoosed_Player_Colors)-1))

        StartGameInfo = {
            "Start":True,
            "Map":self.Choosed_Map_Result,
            "playerColors":self.Player_Color_Result,
            "DefaultBalance":int(self.ChooseDefaults.ChooseDefaultBalance.text),
            "DefaultBank":int(self.ChooseDefaults.ChooseDefaultBank.text),
            "DefaultPriceRising":int(self.ChooseDefaults.ChooseDefaultPriceRising.text)
        }
        print(f"\n\nMap：\t{self.Choosed_Map_Result.__class__.__name__}")
        print(f"PlayerColors：\n\tPlayer1:{self.Player_Color_Result[0].name}\n\tPlayer2:{self.Player_Color_Result[1].name}\n\tPlayer3:{self.Player_Color_Result[2].name}\n\tPlayer4:{self.Player_Color_Result[3].name}")
        print(f"Defaults：\n\tWallet:{self.ChooseDefaults.ChooseDefaultBalance.text}\n\tBank:{self.ChooseDefaults.ChooseDefaultBank.text}\n\tPriceRising:{self.ChooseDefaults.ChooseDefaultPriceRising.text}")
        return StartGameInfo

    def Check(self):
        if self.ChooseMap_System.Built:
            New_Choose_Map_Result = self.ChooseMap_System.Check()
            if New_Choose_Map_Result:
                if New_Choose_Map_Result != "Old":
                    self.Choosed_Map_Result = New_Choose_Map_Result
                self.Build_Room_GUI()
        elif self.Room_Built:
            if self.StartButton.Choosed:
                os.system("cls")
                self.Player_Color_Result = self.Player_Stuff_Area.Get_Player_Colors()
                self.StartGameInfo = self.StartGame()
                destroy(self)
                self.StartButton.Choosed = False
                return True
            elif self.LeaveButton.Choosed:
                self.Destroy_Current_Element()
                self.Build_Welcome_GUI()
            elif self.Choose_Map_Button.Clicked:
                self.Player_Color_Result = self.Player_Stuff_Area.Get_Player_Colors()
                self.ChooseDefaultsDraggerPositions = self.ChooseDefaults.Get_Defaults()
                self.Destroy_Current_Element()
                self.Build_ChooseMap_GUI()
                self.Choose_Map_Button.Clicked = False
        elif self.Welcome_Built:
            if self.Welcome_Button.Clicked:
                self.Welcome_Built = False
                destroy(self.Welcome_Button)
                self.Build_Room_GUI()
        return False




#############################################################
"""
Preloader class
"""
class Preloader():
    def __init__(self):
        self.Models = ["CubeModel", "hospital", "Jail", "sign", "house1", "house2", "house3", "house4", "hotel", "OilField", "Park", "StockExchange"]
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




#############################################################
"""
Lottery GUI
"""
class LotteryOpening():
    def __init__(self):
        self.ScrollCount = self.WinnerNumber = self.Scrolling = self.Built = self.End = False
    def Open(self, WinnerPrice):
        if not self.Built:
            self.Built = True
            self.End = False
            self.BackGround = Entity(
                model="quad",
                parent=camera.ui,
                color=color.white,
                scale=(0.7, 0.7),
                position=(0, 0, 0),
                texture="assets\LotteryOpening\Background"
            )
            self.Top = Entity(
                model="quad",
                parent=self.BackGround,
                color=color.white,
                scale=(0.705, 0.079),
                position=(0.0145, 0.4606, -2),
                texture="assets\LotteryOpening\TOP"
            )
            self.Bottom = Entity(
                model="quad",
                parent=self.BackGround,
                color=color.white,
                scale=(0.705, 0.22),
                position=(0.0145, -0.39, -2),
                texture="assets\LotteryOpening\Bottom"
            )
            self.Number = Entity(
                model="quad",
                parent=self.BackGround,
                color=color.white,
                scale=(0.705, 0.705),
                position=(0.0145, 0.07, -1)
            )
            self.Price = Button(
                model="quad",
                parent=self.BackGround,
                color=color.white,
                disabled=True,
                text_color=color.black,
                text=f"{WinnerPrice}",
                scale=(0.7, 0.06),
                position=(0.0145, -0.4118, -3)
            )
            self.Container = [
                self.BackGround,
                self.Top,
                self.Bottom,
                self.Number,
                self.Price
            ]
        else:
            return self.Scroll()
    def Destroy_GUI(self, delay=0):
        sleep(delay)
        if self.Built:
            for item in self.Container:
                destroy(item)
            self.End = True
            self.Built = False
    def Scroll(self):
        if not self.Scrolling:
            self.Current = 1
            self.WinnerNumber = randint(1, 30)
            self.ScrollCount = self.WinnerNumber+(30*(randint(3, 6)))
            self.Scrolling = True
            return False
        elif self.ScrollCount > 0:
            self.ScrollCount -= 1
            self.Number.texture=f"assets\LotteryOpening\{self.Current}" if self.Current >= 10 else f"assets/LotteryOpening/0{self.Current}"
            self.Current += 1
            if self.Current>30:
                self.Current = 1
            return False
        else:
            self.Number.texture=f"assets\LotteryOpening\{self.WinnerNumber}" if self.WinnerNumber >= 10 else f"assets/LotteryOpening/0{self.WinnerNumber}"
            Thread(target=self.Destroy_GUI, args=[3]).start()
            return self.WinnerNumber

class ChooseLotteryButton(Button):
    def __init__(self, posX, posY, num, Owner, Choosed=False):
        super().__init__(
                    parent = camera.ui,
                    model = "circle",
                    position = (posX, posY, 0),
                    scale = 0.05,
                    text="{:0>2}".format(num),
                    highlight_color = rgb(183, 255, 191),
                    color = Owner.color if Owner else color.white,
                    text_color=color.black
                )
        self.number = num
        self.Choosed = Choosed
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if not self.Choosed:
                    self.color = color.yellow
                    self.Choosed = True

class LotteryTextArea(Button):
    def __init__(self, text):
        super().__init__( #Text Bar
            text=text,
            parent=camera.ui,
            model="quad",
            position=(0.0525, -0.2),
            scale=(0.45, 0.1, 0),
            text_color=color.black,
            color=color.white,
            disabled=True
        )

class LotteryPickRandomButton(Button):
    def __init__(self):
        super().__init__( #AutoPick Button
            parent=camera.ui,
            model="quad",
            text = "Random",
            position=(-0.25, -0.2),
            scale=(0.1, 0.1, 0),
            text_color=color.black,
            color=color.red,
        )
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseLottery():
    def __init__(self):
        self.OpenSystem = LotteryOpening()
        self.LotteryPrice = 1500
        self.WinningPrice = 0
        self.LotteryNumbers=[
            [ 1,  2,  3,  4,  5,  6],
            [ 7,  8,  9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30],
        ]
        self.ChoosedNumbers = {
             1:None, 2:None, 3:None, 4:None, 5:None, 6:None,
             7:None, 8:None, 9:None,10:None,11:None,12:None,
            13:None,14:None,15:None,16:None,17:None,18:None,
            19:None,20:None,21:None,22:None,23:None,24:None,
            25:None,26:None,27:None,28:None,29:None,30:None
        }
        self.Button_Container=[]
        self.Built = self.WinnerNumber = self.Announcing = False
    def Reset_Lottery(self):
        self.LotteryNumbers=[
            [ 1,  2,  3,  4,  5,  6],
            [ 7,  8,  9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30],
        ]
        self.ChoosedNumbers = {
             1:None, 2:None, 3:None, 4:None, 5:None, 6:None,
             7:None, 8:None, 9:None,10:None,11:None,12:None,
            13:None,14:None,15:None,16:None,17:None,18:None,
            19:None,20:None,21:None,22:None,23:None,24:None,
            25:None,26:None,27:None,28:None,29:None,30:None
        }
        self.WinningPrice = 0
        self.WinnerNumber = False
    def wipe(self, player):
        for number, owner in self.ChoosedNumbers.items():
            if owner == player:
                self.ChoosedNumbers[number] = None
    def Announcement(self, text):
        self.Announcement_Bar = Button(
            text=text,
            parent=camera.ui,
            model="quad",
            position=(0, 0.3, 5),
            scale=(1, 0.1, 1),
            text_color=color.black,
            color=color.white,
            disabled=True
        )
        self.Announcing = True
        Make_After(dic={"Announcing":self.Announcing}, key="Announcing", value=False, delay=3)
        destroy(self.Announcement_Bar, 3)
    def RandomPick(self):
        Can_Choose = [number for number, owner in self.ChoosedNumbers.items() if not owner]
        return Can_Choose[randint(0, len(Can_Choose)-1)]
    def Build_GUI(self):
        if not self.Built:
            self.Result = None
            self.BackGround = BackGround()
            self.LotteryBackGround = Entity(
                parent=camera.ui,
                model = "circle",
                scale = 1,
                position = (0, 0, 1),
                color = rgb(190, 160, 120),
            )
            self.TextArea = LotteryTextArea(f"Buy a Lottery Number with {self.LotteryPrice}$")
            self.Button_Container = [self.LotteryBackGround, LotteryPickRandomButton()]
            y = 0.3
            for num_list in self.LotteryNumbers:
                x = -0.25
                for number in num_list:
                    self.Button_Container.append(
                        ChooseLotteryButton(
                            posX=x,
                            posY=y,
                            num=number,
                            Owner=self.ChoosedNumbers[number],
                            Choosed=False if not self.ChoosedNumbers[number] else True
                        )
                    )

                    x+=0.1
                y-=0.1
        self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            destroy(self.BackGround.CloseButton)
            destroy(self.BackGround)
            for button in self.Button_Container:
                destroy(button)
            destroy(self.TextArea)
        self.Built = False
    def Check(self, Player):
        if self.BackGround.CloseButton.Close:
            self.Destroy_GUI()
            return True
        for button in self.Button_Container[2:]:
            if not self.ChoosedNumbers[button.number]:
                if button.Choosed:
                    self.Result = button.number
                    if Player.Property["Balance"] >= self.LotteryPrice:
                        self.ChoosedNumbers[self.Result] = Player
                        self.WinningPrice += self.LotteryPrice
                        Player.Property["Balance"] -= self.LotteryPrice
                    else:
                        self.Result = -1
                    self.Destroy_GUI()
                    return True
        if self.Button_Container[1].Choosed:
            self.Result = self.RandomPick()
            if Player.Property["Balance"] >= self.LotteryPrice:
                self.ChoosedNumbers[self.Result] = Player
                self.WinningPrice += self.LotteryPrice
                Player.Property["Balance"] -= self.LotteryPrice
            else:
                self.Result = -1
            self.Destroy_GUI()
            return True
        return False
    def Open(self):
        if not self.OpenSystem.End:
            self.WinnerNumber = self.OpenSystem.Open(self.WinningPrice)
            return False
        else:
            winner = self.ChoosedNumbers[self.WinnerNumber]
            if winner:
                winner.Announcement(text=f"Player_{winner.ID} Won Lottery Price {self.WinningPrice}$")
                winner.Property["Balance"] += self.WinningPrice
                self.Reset_Lottery()
            else:
                self.Announcement(text="No one Won the Lottery")
            return winner




#############################################################
"""
Magic GUI
"""
class ChooseMagicButton(Button):
    def __init__(self, posX, posY, Text):
        super().__init__(
                    parent = camera.ui,
                    model = "circle",
                    position = (posX, posY, 0),
                    scale = 0.1,
                    text=Text,
                    color = rgb(115, 96, 206),
                    text_color = color.black,
                    highlight_color = color.gray
                )
        self.event = Text
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseMagic():
    def __init__(self):
        self.Button_Container = []
        self.Built = False
        self.PlayerList = []
        self.Counter = 0
    def Build_GUI(self, PlayerList):
        if not self.Built:
            self.Counter = 0
            self.PlayerList = PlayerList
            self.Result = None
            self.BackGround = BackGround()
            self.Button_Container = [
                    ChooseMagicButton(
                        -0.30, 0.00, "Jail 3 Days"
                    ),
                    ChooseMagicButton(
                        -0.26, 0.15, "Deposit All Balance"
                    ),
                    ChooseMagicButton(
                        -0.15, 0.26, "Gain 3 Cards"
                    ),
                    # ChooseMagicButton(
                    #     -0.00, 0.30, "
                    # ),
                    ChooseMagicButton(
                        +0.15, 0.26, "Loss 3 Cards"
                    ),
                    ChooseMagicButton(
                        +0.26, 0.15, "Withdraw All Saving"
                    ),
                    ChooseMagicButton(
                        +0.30, 0.00, "Destroy 1 Building"
                    )
                ]
        self.Built = True
    def ChooseAndDisplay(self):
        PlayerList = self.PlayerList.copy()
        EffectHowManyPlayer = randint(0, len(PlayerList)-1)
        for _ in range(EffectHowManyPlayer):
            self.Result["target"].append(PlayerList.pop(randint(0, len(PlayerList)-1)))
        if EffectHowManyPlayer == 1:
            self.Button_Container.extend(
                [
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (0, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][0].color
                    )
                ]
            )
        elif EffectHowManyPlayer == 2:
            self.Button_Container.extend(
                [
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (0.1, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][0].color
                    ),
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (-0.1, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][1].color
                    )
                ]
            )
        elif EffectHowManyPlayer == 3:
            self.Button_Container.extend(
                [
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (0.20, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][0].color
                    ),
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (0, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][1].color
                    ),
                    Entity(
                        parent = camera.ui,
                        model = "quad",
                        position = (-0.20, -0.15, 0),
                        scale = 0.1,
                        color = self.Result["target"][2].color
                    )
                ]
            )
    def Destroy_GUI(self):
        if self.Built:
            for button in self.Button_Container:
                destroy(button)
            destroy(self.BackGround.CloseButton)
            destroy(self.BackGround)
        self.Built = False
    def Check(self):
        if not self.Result:
            for button in self.Button_Container[:6]:
                if button.Choosed or self.BackGround.CloseButton.Close:
                    self.Result = {"event":button.event, "target":[]}
        else:
            if self.Counter == 0:
                self.ChooseAndDisplay()
            self.Counter += 1
            if self.Counter > 100:
                self.Destroy_GUI()
                return True
        return False




#############################################################
"""
Choose Yes/No GUI
"""
class ChooseYesNoText(Button):
    def __init__(self, BG, text):
        super().__init__(
            parent=BG,
            model="quad",
            scale=(1, 0.25),
            position=(0, 0.25, 0),
            disabled=True,
            text_color=color.black,
            text=text,
            color=color.white
        )

class ChooseYesButton(Button):
    def __init__(self, BG):
        super().__init__(
            parent=BG,
            model="quad",
            scale=(0.5, 0.5),
            position=(-0.25, -0.25, 0),
            text_color=color.black,
            text="YES",
            color=color.white,
            highlight_color=color.gray
        )
        self.Choice = True
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseNoButton(Button):
    def __init__(self, BG):
        super().__init__(
            parent=BG,
            model="quad",
            scale=(0.5, 0.5),
            position=(0.25, -0.25, 0),
            text_color=color.black,
            text="NO",
            color=color.white,
            highlight_color=color.gray
        )
        self.Choice = False
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseYesNoBG(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.6, 0.25, 1)
        )

class ChooseYesNo():
    def __init__(self):
        self.Built = False
        self.Container = []
    def Build_GUI(self, text):
        if not self.Built:
            self.BG = ChooseYesNoBG()
            self.Text = ChooseYesNoText(BG=self.BG, text=text)
            self.YesButton = ChooseYesButton(BG=self.BG)
            self.NoButton = ChooseNoButton(BG=self.BG)
            self.Container = [self.BG, self.Text, self.YesButton, self.NoButton]
        self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            for item in self.Container:
                destroy(item)
        self.Built = False
    def Check(self):
        for button in self.Container[2:]:
            if button.Choosed:
                self.Destroy_GUI()
                self.Result = button.Choice
                return True
        return False




#############################################################
"""
Choose LargeBuilding GUI
"""
class ChooseLargeBuildingButton(Button):
    def __init__(self, posX, posY, texture):
        super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    texture=f"assets\LargeBuildingChooseTexture\{texture}",
                    position = (posX, posY, 0),
                    color = color.white,
                    scale = (0.48, 0.32, 1),
                    highlight_color = color.light_gray
                )
        self.Choice = texture
        self.Choosed = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class ChooseLargeBuilding():
    def __init__(self):
        self.Button_Container = []
        self.Built = False
    def Build_GUI(self, text=None):
        self.Button_Container = []
        if not self.Built:
            if text:
                self.Button_Container.append(
                    Button( #Text Bar
                        text=text,
                        parent=camera.ui,
                        model="quad",
                        position=(0, 0.42),
                        scale=(1, 0.1, 1),
                        text_color=color.black,
                        color=color.white,
                        disabled=True
                    )
                )
            self.Result = None
            self.BackGround = BackGround()
            self.Button_Container.extend(
                [
                        ChooseLargeBuildingButton(0.3, 0.2, "Hotel"),
                        ChooseLargeBuildingButton(0.3, -0.2, "Park"),
                        ChooseLargeBuildingButton(-0.3, 0.2, "StockExchange"),
                        ChooseLargeBuildingButton(-0.3, -0.2, "OilField")
                ]
            )
        self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            for button in self.Button_Container:
                destroy(button)
            destroy(self.BackGround.CloseButton)
            destroy(self.BackGround)
        self.Built = False
    def Check(self):
        for button in self.Button_Container[1:]:
            if button.Choosed or self.BackGround.CloseButton.Close:
                self.Destroy_GUI()
                self.Result = button.Choice
                return True
        return False




#############################################################
"""
Shop GUI
"""
class BuyCardButton(Button):
    def __init__(self, Card_Type, posX, posY):
        super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (posX, posY, 1),
                    color = color.white,
                    scale = (0.16, 0.28, 0),
                    highlight_color = color.light_gray,
                    text = f"{Card_Type.price}$",
                    text_origin = (0, -.46),
                    text_color = color.black
                )
        self.Choosed = False
        self.Card_Type = Card_Type
        self.Card_Image = Entity(
            parent = camera.ui,
            model = "quad",
            position = (posX, posY+0.02, 0),
            scale = (0.16, 0.24, 0),
            color = color.white,
            texture=load_texture(f"assets/CardTextures/{Card_Type.__name__}.png")
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Choosed = True

class BuyCardShop():
    def __init__(self):
        self.Button_Container = []
        self.Built = False
        self.Card_Types = [
                    BuyLandCard, 
                    # ChangeHouse, 
                    RebuildCard, 
                    RemoveHouse,
                    ControlDice, 
                    TurtleSpeed, 
                    TurnBackCrd, 
                    NotMoveCard,
                    MoveAtSleep, 
                    AGreatSleep, 
                    StopHereCrd, 
                    TheBombCard,
                    TheTimeBomb, 
                    # AMissleCard, 
                    # TheFreeCard, 
                    PaidTaxCard,
                    EvenPoorCrd, 
                    EvenRichCrd, 
                    TheStealCrd, 
                    TheTrapCard,
                    TheNoSinCrd, 
                    ClearMyRoad, 
                    BuildALevel, 
                    # TheNukeCard,
                    PayBackCard, 
                    FriendsCard
                ]
    def Build_GUI(self):
        if not self.Built:
            self.Result = None
            self.BackGround = BackGround()
            TemporaryTypeList = self.Card_Types.copy()
            StartY = 0.15
            for i in range(2):
                StartX = -0.3
                for k in range(4):
                    self.Button_Container.append(
                        BuyCardButton(TemporaryTypeList.pop(randint(0, len(TemporaryTypeList)-1)), StartX, StartY)
                    )
                    StartX += 0.2
                StartY = -StartY
        self.Built = True
    def Destroy_GUI(self):
        if self.Built:
            for button in self.Button_Container:
                destroy(button.Card_Image)
                destroy(button)
            destroy(self.BackGround.CloseButton)
            destroy(self.BackGround)
            self.Button_Container = []
        self.Built = False
    def Check(self):
        for button in self.Button_Container:
            if button.Choosed or self.BackGround.CloseButton.Close:
                self.Destroy_GUI()
                self.Result = button.Card_Type
                return True
        return False




#############################################################
"""
Bank GUI
"""
class BankBG(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(1, 1, 0),
            position=(0, 0, 2),
            color = rgb(195, 195, 195)
        )
        self.BackGround = BackGround()
        self.Container = [self.BackGround, self]

class BankDigitalScreen():
    def __init__(self, maxBalance, maxBank):
        self.TextArea = Button(
                parent=camera.ui,
                model="quad",
                disabled=True,
                text_color=color.black,
                text="|",
                text_origin=(0.5,0),
                scale=(0.825, 0.1, 0),
                position=(0, 0.35, 0),
                color = color.white
            )
        self.Container = [
            Entity(
                parent=camera.ui,
                model="quad",
                scale=(0.925, 0.2, 0),
                position=(0, 0.35, 1),
                color = color.black
            ),
            self.TextArea
        ]
        self.Withdraw = True
        self.Deposit = False
        self.maxBalance = maxBalance
        self.maxBank = maxBank
    def setMax(self):
        if self.Withdraw and not self.Deposit:
            self.TextArea.text = f"|{self.maxBank}"
        elif not self.Withdraw and self.Deposit:
            self.TextArea.text = f"|{self.maxBalance}"
    def Do_Withdraw(self):
        self.Withdraw = True
        self.Deposit = False
    def Do_Deposit(self):
        self.Withdraw = False
        self.Deposit = True
    def AddDigital(self, number_text):
        self.TextArea.text+=number_text
        if self.Withdraw and int(self.TextArea.text[1:])>self.maxBank:
            self.setMax()
        elif self.Deposit and int(self.TextArea.text[1:])>self.maxBalance:
            self.setMax()

class BankNumber():
    def __init__(self, DigitalScreen):
        self.DigitalScreen = DigitalScreen
        class BankNumberButtons(Button):
            def __init__(self, text, posX, posY, DigitalScreen):
                super().__init__(
                    parent=camera.ui,
                    model="circle",
                    scale=0.15,
                    text=text,
                    text_color=color.black,
                    position=(posX, posY, 1),
                    color = color.white
                )
                self.DigitalScreen = DigitalScreen
            def input(self, key):
                if self.hovered:
                    if key == "left mouse down":
                        self.DigitalScreen.AddDigital(self.text)
        startX = 0.05
        startY = 0.15
        t = 0
        self.Container = []
        for i in range(3):
            self.Container.extend([
                    BankNumberButtons(f"{t+1}", startX-0.4, startY, self.DigitalScreen),
                    BankNumberButtons(f"{t+2}", startX-0.2, startY, self.DigitalScreen),
                    BankNumberButtons(f"{t+3}", startX, startY, self.DigitalScreen)
                ]
            )
            startY-=0.18
            t+=3
        self.Container.extend([
                BankNumberButtons(f"00", startX-0.4, startY, self.DigitalScreen),
                BankNumberButtons(f"0", startX-0.2, startY, self.DigitalScreen),
                BankNumberButtons(f"000", startX, startY, self.DigitalScreen)
            ]
        )
        
class BankChooseWithdrawDeposit(Draggable):
    def __init__(self, DigitalScreen):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.125, 0.075, 0),
            position=(0.3625, 0.16, 0),
            lock_y = 1,
            max_x = 0.3625,
            min_x = 0.2375,
            text="Withdraw",
            text_color=color.black,
            color = color.red
        )
        self.Container = [
            self,
            Entity(
                parent=camera.ui,
                model="quad",
                scale=(0.25, 0.05, 0),
                position=(0.3, 0.16, 1),
                color = color.white
            )
        ]
        self.DigitalScreen = DigitalScreen
    def Turn_Withdraw(self):
        self.position = (self.max_x, self.position[1], self.position[2])
        self.color = color.red
        self.text = "Withdraw"
        self.DigitalScreen.Do_Withdraw()
        if self.DigitalScreen.TextArea.text[1:]:
            if int(self.DigitalScreen.TextArea.text[1:]) > self.DigitalScreen.maxBank:
                self.DigitalScreen.setMax()
    def Turn_Deposit(self):
        self.position = (self.min_x, self.position[1], self.position[2])
        self.color = rgb(15, 210, 70)
        self.text = "Deposit"
        self.DigitalScreen.Do_Deposit()
        if self.DigitalScreen.TextArea.text[1:]:
            if int(self.DigitalScreen.TextArea.text[1:]) > self.DigitalScreen.maxBalance:
                self.DigitalScreen.setMax()
    def drop(self):
        if self.position[0]>0.3:
            self.Turn_Withdraw()
        else:
            self.Turn_Deposit()

class BankChooseAll(Button):
    def __init__(self, DigitalScreen):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.25, 0.075, 0),
            position=(0.3, 0.02, 0),
            text="All",
            text_color=color.black,
            color = rgb(0, 170, 245)
        )
        self.Container = [self]
        self.DigitalScreen = DigitalScreen
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.DigitalScreen.setMax()

class BankClear(Button):
    def __init__(self, DigitalScreen):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.25, 0.075, 0),
            position=(0.3, -0.12, 0),
            text="Clear",
            text_color=color.black,
            color = rgb(255, 130, 40)
        )
        self.Container = [self]
        self.DigitalScreen = DigitalScreen
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.DigitalScreen.TextArea.text = "|"

class BankBackSpace(Button):
    def __init__(self, DigitalScreen):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.25, 0.075, 0),
            position=(0.3, -0.26, 0),
            text="BackSpace",
            text_color=color.black,
            color = color.yellow
        )
        self.Container = [self]
        self.DigitalScreen = DigitalScreen
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if len(self.DigitalScreen.TextArea.text)>1:
                    self.DigitalScreen.TextArea.text = self.DigitalScreen.TextArea.text[:-1]

class BankConfirm(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.25, 0.075, 0),
            position=(0.3, -0.4, 0),
            text="Confirm",
            text_color=color.black,
            color = rgb(255, 130, 40)
        )
        self.Container = [self]
        self.Confirm = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Confirm = True

class ShowBank():
    def __init__(self):
        self.Container = []
        self.Built = False
        self.Result = False

    def Build_GUI(self, player):
        if not self.Built:
            self.Built = True
            self.Result = False
            self.MaxBalance = player.Property["Balance"]
            self.MaxBank = player.Property["Bank"]
            self.BackGround = BankBG()
            self.DigitalScreen = BankDigitalScreen(maxBalance=self.MaxBalance, maxBank=self.MaxBank)
            self.ChooseWithdrawDeposit = BankChooseWithdrawDeposit(DigitalScreen=self.DigitalScreen)
            self.NumberButton = BankNumber(DigitalScreen=self.DigitalScreen)
            self.ChooseAllButton = BankChooseAll(DigitalScreen=self.DigitalScreen)
            self.ClearButton = BankClear(DigitalScreen=self.DigitalScreen)
            self.BackSpaceButton = BankBackSpace(DigitalScreen=self.DigitalScreen)
            self.ConfirmButton = BankConfirm()

            self.elements = [
                self.BackGround,
                self.DigitalScreen,
                self.ChooseWithdrawDeposit,
                self.NumberButton,
                self.ChooseAllButton,
                self.ClearButton,
                self.BackSpaceButton,
                self.ConfirmButton
            ]

            self.Container = []
            for element in self.elements:
                self.Container.extend(element.Container)
    
    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            destroy(self.Container[0].CloseButton)
            for element in self.Container:
                destroy(element)

    def Check(self):
        if self.ConfirmButton.Confirm or self.BackGround.BackGround.CloseButton.Close:
            if self.DigitalScreen.TextArea.text[1:]:
                self.Result = int(self.DigitalScreen.TextArea.text[1:])
            else:
                self.Result = 0
            print(self.Result)
            self.Destroy_GUI()
            return True




#############################################################
"""
News GUI
"""
class NewsAnnouncment():
    def __init__(self):
        self.Element_Container = []
        self.Built = False
        self.counter = 0
        self.News_Types = {
            "Ran in to a Car, Go Hospital for 3 Days":("HOSP", 3),
            "Got cought Stealing, Go Jail for 3 Days":("Jail", 3)
        }
    def Build_GUI(self, ui=None):
        if ui:
            if ui.Built:
                ui.Destroy_GUI()
        if not self.Built:
            self.Built = True
            self.counter = 0
            self.Picked_News = list(self.News_Types.keys()).copy().pop(randint(0, len(self.News_Types)-1))
            self.News_BackGround = Button(
                parent = camera.ui,
                position=(0, 0, 0),
                model = "quad",
                scale = (2, 1, 0),
                text = self.Picked_News,
                disabled = True,
                color = color.white,
                text_color = color.black,
                texture = "assets/Others/News"
            )
            self.Result = self.News_Types[self.Picked_News]
    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            destroy(self.News_BackGround)
    def Check(self):
        if self.counter > 200:
            self.Destroy_GUI()
            return True
        else:
            self.counter += time.dt * 60
        return False




#############################################################
class WaitDelay():
    def __init__(self):
        self.finish = True
    def Wait(self, duration=3):
        Thread(target=self.wait_function, args=[duration]).start()
    def wait_function(self, duration):
        self.finish = False
        sleep(duration)
        self.finish = True