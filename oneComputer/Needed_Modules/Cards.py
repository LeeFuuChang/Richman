"""
卡片物件導向檔案
"""
from random import randint
from ursina import *
from .CardSystems import *



UseCardSystem = {
    "ChooseTarget":None,
    "ChoosePoint":None,
    "ChooseYesNo":None,
    "Close":None
}



def Make_Card_Use_System(syst):
    global UseCardSystem
    UseCardSystem = syst



class TurnBackCrd(Button): #轉向卡
    #讓周圍任意一名角色聽你的話，向後轉！
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Choosed = False
                self.Owner.UI.Clear_Used_Card()
                PreUseResult.Turn()
                destroy(self)
            self.Choosed = False
            return True



class ControlDice(Button): #遙控骰子卡
    #用遙控骰子投出你中意的數字吧。除了醫院和監獄的岔路口不能走，別的岔路口任你選擇。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChoosePoint"].Built:
            UseCardSystem["ChoosePoint"].Build_GUI()
        else:
            if UseCardSystem["ChoosePoint"].Check():
                if not UseCardSystem["ChoosePoint"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChoosePoint"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.Property["Status"]["point"] = PreUseResult
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class BuyLandCard(Button): #買地卡
    #強制收購任何所在土地的房屋，既然要買那麼土地價和加蓋價格就一起付清吧。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseYesNo"].Built:
            CurrentLand = self.Owner.MapBindings.get((self.Owner.MapPosZ, self.Owner.MapPosX), False)
            if CurrentLand:
                if CurrentLand.Owner: #If the Land has a Owner
                    CurrentLandOwner = CurrentLand.Owner.ID
                    CurrentLandLevel = CurrentLand.Level
                    DisplayText = f"TakeOver Player_{CurrentLandOwner}\'s Land? (with {CurrentLand.__class__.__name__} level: {CurrentLandLevel}"
                    UseCardSystem["ChooseYesNo"].Build_GUI(text=DisplayText)
                    return False
                else: #No Owner
                    self.Owner.Announcement("This Land has no Owner!")
                    return -1
            else: #Not Ownable
                self.Owner.Announcement("You can't use this Card here!")
                return -1
        else:
            if UseCardSystem["ChooseYesNo"].Check():
                if UseCardSystem["ChooseYesNo"].Result:
                    return 1
                else:
                    return 0
            return False
    def Use(self, PreUseResult):
        if type(PreUseResult) != bool:
            if PreUseResult == -1 or PreUseResult == 0:
                self.Choosed = False
            else:
                self.Can_Use = False
                CurrentLand = self.Owner.MapBindings[(self.Owner.MapPosZ, self.Owner.MapPosX)]
                CurrentLand.Owner = self.Owner
                CurrentLand.Building.color = self.Owner.color
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            return True



class RebuildCard(Button): #改建卡
    #把你所在格房屋變更成任何項目，可以反復變更。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseYesNo"].Built:
            CurrentLand = self.Owner.MapBindings.get((self.Owner.MapPosZ, self.Owner.MapPosX), False)
            if CurrentLand.__class__.__name__ == "LargeBuilding":
                if CurrentLand.Owner: #If the Land has a Owner
                    CurrentLandOwner = CurrentLand.Owner.ID
                    DisplayText = f"Rebuild Player_{CurrentLandOwner}\'s Land to a Park?"
                    UseCardSystem["ChooseYesNo"].Build_GUI(text=DisplayText)
                    return False
                else:
                    self.Owner.Announcement("This Land has no Owner!")
                    return -1 #No Owner
            else:
                self.Owner.Announcement("You can only use this card at LargeBuilding Plot!")
                return -1 #Not Ownable
        else:
            if UseCardSystem["ChooseYesNo"].Check():
                if UseCardSystem["ChooseYesNo"].Result:
                    return 1 #Choose Yes
                else:
                    return 0 #Choose No
            return False
    def Use(self, PreUseResult):
        if type(PreUseResult) != bool:
            if PreUseResult == 0 or PreUseResult == -1:
                self.Choosed = False
                return True
            self.Can_Use = False
            CurrentLand = self.Owner.MapBindings.get((self.Owner.MapPosZ, self.Owner.MapPosX), False)
            CurrentLand_Owner = CurrentLand.Owner
            CurrentLand_posX = CurrentLand.Building.position[0]
            CurrentLand_posZ = CurrentLand.Building.position[2]
            CurrentLand_Rotation_Y = CurrentLand.Building.rotation_y
            destroy(CurrentLand.Building)
            CurrentLand.Building = CurrentLand.Building_Types["Park"](posX=CurrentLand_posX, posZ=CurrentLand_posZ,
                Owner=CurrentLand_Owner, rotate=CurrentLand_Rotation_Y)
            self.Owner.UI.Clear_Used_Card()
            destroy(self)
            return True



class TheTimeBomb(Button): #定時炸彈卡
    #路過後定時炸彈就會纏著你，被它炸傷要住院4天。爆炸會使旁邊建築降低2級，想辦法在30步內擺脫它或者可以路過送給別人！
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Carry_Time_Bomb(Steps=30)
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TheTrapCard(Button): #陷害卡
    #陷害周圍的敵人讓他立刻入獄3天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Go_Jail(Rounds=3)
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TheStealCrd(Button): #偷盜卡
    #從周圍角色手中隨機搶奪一張手卡，切記如果對方沒有手卡可是會搶奪失敗的。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                target_Owned_Cards = [card for card, amount in PreUseResult.Property["OwnCard"].items() if amount > 0]
                target_Owned_Cards_length = len(target_Owned_Cards)
                if target_Owned_Cards_length > 0:
                    picked_Card = target_Owned_Cards[randint(0, target_Owned_Cards_length-1)]
                    self.Owner.AddCard(Amount=1, Type=picked_Card)
                    PreUseResult.Property["OwnCard"][picked_Card] -= 1
                    PreUseResult.UI.refresh()
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class NotMoveCard(Button): #停留卡
    #把周圍任意角色冰凍在原地1天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Property["SpecialEffect"][self.__class__.__name__] = 1
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TurtleSpeed(Button): #烏龜卡
    #召喚烏龜附身在周圍任何一一個人身上，被附身後只能一步-步爬。效果持續3天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Property["SpecialEffect"][self.__class__.__name__] = 3
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class PayBackCard(Button): #還貸卡
    #從指定敵人處獲得20%存款。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                amount = int(PreUseResult.Property["Bank"]*0.2)
                PreUseResult.Property["Bank"] -= amount
                self.Owner.Property["Balance"] += amount
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class PaidTaxCard(Button): #查稅卡
    #從指定敵人處獲得15%現金。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                amount = int(PreUseResult.Property["Balance"]*0.15)
                PreUseResult.Property["Balance"] -= amount
                self.Owner.Property["Balance"] += amount
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class EvenPoorCrd(Button): #均貧卡
    #與所有在場角色平均存款。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseYesNo"].Built:
            UseCardSystem["ChooseYesNo"].Build_GUI(text=f"Sure to Even All Player's Bank?")
        else:
            if UseCardSystem["ChooseYesNo"].Check():
                if UseCardSystem["ChooseYesNo"].Result:
                    return UseCardSystem["ChooseTarget"].Get_All_Player()
                else:
                    return True
            else:
                return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                Total_Bank = 0
                for Player in PreUseResult:
                    Total_Bank += Player.Property["Bank"]
                Evened_Bank = Total_Bank//len(PreUseResult)
                for Player in PreUseResult:
                    Player.Property["Bank"] = Evened_Bank
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class EvenRichCrd(Button): #均富卡
    #與所有在場角色平均現金。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseYesNo"].Built:
            UseCardSystem["ChooseYesNo"].Build_GUI(text=f"Sure to Even All Player's Balance?")
        else:
            if UseCardSystem["ChooseYesNo"].Check():
                if UseCardSystem["ChooseYesNo"].Result:
                    return UseCardSystem["ChooseTarget"].Get_All_Player()
                else:
                    return True
            else:
                return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                Total_Balance = 0
                for Player in PreUseResult:
                    Total_Balance += Player.Property["Balance"]
                Evened_Balance = Total_Balance//len(PreUseResult)
                for Player in PreUseResult:
                    Player.Property["Balance"] = Evened_Balance
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class MoveAtSleep(Button): #夢游卡
    #讓周圍一名角色進入夢游狀態，睡覺的時候就要安心睡覺哦。效果持續3天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Property["SpecialEffect"][self.__class__.__name__] = 3
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class AGreatSleep(Button): #冬眠卡
    #凜冬將至!指定任何一名角色進入冬眠狀態。待在原地睡個好覺吧。效果持續3天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                PreUseResult.Property["SpecialEffect"][self.__class__.__name__] = 3
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TheNoSinCrd(Button): #免罪卡
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        self.Owner.Announcement("This Card can't be manually used")
        return True
    def Use(self, PreUseResult):
        if PreUseResult:
            self.Choosed = False
            return True



class BuildALevel(Button): #建造卡
    #機器工人可以幫你加蓋1層周圍指定任意己方房屋。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseYesNo"].Built:
            UseCardSystem["ChooseYesNo"].Build_GUI(text=f"Sure to Upgrade the Building?")
        else:
            if UseCardSystem["ChooseYesNo"].Check():
                if UseCardSystem["ChooseYesNo"].Result:
                    Current_Land = self.Owner.MapBindings.get((self.Owner.MapPosZ, self.Owner.MapPosX), False)
                    if Current_Land.__class__.__name__ == "SmallBuilding":
                        if Current_Land.Owner == self.Owner:
                            if Current_Land.Building.Level < Current_Land.Building.MaxLevel:
                                Current_Land.Building.upgrade()
                                return 1
                            else:
                                self.Owner.Announcement(f"The Building has reached Max Level")
                                return True
                        else:
                            self.Owner.Announcement(f"You does not Own this land")
                            return True
                    else:
                        self.Owner.Announcement(f"This Card can only be used at SmallBuilding")
                        return True
                else:
                    return True
            else:
                return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class ClearMyRoad(Button): #整路卡
    #機器娃娃可以幫你掃清前方10步內所有的神仙、地雷、野狗、乞丐等障礙物。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
        self.AskConfirm = False
        self.CleanBot = None
        self.frameCounter = -10
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if self.AskConfirm:
            return self.Play_CleanBot()
        else:
            if not UseCardSystem["ChooseYesNo"].Built:
                UseCardSystem["ChooseYesNo"].Build_GUI(text=f"Clean 10 Blocks in front of you?")
            else:
                if UseCardSystem["ChooseYesNo"].Check():
                    if UseCardSystem["ChooseYesNo"].Result:
                        self.AskConfirm = True
                        if not self.CleanBot:
                            self.CleanBot = CleanBot(
                                Owner=self.Owner, 
                                map=self.Owner.MAP, 
                                mapWidth=self.Owner.MapWidth,
                                mapHeight=self.Owner.MapHeight,
                                Walkable_Bindings=self.Owner.Walkable_Bindings,
                                direction=self.Owner.direction,
                                start=self.Owner.position,
                                speed=1
                            )
                            self.CleanBot.Camera_Follow()
                    else:
                        return True
    def Play_CleanBot(self):
        self.frameCounter += 1
        if self.frameCounter%15 == 0 and self.frameCounter>0:
            return self.CleanBot.move()
        else:
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class StopHereCrd(Button): #路障卡
    #路障已放好，到此停止！
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
        self.CloseButton = None
        self.Choosing = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not self.CloseButton:
            self.CloseButton = Close_Button()
        if not self.Choosing:
            for block in self.Owner.Walkable_Bindings.values():
                if not any(player.position[0]==block.position[0] and player.position[2]==block.position[2] for player in self.Owner.OtherPlayer+[self.Owner]):
                    block.Choosing = True
            self.Choosing = True
        for block in self.Owner.Walkable_Bindings.values():
            if block.Choosed == True:
                block.Stop = Entity(
                    model = "Stop",
                    scale = .25,
                    position = (block.position[0], block.position[1]+0.25, block.position[2]),
                    color = self.Owner.color
                )
                block.Choosed = False
                for block in self.Owner.Walkable_Bindings.values():
                    block.Choosing = False
                destroy(self.CloseButton)
                self.CloseButton = None
                return 1
            elif self.CloseButton.Choosed:
                destroy(self.CloseButton)
                self.CloseButton = None
                return True
        return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            self.Choosing = False
            return True



class RemoveHouse(Button): #工程車卡
    #召喚工程車拆除周圍1層房屋。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
        self.CloseButton = None
        self.Choosing = False
        self.ChoosingBlocks = []
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not self.CloseButton:
            self.CloseButton = Close_Button()
        if not self.Choosing:
            self.ChoosingBlocks = []
            for Coordnate, Class in self.Owner.MapBindings.items():
                if Class.__class__.__name__ == "LargeBuilding" or Class.__class__.__name__ == "SmallBuilding":
                    self.Owner.Walkable_Bindings[Coordnate].Choosing = True
                    self.ChoosingBlocks.append(self.Owner.Walkable_Bindings[Coordnate])
            self.Choosing = True
        for block in self.ChoosingBlocks:
            if block.Choosed == True:
                self.Owner.MapBindings[block.ArrBinding].Downgrade()
                block.Choosed = False
                for block in self.ChoosingBlocks:
                    block.Choosing = False
                destroy(self.CloseButton)
                self.CloseButton = None
                return 1
            elif self.CloseButton.Choosed:
                destroy(self.CloseButton)
                self.CloseButton = None
                return True
        return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TheBombCard(Button): #炸彈卡
    #放置一個炸藥碰到人就炸，被炸傷者需要住院1天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
        self.CloseButton = None
        self.Choosing = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not self.CloseButton:
            self.CloseButton = Close_Button()
        if not self.Choosing:
            for block in self.Owner.Walkable_Bindings.values():
                if not any(player.position[0]==block.position[0] and player.position[2]==block.position[2] for player in self.Owner.OtherPlayer+[self.Owner]):
                    block.Choosing = True
            self.Choosing = True
        for block in self.Owner.Walkable_Bindings.values():
            if block.Choosed == True:
                block.Bomb = Entity(
                    model = "Bomb",
                    scale = .25,
                    position = (block.position[0], block.position[1]+0.25, block.position[2]),
                    color = self.Owner.color
                )
                block.Choosed = False
                for block in self.Owner.Walkable_Bindings.values():
                    block.Choosing = False
                destroy(self.CloseButton)
                self.CloseButton = None
                return 1
            elif self.CloseButton.Choosed:
                destroy(self.CloseButton)
                self.CloseButton = None
                return True
        return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            self.Choosing = False
            return True



class FriendsCard(Button): #損友卡
    #與周圍的敵人冰釋前嫌做回朋友吧，互不收取過路費。效果持續7天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                PreUseResult.Make_Friends(Player=self.Owner, Rounds=7)
                self.Owner.Make_Friends(Player=PreUseResult, Rounds=7)
                self.Owner.Announcement(f"Player_{self.Owner.ID} is now Friend with Player_{PreUseResult.ID}")
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



########################################################################################################未完成vvvvvvv
class TheFreeCard(Button): #免費卡
    #當損失超過5000元可以用它獲得免費機會哦。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nError UnFinished Card Called\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        quit()
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        return True
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class ChangeHouse(Button): #換屋卡
    #嫌自己的房子小了？用自己的房子和敵人的房子交換吧。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nError UnFinished Card Called\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        quit()
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        return True
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class AMissleCard(Button): #飛彈卡
    #發射飛彈，炸傷目標和3×3范圍內所有東西。被炸傷的人住院2天、房子降低1級，還會引爆范圍內其他地雷和炸藥。發射飛彈，炸傷目標和3×3范圍內所有東西。被炸傷的人住院2天、房子降低1級，還會引爆范圍內其他地雷和炸藥。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nError UnFinished Card Called\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        quit()
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True



class TheNukeCard(Button): #核彈卡
    #向指定地點發射核彈，核彈會徹底摧毀、引爆5×5范圍內的所有房子、地雷和炸藥。范圍內的角色也會因輻射入院5天。
    price = 2500
    def __init__(self, Owner=None, ui=None, Xpos=0, disabled=False):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nError UnFinished Card Called\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        quit()
        if ui:
            super().__init__(
                    parent = camera.ui,
                    model = "quad",
                    position = (Xpos, -0.35, 0),
                    scale = (0.16, 0.24, 0),
                    color = color.white,
                    highlight_color = color.gray,
                    texture=load_texture(f"assets/CardTextures/{self.__class__.__name__}.png")
                )
            self.disabled = disabled
            self.rotation_z = 25
            self.UI = ui
        self.Owner = Owner
        self.Can_Use = True
        self.Choosed = False
    def input(self, key):
        if not self.disabled and not self.Choosed:
            if self.hovered:
                if key == "left mouse down":
                    print(f"use {self.__class__.__name__}")
                    self.scale = (0.12, 0.18, 1)
            if key == "left mouse up":
                if self.hovered:
                    self.Choosed = True
                self.scale = (0.16, 0.24, 0)
    def PreUse(self):
        if not UseCardSystem["ChooseTarget"].Built:
            UseCardSystem["ChooseTarget"].Build_GUI()
        else:
            if UseCardSystem["ChooseTarget"].Check():
                if not UseCardSystem["ChooseTarget"].BackGround.CloseButton.Close:
                    return UseCardSystem["ChooseTarget"].Result
                else:
                    return True
            return False
    def Use(self, PreUseResult):
        if PreUseResult:
            if type(PreUseResult) != bool:
                self.Can_Use = False
                self.Owner.UI.Clear_Used_Card()
                destroy(self)
            self.Choosed = False
            return True