"""
各類物件檔案
"""
###########################################################################
#-----------------------------Line References-----------------------------#
#-------------------------------------------------------------------------#
#---Player and Entity Classes:-----------------------------------Line:0067#
#------Entity Classes--------------------------------------------Line:0072#
#------Player Classes--------------------------------------------Line:0308#
#-------------------------------------------------------------------------#
#---Building and Map Classes:------------------------------------Line:0778#
#------Large House Classes---------------------------------------Line:0783#
#------Small House Classes---------------------------------------Line:0840#
#------Map Block Classes-----------------------------------------Line:0910#
#------Map Classes-----------------------------------------------Line:1296#
#------Map Builder Class-----------------------------------------Line:1901#
#-------------------------------------------------------------------------#
###########################################################################
from random import randint
from ursina import *
from .Cards import *
from threading import Thread as T
from time import sleep as wait




def Print(sent):
    sents = sent.split("\n")
    maxlen = max([len(_) for _ in sents])
    print("\n"+"-"*(maxlen+2))
    for _ in sents:
        print("|"+_+" "*(maxlen-len(_))+"|")
    print("-"*(maxlen+2))
    return sent




def Make_After(dic, key, value, delay):
    def Make_var():
        wait(delay)
        dic[key] = value
    T(target=Make_var).start()




system = {
    "ChooseTarget":0,
    "ChooseLargeBuilding":0,
    "ChooseLottery":0,
    "ChooseMagic":0,
    "ChooseYesNo":0,
    "ShowNews":0,
    "ShowShop":0,
    "ShowBank":0,
    "ShowGame":1
}
def Make_System(syst):
    global system
    system = syst







################################################################################################################################################
################################################################################################################################################
####                                                                                                                                        ####
####--------------------------------------------------------Player and Entity Classes-------------------------------------------------------####
####                                                                                                                                        ####
################################################################################################################################################
################################################################################################################################################
###########################################################################
#------------------------------Entity Classes-----------------------------#
###########################################################################
class Dice(Entity):
    def __init__(self, pos=(0, 0, 0), Scale=0.1, Color=color.white, Model="CubeModel"):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = "assets/Dice/dice",
            color = Color,
            scale = Scale
        )
        self.Dice_Animation = False

    def Animation(self, Point, n=20):
        alpha = 360*randint(1, 10) #變化量
        DICE_ROTATION = { #基礎轉動量
            "2":(0, 0, 0),
            "5":(90, 0, 0),
            "3":(0, 0, 90),
            "6":(180, 0, 0),
            "4":(0, 0, 270),
            "1":(270, 0, 0)
        }
        Stop = ( #停止轉動量
            DICE_ROTATION[str(Point)][0],
            DICE_ROTATION[str(Point)][1],
            DICE_ROTATION[str(Point)][2]
        )
        D = ( #等差數列公差
            (((Stop[0]+alpha)*2) / n) / (n-1),
            (((Stop[1]+alpha)*2) / n) / (n-1),
            (((Stop[2]+alpha)*2) / n) / (n-1)
        )
        if not self.Dice_Animation: #初始化等差級數
            self.Dice_Animation = n #n
            self._Sum = [0, 0, 0] #<a> <b> <c>
        self._Sum[0] += D[0] #加一個公差
        self._Sum[1] += D[1] #加一個公差
        self._Sum[2] += D[2] #加一個公差
        self.rotation_x += self._Sum[0] #加入級數和
        self.rotation_y += self._Sum[1] #加入級數和
        self.rotation_z += self._Sum[2] #加入級數和
        self.Dice_Animation-=1 #紀錄還需要加幾項
        if self.Dice_Animation==0: #如果級數和算玩了 => 骰子轉動完畢
            #如果跟我們要的面相差過大 則強制固定到需要的面
            if abs(self.rotation_x%360 - Stop[0]) >= 10 and abs(self.rotation_y%360 - Stop[1]) >= 10 and abs(self.rotation_z%360 - Stop[2]) >= 10:
                self.rotation_x = Stop[0] #固定到需要的面
                self.rotation_y = Stop[1] #固定到需要的面
                self.rotation_z = Stop[2] #固定到需要的面
            self.Dice_Animation = False  #恢復False等待下次使用
            return True
        else:
            return False





###########################################################################
#-------------------------------GUI Classes-------------------------------#
###########################################################################
class Exit_Button(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.075, 0.03, 0),
            position=(0.8375, 0.475, 0),
            text_color=color.black,
            text="Exit",
            color=color.white
        )
        self.Container = [self]
        self.Represent = "Exit"
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

class Settings_Button(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.075, 0.03, 0),
            position=(0.7375, 0.475, 0),
            texture="assets/MainGUI/Settings",
            color=color.white
        )
        self.Container = [self]
        self.Represent = "Adjust"
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

class Tutorial_Button(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.075, 0.03, 0),
            position=(0.6375, 0.475, 0),
            texture="assets/MainGUI/Help",
            color=color.white
        )
        self.Container = [self]
        self.Represent = "Help"
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

class Property_Button(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.075, 0.03, 0),
            position=(0.5375, 0.475, 0),
            texture="assets/MainGUI/Property",
            color=color.white
        )
        self.Container = [self]
        self.Represent = "Owns"
        self.Clicked = False
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.Clicked = True

class Show_Wallet(Button):
    def __init__(self, Balance):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.2125, 0.03, 0),
            position=(0.13125, 0.475, 0),
            disabled=True,
            text_color=color.black,
            text_origin=(0.45,0),
            text=f"{Balance}",
            color=color.white
        )
        self.Wallet_Text = Button(
            parent = self,
            model = "quad",
            scale=(0.4, 1, 0),
            position=(-0.325, 0, 0),
            disabled=True,
            text_color=color.black,
            text="Wallet:",
            color=color.white
        )
        self.Container = [self, self.Wallet_Text]

class Show_Bank(Button):
    def __init__(self, Bank):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(0.2125, 0.03, 0),
            position=(0.36875, 0.475, 0),
            disabled=True,
            text_color=color.black,
            text_origin=(0.45,0),
            text=f"{Bank}",
            color=color.white
        )
        self.Bank_Text = Button(
            parent = self,
            model = "quad",
            scale=(0.4, 1, 0),
            position=(-0.325, 0, 0),
            disabled=True,
            text_color=color.black,
            text="Bank:",
            color=color.white
        )
        self.Container = [self, self.Bank_Text]

class Option_Bar(Entity):
    def __init__(self, Balance, Bank):
        super().__init__(
            parent=camera.ui,
            model="quad",
            scale=(1, 0.05, 0),
            position=(0.5, 0.475, 1),
            color = color.gray
        )
        self.Option_Bar_Container = [self]
        self.Show_Wallet = Show_Wallet(Balance=Balance)
        self.Option_Bar_Container.extend(self.Show_Wallet.Container)
        self.Show_Bank = Show_Bank(Bank=Bank)
        self.Option_Bar_Container.extend(self.Show_Bank.Container)
        self.Exit_Button = Exit_Button()
        self.Option_Bar_Container.extend(self.Exit_Button.Container)
        self.Settings_Button = Settings_Button()
        self.Option_Bar_Container.extend(self.Settings_Button.Container)
        self.Tutorial_Button = Tutorial_Button()
        self.Option_Bar_Container.extend(self.Tutorial_Button.Container)
        self.Property_Button = Property_Button()
        self.Option_Bar_Container.extend(self.Property_Button.Container)

