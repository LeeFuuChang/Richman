from ursina import *




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
class IntroductionArea(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(1, 10, 0),
            color=color.white,
            texture="assets/HelpGUI/CardIntroduction",
            position=(0.2, -4.5, 0)
        )
        self.Max_Y = 4.5
        self.Min_Y = -4.5



class CardIntroductionButton(Button):
    def __init__(self, Introduction_Area, Reference):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=0.25,
            color=color.white,
            texture="assets/HelpGUI/CardIntroductionButton",
            position=(-0.6,0.3,0),
            highlight_color=color.gray
        )
        self.Reference = Reference
        self.Introduction_Area = Introduction_Area
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.scale = 0.2
                self.Introduction_Area.texture = self.Reference[self.__class__.__name__][0]
                self.Introduction_Area.scale = self.Reference[self.__class__.__name__][1]
                self.Introduction_Area.position = self.Reference[self.__class__.__name__][2]
                self.Introduction_Area.Max_Y = self.Reference[self.__class__.__name__][3]
                self.Introduction_Area.Min_Y = self.Reference[self.__class__.__name__][4]
        if key == "left mouse up":
            self.scale = 0.25



class BuildingIntroductionButton(Button):
    def __init__(self, Introduction_Area, Reference):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=0.25,
            color=color.white,
            texture="assets/HelpGUI/BuildingIntroductionButton",
            position=(-0.6,0,0),
            highlight_color=color.gray
        )
        self.Reference = Reference
        self.Introduction_Area = Introduction_Area

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.scale = 0.2
                self.Introduction_Area.texture = self.Reference[self.__class__.__name__][0]
                self.Introduction_Area.scale = self.Reference[self.__class__.__name__][1]
                self.Introduction_Area.position = self.Reference[self.__class__.__name__][2]
                self.Introduction_Area.Max_Y = self.Reference[self.__class__.__name__][3]
                self.Introduction_Area.Min_Y = self.Reference[self.__class__.__name__][4]
        if key == "left mouse up":
            self.scale = 0.25



class HTPIntroductionButton(Button):
    def __init__(self, Introduction_Area, Reference):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=0.25,
            color=color.white,
            texture="assets/HelpGUI/HTPIntroductionButton",
            position=(-0.6,-0.3,0),
            highlight_color=color.gray
        )
        self.Reference = Reference
        self.Introduction_Area = Introduction_Area

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.scale = 0.2
                self.Introduction_Area.texture = self.Reference[self.__class__.__name__][0]
                self.Introduction_Area.scale = self.Reference[self.__class__.__name__][1]
                self.Introduction_Area.position = self.Reference[self.__class__.__name__][2]
                self.Introduction_Area.Max_Y = self.Reference[self.__class__.__name__][3]
                self.Introduction_Area.Min_Y = self.Reference[self.__class__.__name__][4]
        if key == "left mouse up":
            self.scale = 0.25



class HelpGUI():
    def __init__(self):
        self.Reference = {
            "CardIntroductionButton":["assets/HelpGUI/CardIntroduction", (1, 10, 0), (0.2, -4.5, 0), 4.5, -4.5],
            "BuildingIntroductionButton":["assets/HelpGUI/BuildingIntroduction", (1, 2.5, 0), (0.2, -0.75, 0), 0.75, -0.75],
            "HTPIntroductionButton":["assets/HelpGUI/HTPIntroduction", (1, 3, 0), (0.2, -1, 0), 1, -1]
        }
        self.Built = False

    def HelpGUI_input(self, key):
        if key == "scroll down":
            self.Introduction_Area.y += 0.1
        if key == "scroll up":
            self.Introduction_Area.y -= 0.1
        if self.Introduction_Area.position[1] > self.Introduction_Area.Max_Y and key == "scroll down":
            self.Introduction_Area.y = self.Introduction_Area.Max_Y
        if self.Introduction_Area.position[1] < self.Introduction_Area.Min_Y and key == "scroll up":
            self.Introduction_Area.y = self.Introduction_Area.Min_Y
    
    def Build_GUI(self):
        if not self.Built:
            self.Built = True
            self.BackGround = BackGround()
            self.Introduction_Area = IntroductionArea()
            self.Card_Introduction_Button = CardIntroductionButton(Introduction_Area=self.Introduction_Area, Reference=self.Reference)
            self.Building_Introduction_Button = BuildingIntroductionButton(Introduction_Area=self.Introduction_Area, Reference=self.Reference)
            self.HTP_Introduction_Button = HTPIntroductionButton(Introduction_Area=self.Introduction_Area, Reference=self.Reference)
            self.Container = [
                self.BackGround, 
                self.BackGround.CloseButton, 
                self.Introduction_Area, 
                self.Card_Introduction_Button, 
                self.Building_Introduction_Button, 
                self.HTP_Introduction_Button
            ]
            return self.HelpGUI_input

    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            for Element in self.Container:
                destroy(Element)

    def Check(self):
        if self.BackGround.CloseButton.Close:
            self.Destroy_GUI()
            return True
        return False