class GUI():
    def __init__(self, Owner, PlayerProperty=None):
        self.Built = False
        self.UIOwner = Owner

        self.Card_Types = self.UIOwner.Property["OwnCard"]
        self.Start = -0.47
        self.Distance = 0.2
        self.Current = -0.47
        self.Card_Container = []

    def Build_GUI(self):
        if not self.Built:
            self.Card_Types = self.UIOwner.Property["OwnCard"]
            self.Built = True
            self.Card_Container = []
            Owner_Balance = self.UIOwner.Property["Balance"]
            Owner_Bank = self.UIOwner.Property["Bank"]
            self.Option_Bar = Option_Bar(Balance=Owner_Balance, Bank=Owner_Bank)
            class RollDice(Button):
                def __init__(self):
                    super().__init__(
                        parent = camera.ui,
                        model = "circle",
                        position = (0.8, -0.4, 1),
                        scale = 0.28,
                        color = color.white,
                        highlight_color = color.gray
                    )
                    self.Go=False
                def input(self, key):
                    if self.hovered:
                        if key == "left mouse down":
                            self.Go = True

            self.Elements = {
                "CardTable" : (
                        Entity(
                            parent = camera.ui,
                            model = "quad",
                            position = (0, -0.5, 3),
                            scale = (2, .25, 0),
                            color = color.white
                        )
                    ),
                "Icon" : (
                        Entity(
                            parent = camera.ui,
                            model = "circle",
                            position = (-0.8, -0.4, 0),
                            scale = 0.4,
                            color = self.UIOwner.color
                        )
                    ),
                "DiceBackGround" : (
                        Entity(
                            parent = camera.ui,
                            model = "circle",
                            position = (0.8, -0.4, 2),
                            scale = 0.32,
                            color = color.black
                        )
                    ),
                "DiceButton" : (
                        RollDice()
                    ),
                "DiceImage" : (
                        Entity(
                            parent = camera.ui,
                            model = "quad",
                            position = (0.79, -0.4, 0),
                            scale = 0.2,
                            texture = load_texture("assets/Dice/RollDice.png")
                        )
                    )
            }
            self.RD = self.Elements["DiceButton"]
            for Type, quantity in self.Card_Types.items():
                for i in range(quantity):
                    self.Make_Card(Type)

    def Destroy_GUI(self):
        if self.Built:
            self.Built = False
            for element in self.Elements.values():
                destroy(element)
            for item in self.Option_Bar.Option_Bar_Container:
                destroy(item)
            for Card in self.Card_Container:
                destroy(Card)

    def Make_Card(self, Type):
        NowHave = len(self.Card_Container)
        if NowHave < 6:
            adding = Type(self.UIOwner, self, self.Start+(self.Distance*NowHave))
            self.Card_Container.append(adding)
    
    def AddCard(self, Type):
        self.UIOwner.Property["OwnCard"][Type] += 1

    def refresh(self):
        if self.Built:
            Owner_Balance = self.UIOwner.Property["Balance"]
            Owner_Bank = self.UIOwner.Property["Bank"]
            if Owner_Balance <= 0:
                self.Option_Bar.Show_Wallet.text = f"0"
            else:
                self.Option_Bar.Show_Wallet.text = f"{Owner_Balance}"
            
            if Owner_Bank <= 0:
                self.Option_Bar.Show_Bank.text = f"0"
            else:
                self.Option_Bar.Show_Bank.text = f"{Owner_Bank}"
                
            for i in range(6):
                NowHave = len(self.Card_Container)
                if i < NowHave:
                    if not self.Card_Container[i].Can_Use:
                        self.Card_Container[i].Choosed = False
                        self.UIOwner.Property["OwnCard"][self.Card_Container[i].__class__]-=1
                        self.Card_Container.pop(i)
                        for j in range(i, NowHave):
                            if j < len(self.Card_Container):
                                _temp = self.Card_Container[j]
                                _temp.position = (_temp.position[0]-0.2, _temp.position[1], _temp.position[2])
        
            for Button in self.Option_Bar.Option_Bar_Container[5:]:
                if Button.Clicked:
                    Button.Clicked = False
                    return Button.Represent
    
    def Clear_Used_Card(self):
        for i in range(6):
            NowHave = len(self.Card_Container)
            if i < NowHave:
                if not self.Card_Container[i].Can_Use:
                    self.UIOwner.Property["OwnCard"][self.Card_Container[i].__class__]-=1
                    self.Card_Container.pop(i)





###########################################################################
#------------------------------Player Classes-----------------------------#
###########################################################################
class Player_Broke_Animation():
    def __init__(self):
        self.Original_v = 0.02
        self.v = -0.02
        self.UI = None
    def play_Broken_Animation(self):
        if not self.UI:
            self.UI = Entity(
                parent=camera.ui,
                model="quad",
                texture="assets\Others\_No_BG_Broken",
                scale=(2, 1),
                position=(0, 5),
                color=color.gray
            )
        elif int(str(self.Original_v)[0]) <= 0:
            if self.UI.y+self.v>0:
                self.UI.y += self.v
            else:
                self.Original_v*=0.75
                self.v = self.Original_v
            self.v -= 0.0005
            return False
        else:
            destroy(self.UI)
            return True



class Win_GameOver_Animation():
    def __init__(self):
        self.Original_v = 0.02
        self.v = -0.02
        self.UI = None
    def play_Win_Animation(self):
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
        else:
            return True



class Player(Entity):
    def __init__(self, Idenity, map, mapBindings, Walkable_Bindings, Hospital_Jail, ID, SoundPlayer, DefaultBalance, DefaultBank, start=(1, 1, 7), speed=1):
        super().__init__(
            parent = scene,
            position = start,
            model = "sphere",
            color = Idenity,
            scale = 1,
            double_sided = True
        )

        self.ID = ID
        self.MAP = map.Map
        self.Walkable_Bindings = Walkable_Bindings
        self.MapBindings = mapBindings
        self.Hospital_Jail = Hospital_Jail
        self.MapWidth = map.width
        self.MapHeight = map.height
        self.MapPosZ = int(self.MapHeight-self.position[2])
        self.MapPosX = int(self.position[0])
        self.SPEED = speed

        self.Broke_Animater = Player_Broke_Animation()
        self.Win_Animater = Win_GameOver_Animation()

        self.Property = {
            "Broke":False,
            "Rising":1,
            "Round":1, 
            "Balance":DefaultBalance,
            "Bank":DefaultBank,
            "Announcing":False,
            "OwnCard":{
                BuyLandCard:0,
                # ChangeHouse:0,
                RebuildCard:0,
                RemoveHouse:0,
                ControlDice:0,
                TurtleSpeed:0,
                TurnBackCrd:0,
                NotMoveCard:0,
                MoveAtSleep:0,
                AGreatSleep:0,
                StopHereCrd:0,
                TheBombCard:0,
                TheTimeBomb:0,
                # AMissleCard:0,
                # TheFreeCard:0,
                PaidTaxCard:0,
                EvenPoorCrd:0,
                EvenRichCrd:0,
                TheStealCrd:0,
                TheTrapCard:0,
                TheNoSinCrd:0,
                ClearMyRoad:0,
                BuildALevel:0,
                # TheNukeCard:0,
                PayBackCard:0,
                FriendsCard:0
            },
            "LargeHouse":{
            },
            "SmallHouse":{
            },
            "SoundEffects":{
                "Walking":SoundPlayer[0]
            },
            "Status":{
                "Dice_Animation":0,
                "point":0,
                "go":0,
                "counter":0
            },
            "SpecialEffect":{
                "Hotel":-1,
                "HOSP":-1,
                "Jail":-1,
                "TurtleSpeed":-1,
                "NotMoveCard":-1,
                "MoveAtSleep":-1,
                "AGreatSleep":-1
            },
            "Friends":{},
            "TheTimeBomb":-1
        }

        self.Walkable = ["Lott","Game",
        "Add1C","Add2C","Add3C","Magic","Road","Bank",
        "Add2","Add5","Add10","Add20","Mis2","Mis5","Mis10","Mis20",
        "News","Shop"]
        self.direction = [False, False, False, False] #上 下 左 右
        self.direction[randint(0, 3)] = True

    def Broke(self):
        self.color = color.gray
        for house, coordnate in self.Property["LargeHouse"].items():
            if house.Building:
                destroy(house.Building)
            house.Owner = house.Building = None
            house.Level = 0
            house.Building_Function = house.None_Building_Function
        for house, coordnate in self.Property["SmallHouse"].items():
            if house.Building:
                destroy(house.Building)
            house.Owner = house.Building = None
            house.Level = 0
        self.Property["Balance"] = 0
        self.Property["Bank"] = 0
        self.Property["Broke"] = True

    def Bind_Other_Player(self, PlayerList):
        _PlayerList = PlayerList.copy()
        _PlayerList.remove(self)
        self.OtherPlayer = _PlayerList
        self.Property["Friends"] = {}
        for player in self.OtherPlayer:
            self.Property["Friends"][player] = -1

    def AddCard(self, Amount, Type=None):
        if Type:
            if sum(list(self.Property["OwnCard"].values())) < 6:
                self.Property["OwnCard"][Type] += Amount
                self.Announcement(f"Player_{self.ID} added {Amount} {Type.__name__} Cards")
                Print(f"Player_{self.ID} added {Amount} {Type.__name__} Cards")
        else:
            _cardType = list(self.Property["OwnCard"].keys())
            add = 0
            for i in range(Amount):
                if sum(list(self.Property["OwnCard"].values())) < 6:
                    rdCard = _cardType[randint(0, len(_cardType)-1)]
                    self.Property["OwnCard"][rdCard] += 1
                    add += 1
            self.Announcement(f"Player_{self.ID} added {add} Cards")
            Print(f"Player_{self.ID} added {add} Cards")

    def AddMoney(self, Amount, Announce=True):
        self.Property["Balance"] += Amount
        Print(f"Player_{self.ID} gain {Amount}$")
        if Announce:
            self.Announcement(f"Player_{self.ID} gain {Amount}$")
        return Amount

    def LossMoney(self, Amount, Announce=True):
        if self.Property["Balance"] >= Amount:
            self.Property["Balance"] = self.Property["Balance"]-Amount
            left = 0
        else:
            left = Amount - self.Property["Balance"]
            self.Property["Balance"] = 0
            if self.Property["Bank"] >= Amount:
                self.Property["Bank"] -= left
                left = 0
            else:
                self.Property["Bank"] = 0
                left = left - self.Property["Bank"]
                self.Broke()
        Print(f"Player_{self.ID} loss {Amount}$")
        if Announce:
            self.Announcement(f"Player_{self.ID} loss {Amount - left}$")
        return Amount - left

    def Make_Friends(self, Player, Rounds):
        self.Property["Friends"][Player] = Rounds

    def Go_Hotel(self, Hotel, Rounds, Price):
        self.Property["SpecialEffect"]["Hotel"] = Rounds+1
        self.Camera_Follow()
        self.Announcement(f"Player_{self.ID} paid {Price} into Player_{Hotel.Owner.ID}\'s Hotel, rounds left: {Rounds}")
        Print(f"Player_{self.ID} checked into Player_{Hotel.Owner.ID}\'s Hotel, rounds left: {Rounds}")
        self.visible = False

    def Go_Jail(self, Rounds, Announce=True):
        if self.Property["OwnCard"][TheNoSinCrd] > 0:
            self.Property["OwnCard"][TheNoSinCrd] -= 1
            self.Announcement(f"Player_{self.ID} Used TheNoSinCrd to prevent going to Jail")
            Print(f"Player_{self.ID} Used TheNoSinCrd to prevent going to Jail")
        else:
            self.Property["SpecialEffect"]["Jail"] = Rounds+1
            self.position = (self.Hospital_Jail["Jail"][0], self.position[1], self.Hospital_Jail["Jail"][2])
            self.Camera_Follow()
            if Announce:
                self.Announcement(f"Player_{self.ID} still in Jail, rounds left: {Rounds}")
            Print(f"Player_{self.ID} still in Jail, rounds left: {Rounds}")
            self.visible = False

    def Go_Hospital(self, Rounds, Announce=True):
        self.Property["SpecialEffect"]["HOSP"] = Rounds+1
        self.position = (self.Hospital_Jail["HOSP"][0], self.position[1], self.Hospital_Jail["HOSP"][2])
        self.Camera_Follow()
        if Announce:
            self.Announcement(f"Player_{self.ID} still in Hospital, rounds left: {Rounds}")
        Print(f"Player_{self.ID} still in Hospital, rounds left: {Rounds}")
        self.visible = False

    def Carry_Time_Bomb(self, Steps):
        self.Property["TheTimeBomb"] = Steps
        self.Announcement(f"Player_{self.ID} Now Carries a time bomb (steps left: {Steps}")

    def Turn(self):
        self.direction[0], self.direction[1] = self.direction[1], self.direction[0]
        self.direction[2], self.direction[3] = self.direction[3], self.direction[2]

    def Bind_UI(self, ui):
        self.UI = ui

    def Camera_Follow(self):
        camera.position = (self.position[0]-6, MIN_ZOOM_IN, self.position[2]-NORMAL_ZOOM)
        
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
        self.Announcement_Icon = Entity(
            parent=camera.ui,
            model="circle",
            position=(self.Announcement_Bar.position[0]-(self.Announcement_Bar.scale[0]/2), self.Announcement_Bar.position[1], 4),
            scale=0.2,
            color=self.color
        )
        self.Property["Announcing"] = True
        Make_After(dic=self.Property, key="Announcing", value=False, delay=3)
        destroy(self.Announcement_Bar, 3)
        destroy(self.Announcement_Icon, 3)

    def NoNe(self):
        return None, None

    def updateProperty(self):
        for _ in self.MapBindings.items():
            if _[1].Owner==f"Player_{self.ID}":
                if _[1].Type == "LargeHouse":
                    self.Property[_[1].Type][_[1].Building_Type].update(
                        {_[1].bindWith : _[1].Level}
                    )
                if _[1].Type == "SmallHouse":
                    self.Property[_[1].Type].update({_[1].bindWith : _[1].Level})

    def update_Special_Effect(self):
        for EffectName in self.Property["SpecialEffect"].keys():
            if self.Property["SpecialEffect"][EffectName] >= 0:
                self.Property["SpecialEffect"][EffectName] -= 1
                if self.Property["SpecialEffect"][EffectName] <= 0:
                    self.Property["SpecialEffect"][EffectName] = -1
        for player in self.OtherPlayer:
            if self.Property["Friends"][player] >= 0:
                self.Property["Friends"][player] -= 1
                if self.Property["Friends"][player] <= 0:
                    self.Property["Friends"][player] =-1
    
    def Start_Round(self):
        self.dice = Dice(pos=(10,3,9), Scale=0.5, Color=color.white, Model="CubeModel")
        self.dice.rotation_x = self.dice.rotation_y = self.dice.rotation_z = self.Property["Status"]["Dice_Animation"] = self.Property["Status"]["counter"] = 0
        self.Property["Status"]["go"] = True
        self.Property["Status"]["counter"]=-19

    def Play_Step(self):
        if any(HOSP_Jail_Rounds > 0 for HOSP_Jail_Rounds in self.Property["SpecialEffect"].values()):
            if self.Property["SpecialEffect"]["Hotel"] > 0:
                self.Camera_Follow()
                rounds_left = self.Property["SpecialEffect"]["Hotel"]-1
                self.Announcement(f"Player_{self.ID} still in Hotel, rounds left: {rounds_left}")
                Print(f"Player_{self.ID} still in Hotel, rounds left: {rounds_left}")
                self.visible = False
                if self.Property["SpecialEffect"]["Hotel"]-1 == 0:
                    self.Property["SpecialEffect"]["Hotel"] = -1
                    self.visible = True
                    self.Camera_Follow()
                    return False, False
                self.update_Special_Effect()
                return True, True
            elif self.Property["SpecialEffect"]["HOSP"] > 0:
                self.Camera_Follow()
                rounds_left = self.Property["SpecialEffect"]["HOSP"]-1
                self.Announcement(f"Player_{self.ID} still in Hospital, rounds left: {rounds_left}")
                Print(f"Player_{self.ID} still in Hospital, rounds left: {rounds_left}")
                self.visible = False
                if self.Property["SpecialEffect"]["HOSP"]-1 == 0:
                    self.Property["SpecialEffect"]["HOSP"] = -1
                    self.visible = True
                    self.position = (self.Hospital_Jail["HOSP"][0], self.position[1], self.Hospital_Jail["HOSP"][2])
                    self.Camera_Follow()
                    return False, False
                self.update_Special_Effect()
                return True, True

            elif self.Property["SpecialEffect"]["Jail"] > 0:
                self.Camera_Follow()
                rounds_left = self.Property["SpecialEffect"]["Jail"]-1
                self.Announcement(f"Player_{self.ID} still in Jail, rounds left: {rounds_left}")
                Print(f"Player_{self.ID} still in Jail, rounds left: {rounds_left}")
                self.visible = False
                if self.Property["SpecialEffect"]["Jail"]-1 == 0:
                    self.Property["SpecialEffect"]["Jail"] = -1
                    self.visible = True
                    self.position = (self.Hospital_Jail["Jail"][0], self.position[1], self.Hospital_Jail["Jail"][2])
                    self.Camera_Follow()
                    return False, False
                self.update_Special_Effect()
                return True, True
            
            elif self.Property["SpecialEffect"]["MoveAtSleep"] > 0:
                if not self.Property["Status"]["go"]:
                    self.Start_Round()
            
            elif self.Property["SpecialEffect"]["AGreatSleep"] > 0:
                rounds_left = self.Property["SpecialEffect"]["AGreatSleep"]
                self.Announcement(f"Player_{self.ID} still Sleeping, rounds left: {rounds_left}")
                self.update_Special_Effect()
                return True, True

            elif self.Property["SpecialEffect"]["NotMoveCard"] > 0:
                self.Property["Status"]["point"] = -1

            elif self.Property["SpecialEffect"]["TurtleSpeed"] > 0:
                self.Property["Status"]["point"] = 1

        if any(Card.Choosed for Card in self.UI.Card_Container):
            if not self.Property["Status"]["go"] and self.Property["SpecialEffect"]["MoveAtSleep"]<=0 and self.Property["SpecialEffect"]["AGreatSleep"]<=0:
                for _Card in self.UI.Card_Container:
                    if _Card.Choosed:
                        Card = _Card
                        PreUse_Function = _Card.PreUse
                        break
                def Card_Use_Function():
                    nonlocal Card
                    return Card.Use(PreUse_Function())
                return "Pausefunction", Card_Use_Function
            else:
                for Card in self.UI.Card_Container: Card.Choosed=False
        if self.UI.RD.Go and not self.Property["Status"]["go"]:
            self.Start_Round()
            self.UI.RD.Go = False
        if self.Property["Status"]["go"]:
            if not self.Property["Status"]["point"]:
                point = randint(1, 6)
                self.Property["Status"]["point"] = point
                print("\n----------------------\n| {:<19}|\n----------------------\n".format(f"{self.color.name} gets {point} moves"))
            if not self.Property["Status"]["Dice_Animation"]:
                camera.position = (4, 8, -1)
                self.Property["Status"]["Dice_Animation"] = self.dice.Animation(self.Property["Status"]["point"] if self.Property["Status"]["point"]>0 else randint(1, 6))
            else:
                self.Property["Status"]["counter"]+=1
                if self.Property["Status"]["counter"]==0:
                    destroy(self.dice)
                    self.Camera_Follow()
                if self.Property["Status"]["counter"]%20==0 and self.Property["Status"]["counter"]!=0:
                    if self.Property["SoundEffects"]["Walking"]:
                        if self.Property["SoundEffects"]["Walking"].get_num_channels() == 0:
                            self.Property["SoundEffects"]["Walking"].play(loops=-1)
                    self.Property["Status"]["point"], response = self.move(self.Property["Status"]["point"])
                    self.Camera_Follow()
                    res, attachment = response()
                    if res in ["LargeBuilding", "SmallBuilding"]:
                        self.Property["Status"]["point"] = self.Property["Status"]["go"] = self.Property["Status"]["Dice_Animation"] = 0
                        self.update_Special_Effect()
                        return "Stopfunction", attachment
                    if res and self.Property["SpecialEffect"]["MoveAtSleep"]<=0 and self.Property["SpecialEffect"]["AGreatSleep"]<=0:
                        if res in ["Magic", "AddCard", "Add", "Mis", "Shop", "News"]:
                            self.Property["Status"]["point"] = self.Property["Status"]["go"] = self.Property["Status"]["Dice_Animation"] = 0
                            self.update_Special_Effect()
                            return "Stopfunction", attachment
                        elif res in ["Lott", "Bank"]:
                            if self.Property["Status"]["point"]==0:
                                self.Property["Status"]["point"] = self.Property["Status"]["go"] = self.Property["Status"]["Dice_Animation"] = 0
                                self.update_Special_Effect()
                                return "Stopfunction", attachment
                            return "Pausefunction", attachment
                        elif res=="Game":
                            self.Property["Status"]["point"] = self.Property["Status"]["go"] = self.Property["Status"]["Dice_Animation"] = 0
                            self.update_Special_Effect()
                            return "Game", attachment
                    if self.Property["Status"]["point"]<=0:
                        self.Property["Status"]["point"] = self.Property["Status"]["go"] = self.Property["Status"]["Dice_Animation"] = 0
                        self.update_Special_Effect()
                        return True, None
        return False, None

    def move(self, points_Left):
        if points_Left > 0:
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

            points_Left -= 1
            if self.Property["TheTimeBomb"] > 0:
                self.Property["TheTimeBomb"] -= 1
                if self.Property["TheTimeBomb"] == 0:
                    self.Property["TheTimeBomb"] = -1
                    self.Go_Hospital(Rounds=4)
                    return 0, self.NoNe
        x, _, z = self.position
        self.MapPosZ = int(self.MapHeight-z)
        self.MapPosX = int(x)

        GetBindingInformation = self.Walkable_Bindings.get((self.MapPosZ, self.MapPosX), False)
        if GetBindingInformation:
            if GetBindingInformation.Stop:
                destroy(GetBindingInformation.Stop)
                GetBindingInformation.Stop = False
                points_Left = -1
            elif GetBindingInformation.Bomb and points_Left<=0:
                destroy(GetBindingInformation.Bomb)
                GetBindingInformation.Bomb = False
                self.Go_Hospital(Rounds=3)
                points_Left = 0
                return points_Left, self.NoNe

        GetBindingInformation = self.MapBindings.get((self.MapPosZ, self.MapPosX), False)
        if GetBindingInformation:
            if points_Left==0 or points_Left==-1:
                points_Left = 0
                return points_Left, GetBindingInformation.OnStop(Player=self, StoppedAt=(z, x))
            else:
                return points_Left, GetBindingInformation.OnPass(Player=self, StoppedAt=(z, x))
        else:
            return points_Left, self.NoNe