#############################################################
class Settings_CloseButton(Button):
    def __init__(self, parent, position):
        super().__init__(
            parent = parent,
            model = "quad",
            scale = ((parent.scale[0])*0.2, (parent.scale[0]/parent.scale[1])*parent.scale[0]*0.2, 0),
            position = position,
            color = color.red,
            text = "X",
            text_color = color.white
        )
        self.Close = False
        self.Container = [self]
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Close = True



class slideBar(Draggable):
    def __init__(self, parent, Ypos, Xpos, startposition, endposition, BG_MusicPlayer=None, Effect_SoundPlayer=None):
        super().__init__(
            parent = parent,
            model = "circle",
            scale = ((parent.scale[0])*0.15, (parent.scale[0]/parent.scale[1])*parent.scale[0]*0.15, 0),
            position = (Xpos if Xpos else endposition, Ypos, -1),
            lock_y = 1,
            max_x = endposition,
            min_x = startposition,
            color = color.red
        )
        self.Container = [
            self,
            Entity(
                parent=parent,
                model="quad",
                scale=(0.8, (parent.scale[0]/parent.scale[1])*parent.scale[0]*0.05, 0),
                position=(0, Ypos, 0),
                color = color.gray
            )
        ]

        self.BG_MusicPlayer = BG_MusicPlayer
        self.Effect_SoundPlayer = Effect_SoundPlayer

        self.Length = endposition - startposition
        self.Ratio = 100 / self.Length

    def Bind_Controls(self, Main_Volume_Control=None, BG_Volume_Control=None, Effect_Volume_Control=None):
        self.Main_Volume_Control = Main_Volume_Control if Main_Volume_Control else self
        self.BG_Volume_Control = BG_Volume_Control if BG_Volume_Control else self
        self.Effect_Volume_Control = Effect_Volume_Control if Effect_Volume_Control else self

    def Get_value(self):
        return int((self.Ratio * self.position[0]) + 50)

    def drop(self):
        if self.BG_MusicPlayer:
            self.BG_MusicPlayer.set_volume((self.BG_Volume_Control.Get_value()*0.01)*(self.Main_Volume_Control.Get_value()*0.01))
        if self.Effect_SoundPlayer:
            for EffectPlayer in self.Effect_SoundPlayer:
                EffectPlayer.set_volume((self.Effect_Volume_Control.Get_value()*0.01)*(self.Main_Volume_Control.Get_value()*0.01))