################################################################################################################################################
################################################################################################################################################
####                                                                                                                                        ####
####--------------------------------------------------------Building and Map Classes--------------------------------------------------------####
####                                                                                                                                        ####
################################################################################################################################################
################################################################################################################################################
###########################################################################
#---------------------------Large House Classes---------------------------#
###########################################################################
class StockExchange(Entity):
    def __init__(self, bindWith, posX, posZ, Owner, OtherPlayer, rotate=0):
        super().__init__(
            model=self.__class__.__name__,
            scale=.4,
            position=(posX,0.3,posZ),
            rotation_y = rotate,
            color = Owner.color
        )
        self.Owner = Owner
        self.bindWith = bindWith
        self.OtherPlayer = OtherPlayer
    def Building_Function(self, Player):
        if Player != self.Owner:
            Print(f"Player_{Player.ID} triggered Player_{self.Owner.ID}\'s {self.__class__.__name__}\'s Building_Function at {self.bindWith}")
        return True
    def Roundly_Function(self):
        Gain = 0
        for player in self.OtherPlayer:
            Gain += player.LossMoney(Amount=int(300*self.Owner.Property["Rising"]), Announce=False)
        self.Owner.AddMoney(Amount=Gain, Announce=True)
        Print(f"Player_{self.Owner.ID}\'s {self.__class__.__name__} at {self.bindWith} Excuted Roundly Function")
        return True

class Hotel(Entity):
    price = 5000
    def __init__(self, bindWith, posX, posZ, Owner, OtherPlayer, rotate=0):
        super().__init__(
            model=self.__class__.__name__,
            scale=.5,
            position=(posX,0.3,posZ),
            rotation_y = rotate,
            color = Owner.color
        )
        self.Owner = Owner
        self.bindWith = bindWith
        self.OtherPlayer = OtherPlayer
    def Building_Function(self, Player):
        if Player != self.Owner:
            price = int(self.price*self.Owner.Property["Rising"])
            Player.Go_Hotel(Hotel=self, Rounds=3, Price=price)
            Gain = Player.LossMoney(Amount=price, Announce=False)
            self.Owner.AddMoney(Gain, Announce=False)
            Print(f"Player_{Player.ID} triggered Player_{self.Owner.ID}\'s {self.__class__.__name__}\'s Building_Function at {self.bindWith}")
        return True
    def Roundly_Function(self):
        Print(f"Player_{self.Owner.ID}\'s {self.__class__.__name__} at {self.bindWith} Excuted Roundly Function")
        return True

class OilField(Entity):
    def __init__(self, bindWith, posX, posZ, Owner, OtherPlayer, rotate=0):
        super().__init__(
            model=self.__class__.__name__,
            scale=.0125,
            position=(posX,0.3,posZ),
            rotation_y = rotate,
            color = Owner.color
        )
        self.Owner = Owner
        self.bindWith = bindWith
        self.OtherPlayer = OtherPlayer
        self.Last_Stopped_Round = self.Owner.Property["Round"]
    def Building_Function(self, Player):
        if Player == self.Owner:
            Passed_Round = self.Owner.Property["Round"] - self.Last_Stopped_Round
            self.Owner.AddMoney(Amount=int((Passed_Round*1000)*self.Owner.Property["Rising"]), Announce=True)
            Print(f"Player_{Player.ID} triggered Player_{self.Owner.ID}\'s {self.__class__.__name__}\'s Building_Function at {self.bindWith}")
        return True
    def Roundly_Function(self):
        Print(f"Player_{self.Owner.ID}\'s {self.__class__.__name__} at {self.bindWith} Excuted Roundly Function")
        return True

class Park(Entity):
    def __init__(self, bindWith, posX, posZ, Owner, OtherPlayer, rotate=0):
        super().__init__(
            model=self.__class__.__name__,
            scale=.13,
            position=(posX,0.3,posZ),
            rotation_y = rotate,
            color = Owner.color
        )
        self.Owner = Owner
        self.bindWith = bindWith
        self.OtherPlayer = OtherPlayer
    def Building_Function(self, Player):
        if Player != self.Owner:
            Print(f"Player_{Player.ID} triggered Player_{self.Owner.ID}\'s {self.__class__.__name__}\'s Building_Function at {self.bindWith}")
        return True
    def Roundly_Function(self):
        Print(f"Player_{self.Owner.ID}\'s {self.__class__.__name__} at {self.bindWith} Excuted Roundly Function")
        return True