class ChoiceButton(Button):
    def __init__(self, job, CurrentSize, parent, Xpos, Ypos, Window):
        super().__init__(
            parent = parent,
            model = "quad",
            position = (Xpos, Ypos, 0),
            scale = (0.8, 0.05, 0),
            color=color.white,
            highlight_color=color.light_gray
        )
        self.Window = Window
        self.Resolution = self.Window.screen_resolution
        self.Container = [self]

        self.Choosed = False
        self.disabled = False
        self.Current_Window_Size = str(CurrentSize)

        if job == "Fullscreen":
            self.do = self.input_FullScreen_Window

        elif job == "Border_Windowed":
            self.do = self.input_Border_Window

        elif job == "Borderless_Windowed":
            self.do = self.input_Borderless_Window

        elif job == "(3072, 1728)":
            if self.Resolution[0] < 3072 and self.Resolution[1] < 1728:
                self.disabled = True
                self.color = color.gray
            self.do = self.input_3072_1728

        elif job == "(1920, 1080)":
            if self.Resolution[0] < 1920 and self.Resolution[1] < 1080:
                self.disabled = True
                self.color = color.gray
            self.do = self.input_1920_1080
            
        elif job == "(1280, 720)":
            if self.Resolution[0] < 1280 and self.Resolution[1] < 720:
                self.disabled = True
                self.color = color.gray
            self.do = self.input_1280_720
        self.texture = f"assets\SettingsGUI\{job}"

    def do(self):
        pass

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if not self.disabled:
                    self.Choosed = True
                    self.do()

    def input_FullScreen_Window(self):
        window.borderless = window.fullscreen = True

    def input_Border_Window(self):
        window.borderless = window.fullscreen = False
        self.update_size()

    def input_Borderless_Window(self):
        self.Window.borderless = True
        self.Window.fullscreen = False
        self.update_size()

    def input_3072_1728(self):
        if not self.disabled:
            self.make_window_size(size=(3072, 1728))

    def input_1920_1080(self):
        if not self.disabled:
            self.make_window_size(size=(1920, 1080))

    def input_1280_720(self):
        if not self.disabled:
            self.make_window_size(size=(1280, 720))
    
    def update_size(self):
        if self.Current_Window_Size == str((3072, 1728)):
            self.input_3072_1728()
            return
        if self.Current_Window_Size == str((1920, 1080)):
            self.input_1920_1080()
            return
        if self.Current_Window_Size == str((1280, 720)):
            self.input_1280_720()
            return

    def make_window_size(self, size):
        self.Window.fullscreen = False
        self.Window.windowed_size = size
        self.Window.setSize(size)
        self.Current_Window_Size = str(self.Window.size)
        base.win.requestProperties(self.Window)
        self.update_center()
    
    def update_center(self):
        window_size = self.Window.size
        self.Window.position = (self.Resolution[0]//2-window_size[0]//2, self.Resolution[1]//2-window_size[1]//2)



class SettingsGUI():
    def __init__(self, BG_MusicPlayer, Effect_SoundPlayer, Window=window):

        self.BG_MusicPlayer = BG_MusicPlayer
        self.Effect_SoundPlayer = Effect_SoundPlayer
        self.Window = Window
        self.Current_Window_Size = self.Window.size

        self.Built = False

        self.Current_Main_positionX = 0
        self.BG_Music_positionX = 0
        self.Effect_Music_positionX = 0

    def Build_GUI(self):
        if not self.Built:
            self.Built = True
            self.BG = Entity(
                parent=camera.ui,
                model="quad",
                scale=(0.4, 0.8),
                position=(0, 0, 1),
                texture="assets/SettingsGUI/SettingsBG"
            )
            self.closeButton = Settings_CloseButton(parent=self.BG, position=(0.45, 0.475, 0))
            
            
            
            #Sound Volume control
            self.Main_Volume_drag = slideBar(parent=self.BG, Ypos=0.375, Xpos=self.Current_Main_positionX, BG_MusicPlayer=self.BG_MusicPlayer, Effect_SoundPlayer=self.Effect_SoundPlayer, startposition=-0.4, endposition=0.4)
            self.BG_Music_Volume_drag = slideBar(parent=self.BG, Ypos=0.23, Xpos=self.BG_Music_positionX, BG_MusicPlayer=self.BG_MusicPlayer, Effect_SoundPlayer=self.Effect_SoundPlayer, startposition=-0.4, endposition=0.4)
            self.Effect_Music_Volume_drag = slideBar(parent=self.BG, Ypos=0.08, Xpos=self.Effect_Music_positionX, BG_MusicPlayer=self.BG_MusicPlayer, Effect_SoundPlayer=self.Effect_SoundPlayer, startposition=-0.4, endposition=0.4)

            self.Container = [
                self.closeButton, self.Main_Volume_drag, self.BG_Music_Volume_drag, self.Effect_Music_Volume_drag,
            ]

            for Dragger in self.Container[1:4]:
                Dragger.Bind_Controls(
                    Main_Volume_Control=self.Main_Volume_drag, BG_Volume_Control=self.BG_Music_Volume_drag, Effect_Volume_Control=self.Effect_Music_Volume_drag
                )

            self.Main_Volume_drag.drop()



            #Window control
            self.Current_Window_Size = window.size

            Fullscreen_Control = ChoiceButton(job="Fullscreen", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.08, Window=self.Window)
            Border_Windowed_Control = ChoiceButton(job="Border_Windowed", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.13, Window=self.Window)
            Borderless_Windowed_Control = ChoiceButton(job="Borderless_Windowed", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.18, Window=self.Window)
            Window_3072_1728_Control = ChoiceButton(job="(3072, 1728)", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.34, Window=self.Window)
            Window_1920_1080_Control = ChoiceButton(job="(1920, 1080)", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.40, Window=self.Window)
            Window_1280_720_Control = ChoiceButton(job="(1280, 720)", CurrentSize=self.Current_Window_Size, parent=self.BG, Xpos=0, Ypos=-0.46, Window=self.Window)

            self.Container.extend([
                Fullscreen_Control,
                Border_Windowed_Control,
                Borderless_Windowed_Control,
                Window_3072_1728_Control,
                Window_1920_1080_Control,
                Window_1280_720_Control
            ])

            if window.screen_resolution[0]>3072 and window.screen_resolution[1]>1728:
                Window_3072_1728_Control.do()
            elif window.screen_resolution[0]>1920 and window.screen_resolution[1]>1080:
                Window_1920_1080_Control.do()
            elif window.screen_resolution[0]>1280 and window.screen_resolution[1]>720:
                Window_1280_720_Control.do()

    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            destroy(self.BG)
            for Elements in self.Container:
                for element in Elements.Container:
                    destroy(element)

    def Check(self):
        self.Current_Main_positionX = self.Main_Volume_drag.position[0]
        self.BG_Music_positionX = self.BG_Music_Volume_drag.position[0]
        self.Effect_Music_positionX = self.Effect_Music_Volume_drag.position[0]
        
        if self.closeButton.Close:
            self.Destroy_GUI()
            return True
        return False




#############################################################