class Sign(Entity):
    def __init__(self, bindWith, posX, posZ, Owner, OtherPlayer, rotate=0):
        super().__init__(
            model="sign",
            scale=0.25,
            position=(posX,0.3,posZ),
            rotation_y = rotate,
            color = Owner.color
        )
        self.Owner = Owner
        self.bindWith = bindWith
        self.OtherPlayer = OtherPlayer
    def Building_Function(self, Player):
        Print(f"Player_{Player.ID} triggered Player_{self.Owner.ID}\'s {self.__class__.__name__}\'s Building_Function at {self.bindWith}")
        return True
    def Roundly_Function(self):
        Print(f"Player_{self.Owner.ID}\'s {self.__class__.__name__} at {self.bindWith} Excuted Roundly Function")
        return True






###########################################################################
#---------------------------Small House Classes---------------------------#
###########################################################################
class SmallHouseModel(Entity):
    def __init__(self, posX, posZ, Owner, rotate=0):
        super().__init__(
            model="sign",
            scale=0.15,
            position=(posX,0.3,posZ),
            color = Owner.color
        )
        self.Level = 0
        self.MaxLevel = 4
        self.rotation_y = rotate
        self.models = ["sign", "house1", "house2", "house3", "house4"]
    def downgrade(self):
        self.Level -= 1
        self.model = self.models[self.Level]
        if self.Level == 0:
            self.scale = 0.15
        else:
            self.scale = 0.07
    def upgrade(self):
        if self.Level < self.MaxLevel:
            self.Level+=1
            self.model = self.models[self.Level]
            self.scale = 0.07

class Hospital_Building(Entity):
    def __init__(self, posX, posZ):
        super().__init__(
            model="hospital",
            color = rgb(255,182,193),
            scale=.4,
            position=(posX, 0.25, posZ)
        )

class Jail_Building(Entity):
    def __init__(self, posX, posZ):
        super().__init__(
            model="Jail",
            color = color.gray,
            scale=.05,
            position=(posX, 0.25, posZ)
        )

class Hospital(Entity):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Texture="white_cube", IsBuilding=False):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = Texture,
            color = Color,
            scale = Scale
        )
        self.IsBuilding = IsBuilding
        if self.IsBuilding:
            Hospital_Building(posX=pos[0], posZ=pos[2])

class Jail(Entity):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Texture="white_cube", IsBuilding=False):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = Texture,
            color = Color,
            scale = Scale
        )
        self.IsBuilding = IsBuilding
        if self.IsBuilding:
            Jail_Building(posX=pos[0], posZ=pos[2])





###########################################################################
#----------------------------Map Block Classes----------------------------#
###########################################################################
class Sky(Entity):
    def __init__(self, choice=None):
        getRGB = {
            "NormalPurple":rgb(115, 96, 206),
            "Sea":rgb(64, 156, 255),
            "OverCast":rgb(201, 226, 255),
            "Night1":rgb(12, 20, 69),
            "Night2":rgb(76, 64, 142),
            "Night3":rgb(56, 40, 92)
        }
        super().__init__(
            parent = scene,
            model = "sky_dome",
            color = getRGB[choice if choice in list(getRGB.keys()) else list(getRGB.keys())[randint(0, len(getRGB)-1)]],
            scale = 500,
            double_sided = True
        )



class LargeBuilding(Entity):
    def __init__(self, bindWith=((2, 0), (2, 1)), pos=(0, 0, 0), Scale=(1,0.25,1), Color=color.white, Model="CubeModel"):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = "assets/UVmap/HouseBlock.png",
            color = Color,
            scale = Scale
        )
        self.price = 4400
        self.Level = 0
        self.Type = "LargeHouse"
        self.bindWith = bindWith
        self.Building_Types = {
                        "StockExchange":StockExchange,
                        "Hotel":Hotel,
                        "OilField":OilField,
                        "Park":Park
                        }
        self.Building = None
        self.Owner = None

    def Downgrade(self):
        if type(self.Building) != Sign:
            destroy(self.Building)
            self.Building = Sign(
                bindWith = self.bindWith,posX=self.position[0], posZ=self.position[2], 
                Owner=self.Owner, OtherPlayer=self.Owner.OtherPlayer,
                rotate=0 if self.position[0]-0.5==self.bindWith[0][1] else 90
            )
            self.Building_Function = self.Building.Building_Function


    def None_Building_Function(self, Player):
        pass

    def Building_Function(self, Player):
        pass

    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                current_price = int(self.price*Player.Property["Rising"])
                if Player.Property["SpecialEffect"]["MoveAtSleep"]<=0 and Player.Property["SpecialEffect"]["AGreatSleep"]<=0:
                    if not self.Owner:
                        if not system["ChooseYesNo"].Built:
                            system["ChooseYesNo"].Build_GUI(text=f"Spend {current_price}$ to Buy a LargeBuilding Land?")
                        else:
                            if system["ChooseYesNo"].Check():
                                if system["ChooseYesNo"].Result:
                                    if Player.Property["Balance"] >= current_price:
                                        Player.LossMoney(Amount=current_price, Announce=True)
                                        self.Owner = Player
                                        if self.Building:
                                            destroy(self.Building)
                                        self.Building = Sign(
                                            bindWith = self.bindWith,posX=self.position[0], posZ=self.position[2], 
                                            Owner=Player, OtherPlayer=Player.OtherPlayer,
                                            rotate=0 if self.position[0]-0.5==self.bindWith[0][1] else 90
                                        )
                                        self.Building_Function = self.Building.Building_Function
                                        Player.Property["LargeHouse"][self] = self.bindWith
                                        Print(f"Player_{Player.ID} Now Owned a LargeBuilding Plot at {StoppedAt}")
                                    else:
                                        Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                                return self.__class__.__name__, (self.Owner, self.Level)
                    else:
                        if type(self.Building) == Sign and Player == self.Owner:
                            if not system["ChooseLargeBuilding"].Built:
                                system["ChooseLargeBuilding"].Build_GUI(text=f"Spend {current_price}$ to Upgrade?")
                            else:
                                if system["ChooseLargeBuilding"].Check():
                                    if system["ChooseLargeBuilding"].Result and not system["ChooseLargeBuilding"].BackGround.CloseButton.Close:
                                        if Player.Property["Balance"] >= current_price:
                                            Player.LossMoney(Amount=current_price, Announce=True)
                                            destroy(self.Building)
                                            self.Building = self.Building_Types[system["ChooseLargeBuilding"].Result](
                                                bindWith = self.bindWith,
                                                posX=self.position[0], posZ=self.position[2], 
                                                Owner=Player, OtherPlayer=Player.OtherPlayer,
                                                rotate=0 if self.position[0]-0.5==self.bindWith[0][1] else 90
                                            )
                                            self.Building_Function = self.Building.Building_Function
                                            self.Level = self.Building.__class__.__name__
                                        else:
                                            Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                                    return True, True
                        else:
                            if Player != self.Owner:
                                if self.Owner.Property["Friends"][Player] > 0:
                                    Player.Announcement(f"Player_{Player.ID} is currently friends with Player_{self.Owner.ID}")
                                    return True, True
                            return self.Building_Function(Player=Player), True #不管是不是地產持有者都執行 (因為有油田 要持有者去觸發領錢)
                else:
                    if self.Owner and Player != self.Owner:
                        if self.Owner.Property["Friends"][Player] > 0:
                            Player.Announcement(f"Player_{Player.ID} is currently friends with Player_{self.Owner.ID}")
                            return True, True
                        return self.Building_Function(Player=Player), True #只有當不是地產持有者時才執行 (因為如果是持有者處於睡眠狀態 不可領取油田收益)
                    return True, True
            return self.__class__.__name__, __
        return _



class SmallBuilding(Entity):
    def __init__(self, bindWith, pos=(0, 0, 0), faceDown=True, Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel"):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = "assets/UVmap/HouseBlock.png",
            color = Color,
            scale = Scale
        )
        self.price = 2400
        self.bindWith = bindWith
        self.Building = None
        self.Owner = None
        self.rotate = not faceDown
        self.Level = 0

    def Downgrade(self):
        if self.Level != 0:
            self.Building.downgrade()
            self.Level = self.Building.Level

    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                current_price = int(self.price*Player.Property["Rising"])
                if Player.Property["SpecialEffect"]["MoveAtSleep"]<=0 and Player.Property["SpecialEffect"]["AGreatSleep"]<=0:
                    if not self.Owner:
                        if not system["ChooseYesNo"].Built:
                            system["ChooseYesNo"].Build_GUI(text=f"Spend {current_price}$ to Buy a SmallBuilding Land?")
                        else:
                            if system["ChooseYesNo"].Check():
                                if system["ChooseYesNo"].Result:
                                    if Player.Property["Balance"] >= current_price:
                                        Player.LossMoney(Amount=current_price, Announce=True)
                                        self.Owner = Player
                                        self.Building = SmallHouseModel(posX=self.position[0], posZ=self.position[2], Owner=self.Owner, rotate=90 if self.rotate else 0)
                                        self.Level = self.Building.Level
                                        Player.Property["SmallHouse"][self] = self.bindWith
                                        Print(f"Player_{Player.ID} Now Owned a house at {StoppedAt} Type: {self.__class__.__name__}(Level: {self.Building.Level})")
                                    else:
                                        Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                                return self.__class__.__name__, (self.Owner, 1500)
                    else:
                        if Player == self.Owner:
                            if self.Building.Level < 4:
                                if not system["ChooseYesNo"].Built:
                                    system["ChooseYesNo"].Build_GUI(text=f"Spend {current_price}$ to Upgrade?")
                                else:
                                    if system["ChooseYesNo"].Check():
                                        if system["ChooseYesNo"].Result:
                                            if Player.Property["Balance"] >= current_price:
                                                Player.LossMoney(Amount=current_price, Announce=True)
                                                self.Building.upgrade()
                                                self.Level = self.Building.Level
                                                Print(f"Player_{Player.ID}, Upgraded his Property at {StoppedAt} (Level: {self.Building.Level})")
                                            else:
                                                Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                                        return self.__class__.__name__, (self.Owner, self.Building.Level*1500)
                            else:
                                return True, True
                        else:
                            if self.Owner.Property["Friends"][Player] > 0:
                                Player.Announcement(f"Player_{Player.ID} is currently friends with Player_{self.Owner.ID}")
                                return True, True
                            else:
                                passPaid = int(((self.Level+1)*1500)*self.Owner.Property["Rising"])
                                Print(f"Player_{Player.ID} Stopped at Player_{self.Owner.ID}'s House, Paid {passPaid}$")
                                took = Player.LossMoney(Amount=passPaid, Announce=True)
                                self.Owner.AddMoney(Amount=took, Announce=False)
                                return self.__class__.__name__, (self.Owner, self.Building.Level*1500)
                else:
                    if self.Owner and Player != self.Owner:
                        if self.Owner.Property["Friends"][Player] > 0:
                            Player.Announcement(f"Player_{Player.ID} is currently friends with Player_{self.Owner.ID}")
                            return True, True
                        else:
                            passPaid = int(((self.Level+1)*1500)*self.Owner.Property["Rising"])
                            Print(f"Player_{Player.ID} Stopped at Player_{self.Owner.ID}'s House, Paid {passPaid}$")
                            took = Player.LossMoney(Amount=passPaid, Announce=True)
                            self.Owner.AddMoney(Amount=took, Announce=False)
                            return self.__class__.__name__, (self.Owner, self.Building.Level*1500)
                    return True, True
            return self.__class__.__name__, __
        return _



class Road(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Texture="white_cube", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = Texture,
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            return None, None
        return _



class AddCard(Button):
    def __init__(self, amount, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        self.AddCards = amount
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Add{amount}C.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.amount = amount
        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                Player.AddCard(self.amount)
                return self.__class__.__name__, self.amount
            return self.__class__.__name__, __
        return _



class Add(Button):
    def __init__(self, Balance, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Add{Balance}.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.AddBalance = Balance*1000
        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _
    
    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                Player.AddMoney(int(self.AddBalance*Player.Property["Rising"]))
                return self.__class__.__name__, self.AddBalance
            return self.__class__.__name__, __
        return _



class Mis(Button):
    def __init__(self, Balance, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Mis{Balance}.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.MisBalance = Balance*1000
        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                Player.LossMoney(int(self.MisBalance*Player.Property["Rising"]))
                return self.__class__.__name__, self.MisBalance
            return self.__class__.__name__, __
        return _



class Bank(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Bank.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ShowBank"].Built:
                    system["ShowBank"].Build_GUI(Player)
                else:
                    if system["ShowBank"].Check():
                        Result = system["ShowBank"].Result
                        if system["ShowBank"].BackGround.BackGround.CloseButton.Close:
                            Result = 0
                        if system["ShowBank"].DigitalScreen.Withdraw and not system["ShowBank"].DigitalScreen.Deposit:
                            Result_String = f"Player_{Player.ID} Withdrew {Result}$"
                            Player.Property["Bank"] -= Result
                            Player.Property["Balance"] += Result
                        else:
                            Result_String = f"Player_{Player.ID} Deposited {Result}$"
                            Player.Property["Bank"] += Result
                            Player.Property["Balance"] -= Result
                        if Result:
                            Player.Announcement(Result_String)
                        Print(Result_String)
                        return True
            return self.__class__.__name__, __
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ShowBank"].Built:
                    system["ShowBank"].Build_GUI(Player)
                else:
                    if system["ShowBank"].Check():
                        Result = system["ShowBank"].Result
                        if system["ShowBank"].BackGround.BackGround.CloseButton.Close:
                            Result = 0
                        if system["ShowBank"].DigitalScreen.Withdraw and not system["ShowBank"].DigitalScreen.Deposit:
                            Result_String = f"Player_{Player.ID} Withdrew {Result}$"
                            Player.Property["Bank"] -= Result
                            Player.Property["Balance"] += Result
                        else:
                            Result_String = f"Player_{Player.ID} Deposited {Result}$"
                            Player.Property["Bank"] += Result
                            Player.Property["Balance"] -= Result
                        if Result:
                            Player.Announcement(Result_String)
                        Print(Result_String)
                        return True
            return self.__class__.__name__, __
        return _



class News(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/News.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ShowNews"].Built:
                    system["ShowNews"].Build_GUI(Player.UI)
                else:
                    if system["ShowNews"].Check():
                        Picked_News = system["ShowNews"].Result
                        if Picked_News[0] == "HOSP":
                            Player.Go_Hospital(Rounds=Picked_News[1])
                        elif Picked_News[0] == "Jail":
                            Player.Go_Jail(Rounds=Picked_News[1])
                        return self.__class__.__name__, True
                return False
            return self.__class__.__name__, __
        return _



class Shop(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Shop.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ShowShop"].Built:
                    system["ShowShop"].Build_GUI()
                else:
                    if system["ShowShop"].Check():
                        if not system["ShowShop"].BackGround.CloseButton.Close:
                            if Player.Property["Balance"] >= system["ShowShop"].Result.price:
                                Player.LossMoney(Amount=system["ShowShop"].Result.price, Announce=False)
                                Player.UI.AddCard(system["ShowShop"].Result)
                                Player.Announcement(f"Player_{Player.ID} Bought "+system["ShowShop"].Result.__name__)
                                Print(f"Player_{Player.ID} added a Card: "+system["ShowShop"].Result.__name__)
                            else:
                                Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                        return self.__class__.__name__, system["ShowShop"].Result
            return self.__class__.__name__, __
        return _



class Lott(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Lott.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ChooseLottery"].Built:
                    system["ChooseLottery"].Build_GUI()
                else:
                    if system["ChooseLottery"].Check(Player):
                        if not system["ChooseLottery"].BackGround.CloseButton.Close:
                            Result = system["ChooseLottery"].Result
                            if Result == -1:
                                Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                            else:
                                Player.Announcement(f"Player_{Player.ID} Bought a Lottery Number {Result}")
                                Print(f"Player_{Player.ID} Bought a Lottery Number {Result}")
                        else:
                            Result = None
                        return self.__class__.__name__, Result
            return self.__class__.__name__, __
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ChooseLottery"].Built:
                    system["ChooseLottery"].Build_GUI()
                else:
                    if system["ChooseLottery"].Check(Player):
                        if not system["ChooseLottery"].BackGround.CloseButton.Close:
                            Result = system["ChooseLottery"].Result
                            if Result:
                                if Result == -1:
                                    Player.Announcement(f"Player_{Player.ID} does not have enough Money")
                                else:
                                    Player.Announcement(f"Player_{Player.ID} Bought a Lottery Number {Result}")
                                    Print(f"Player_{Player.ID} Bought a Lottery Number {Result}")
                        else:
                            Result = None
                        return self.__class__.__name__, Result
            return self.__class__.__name__, __
        return _



class Game(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Game.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                GameOver, Score = system["ShowGame"].Play()
                if GameOver:
                    price = Score*100
                    Player.Announcement(f"Player_{Player.ID} won {price} in the MiniGame")
                    Player.AddMoney(Amount=price, Announce=False)
                return GameOver, Score
            return self.__class__.__name__, __
        return _



class Magic(Button):
    def __init__(self, pos=(0, 0, 0), Scale=(0.5,0.25,0.5), Color=color.white, Model="CubeModel", Arrpos=(0, 0)):
        super().__init__(
            parent = scene,
            position = pos,
            model = Model,
            texture = f"assets/UVmap/Magic.png",
            color = Color,
            disabled = True,
            scale = Scale
        )
        self.ArrBinding = Arrpos

        self.Owner = None
        self.Color = Color
        self.Choosing = False

        self.Bomb = False
        self.Stop = False

        self.PreChoosed = False
        self.Choosed = False

    def input(self, key):
        if not self.Bomb and not self.Stop:
            if self.hovered and self.Choosing:
                if key == "left mouse down":
                    self.PreChoosed = True
            if key == "left mouse up":
                if self.hovered and self.PreChoosed:
                    self.Choosed = True

    def update(self):
        if self.hovered and self.Choosing and not self.Bomb and not self.Stop:
            self.color = color.light_gray
        else:
            self.color = self.Color
    
    def OnPass(self, Player, StoppedAt):
        def _():
            return None, None
        return _

    def OnStop(self, Player, StoppedAt):
        def _():
            def __():
                if not system["ChooseMagic"].Built:
                    system["ChooseMagic"].Build_GUI(PlayerList=Player.OtherPlayer+[Player])
                else:
                    if system["ChooseMagic"].Check():
                        if not system["ChooseMagic"].BackGround.CloseButton.Close:
                            Result = system["ChooseMagic"].Result["event"]
                            Print(f"Magic！~ {Result}")
                            if Result == "Jail 3 Days":
                                for target in system["ChooseMagic"].Result["target"]:
                                    target.Go_Jail(Rounds=3, Announce=False)
                                return self.__class__.__name__, Result
                            elif Result == "Deposit All Balance":
                                for target in system["ChooseMagic"].Result["target"]:
                                    target.Property["Bank"] += target.Property["Balance"]
                                    target.Property["Balance"] = 0
                                return self.__class__.__name__, Result
                            elif Result == "Withdraw All Saving":
                                for target in system["ChooseMagic"].Result["target"]:
                                    target.Property["Balance"] += target.Property["Bank"]
                                    target.Property["Bank"] = 0
                                return self.__class__.__name__, Result
                            elif Result == "Gain 3 Cards":
                                for target in system["ChooseMagic"].Result["target"]:
                                    target.AddCard(Amount=3)
                                return self.__class__.__name__, Result
                            elif Result == "Loss 3 Cards":
                                for target in system["ChooseMagic"].Result["target"]:
                                    OwnedCard = []
                                    for cardType, amount in target.Property["OwnCard"].items():
                                        if amount > 0:
                                            for i in range(amount):
                                                OwnedCard.append(cardType)
                                    for i in range(3 if len(OwnedCard) >= 3 else len(OwnedCard)):
                                        target.Property["OwnCard"][OwnedCard.pop(randint(0, len(OwnedCard)-1))] -= 1
                                return self.__class__.__name__, Result
                            elif Result == "Destroy 1 Building":
                                for target in system["ChooseMagic"].Result["target"]:
                                    targetsHouseProperty = []
                                    for House in list(target.Property["SmallHouse"].keys())+list(target.Property["LargeHouse"].keys()):
                                        targetsHouseProperty.append(House)
                                    HowManyHouses = len(targetsHouseProperty)
                                    if HowManyHouses > 0:
                                        targetsHouseProperty[randint(0, HowManyHouses-1)].Downgrade()
                                return self.__class__.__name__, Result
                        else:
                            return self.__class__.__name__, None
            return self.__class__.__name__, __
        return _