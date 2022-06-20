from ursina import *
from random import randint
from .Classes import *

###########################################################################
#-------------------------------Map Classes-------------------------------#
###########################################################################
class Shanghai():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","SM_H","SM_H","SM_H","Road","Road","Road","Road","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","LG_H","LG_H","Road","Road","Road","News","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","LGHH","LG_H","SM_H","SM_H","SM_H","None","None","Road","Road","Game","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","LG_H","LG_H","Road","Road","Road","Add10","Road","Bank","None","None","None","None","None","None","None","Mis5","SM_H","None","None","None","None"],
            ["None","Jail","Jail","Road","Road","News","None","None","None","None","None","None","None","None","None","None","None","None","Add2C","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Shop","Road","SM_H","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Add5","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Game","Mis5","Magic","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","LGHH","LG_H","Road","SM_H","None","None"],
            ["None","None","None","None","None","Add1C","None","None","None","None","None","None","None","LG_H","LG_H","SM_H","SM_H","SM_H","LG_H","LG_H","Road","None","None","None"],
            ["None","None","None","None","None","Road","SM_H","None","None","None","Bank","Road","Game","Road","Lott","Road","Road","Road","Road","Road","Road","HOSP","HOSP","None"],
            ["None","None","None","None","None","Road","SM_H","None","LGHH","LG_H","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","Road","SM_H","None","LG_H","LG_H","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","News","SM_H","SM_H","Road","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","Shop","Road","Road","Magic","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class RichManCity():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","LG_H","LG_H","None","SM_H","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Game","Road","Road","Add2","Lott","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","Road","None","None","None","None","None","Add2","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","Add2","None","None","None","None","None","News","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add1C","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","News","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Bank","Road","Road","Road","Road","Road","Mis5","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","Mis5","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","LGHH","LG_H","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","Road","Road","Add2","None","None","None","None","None","None","None","None","None","LG_H","LG_H","None","LG_H","LG_H","None","Add1C","None","None","None","None","None","None"],
            ["None","HOSP","None","None","None","LGHH","LG_H","None","None","Add1C","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Magic","Road","Road","Shop","Bank","None","None","None","None","None","None"],
            ["None","HOSP","SM_H","SM_H","SM_H","LG_H","LG_H","SM_H","SM_H","Add2","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","Road","Road","Road","Road","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Add1C","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add2","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Magic","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Mis10","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add1C","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Mis2","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","News","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add20","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add2","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Game","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None","None","None","None","None","None"],
            ["None","Road","Lott","Add1C","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None","None","SM_H","None","None","None"],
            ["None","None","None","Bank","Road","Road","SM_H","SM_H","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","News","Road","Add5","Road","Shop","Add3C","Road","None","None","None"],
            ["None","None","None","None","None","Add2","Road","Road","Road","Add2","None","None","SM_H","SM_H","LG_H","LG_H","SM_H","SM_H","None","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","Add10","Mis5","Shop","Road","Road","Road","Road","Road","Road","News","Road","Road","None","SM_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Bank","Road","Road","Road","Road","Road","SM_H","SM_H","SM_H","None","None","None","None","Road","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","Mis2","Road","Add2","Lott","Road","Jail","Jail","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class SpaceStation():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None","None","None"],
            ["None","SM_H","SM_H","SM_H","LGHH","LG_H","None","None","Jail","None","LGHH","LG_H","LG_H","LG_H","None","None","None","None","None","None"],
            ["None","Road","Road","Road","LG_H","LG_H","SM_H","SM_H","Jail","SM_H","LG_H","LG_H","Road","Road","Bank","None","None","None","None","None"],
            ["None","Road","None","Add2","Road","Road","Road","Road","Road","Road","Road","Road","Lott","None","Road","SM_H","None","None","None","None"],
            ["None","Lott","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","None","Road","HOSP","HOSP","None","None","None"],
            ["None","Bank","Road","Road","Mis10","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","Add1C","Road","Road","Road","Road","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None","Add2","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None","Road","LGHH","LG_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","Mis2","Road","SM_H","None","None","None","Road","LG_H","LG_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None","None","Lott","Game","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None","None","None","Bank","Shop","None","None","None","None"],
            ["None","None","None","None","None","None","None","Add5","Road","SM_H","None","None","None","None","None","News","Magic","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None","None","None","None","Road","LGHH","LG_H","None"],
            ["None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None","None","None","None","Road","LG_H","LG_H","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","Road","None","None","None"],
            ["None","None","None","None","None","Bank","Road","Road","Lott","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","None","Road","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","None","Mis10","Road","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","Game","Road","Road","Road","Road","SM_H","SM_H","SM_H","SM_H","Road","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","News","Road","Road","Road","Road","Bank","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Paris():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None","None"],
            ["None","LG_H","LG_H","SM_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","SM_H","SM_H","SM_H","SM_H","LG_H","LG_H","None","None","None","None","None"],
            ["None","Road","Road","Road","Road","Road","Road","Road","SM_H","SM_H","SM_H","SM_H","Road","Road","Road","Road","Road","Road","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","Lott","Road","Road","Road","Road","Bank","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Add1C","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Shop","Add1C","Road","SM_H","None","None"],
            ["None","News","SM_H","SM_H","SM_H","None","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Game","Road","Road","Road","None","LGHH","LG_H","Shop","Road","Road","Road","Road","News","LGHH","LG_H","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","None","Mis2","SM_H","LG_H","LG_H","Add1C","None","None","None","None","Add2","LG_H","LG_H","None","None","None","Add2","Road","SM_H","None"],
            ["None","None","None","None","Magic","Road","Road","Road","Bank","None","None","None","None","Lott","Road","Road","None","None","None","None","Road","SM_H","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","None","None","None","None","Road","SM_H","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","Road","None","None","None","None","News","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","None","None","Jail","None","Road","SM_H","None"],
            ["None","None","None","None","None","SM_H","SM_H","SM_H","None","SM_H","SM_H","None","Mis10","None","None","None","None","None","Jail","None","Road","SM_H","None"],
            ["None","None","None","None","None","Road","Road","Road","Magic","Road","Road","Road","Add5","None","None","Road","Road","Road","Add2","Road","Road","SM_H","None"],
            ["None","None","None","None","None","News","SM_H","SM_H","SM_H","SM_H","LGHH","LG_H","None","None","None","Road","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","Add2C","Road","Road","Road","Road","LG_H","LG_H","SM_H","SM_H","SM_H","Road","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","Bank","Road","Road","Road","Road","Road","Add2","HOSP","HOSP","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Japan():
    def __init__(self):
        self.Map = [
            ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "LGHH", "LG_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "LG_H", "LG_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "Road", "Road", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "Road", "SM_H", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "Road", "SM_H", "Game", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "Road", "LGHH", "LG_H", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "News", "Road", "LG_H", "LG_H", "Road", "SM_H", "SM_H", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "Road", "SM_H", "None", "None", "Add2", "Road", "Road", "Road", "HOSP", "HOSP", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "Road", "SM_H", "None", "None", "None", "None", "None", "Shop", "LGHH", "LG_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "Road", "LGHH", "LG_H", "None", "None", "None", "None", "Lott", "LG_H", "LG_H", "SM_H", "SM_H", "SM_H", "None", "SM_H", "SM_H", "SM_H", "None", "None", "None", "None"],
            ["None", "Road", "LG_H", "LG_H", "None", "None", "None", "None", "Bank", "Road", "Road", "Road", "Road", "Road", "News", "Road", "Road", "Road", "None", "None", "None", "None"],
            ["None", "Bank", "Road", "Shop", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "Bank", "Road", "SM_H", "None", "None"],
            ["None", "None", "None", "None", "Road", "SM_H", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "Road", "SM_H", "None", "None"],
            ["None", "None", "None", "None", "Road", "SM_H", "LGHH", "LG_H", "None", "None", "None", "LGHH", "LG_H", "None", "None", "SM_H", "SM_H", "SM_H", "Road", "None", "None", "None"],
            ["None", "None", "None", "None", "Add5", "Lott", "LG_H", "LG_H", "None", "LGHH", "LG_H", "LG_H", "LG_H", "SM_H", "SM_H", "Road", "Road", "Road", "Add20", "Jail", "Jail", "None"],
            ["None", "None", "None", "None", "None", "Game", "Road", "Road", "None", "LG_H", "LG_H", "Road", "Road", "Road", "Road", "Shop", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "None", "None", "None", "None", "Road", "News", "Road", "Road", "Road", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"],
            ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class SnowKingdom():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Jail","None","None","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Jail","None","None","Road","LGHH","LG_H","Shop","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","Road","Add5","Add1C","Road","LG_H","LG_H","News","Road","Road","Road","None","None","None","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","SM_H","SM_H","None","None","None","None","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","None","Mis5","Road","Road","Road","SM_H","SM_H","SM_H","None","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","Lott","Road","Road","Road","None","None","None"],
            ["None","Game","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","LGHH","LG_H","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","SM_H","SM_H","SM_H","None","None","None","LG_H","LG_H","SM_H","SM_H","SM_H","SM_H","None","None","Road","SM_H","None","None"],
            ["None","Lott","Road","Road","Road","SM_H","SM_H","SM_H","Road","Road","Road","Road","Road","Road","LGHH","LG_H","Add5","None","None","None"],
            ["None","None","None","None","Shop","Road","Road","Road","Add5","None","None","None","None","Magic","LG_H","LG_H","Bank","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","News","Road","Road","Add1C","HOSP","HOSP","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Greece():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","SM_H","SM_H","SM_H","None","None","SM_H","SM_H","SM_H","None","None","None","None"],
            ["None","None","None","None","None","LGHH","LG_H","Road","Road","Road","News","Add5","Road","Road","Road","Road","Jail","Jail","None"],
            ["None","None","None","None","None","LG_H","LG_H","Road","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Lott","Magic","Road","Road","Road","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Shop","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Add1C","None","None","None"],
            ["None","None","Add1C","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None"],
            ["None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None"],
            ["None","None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","Game","Road","SM_H","None","None"],
            ["None","None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","Magic","None","None","None","None"],
            ["None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","News","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Bank","Shop","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","Bank","Add2","None","None","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","Mis2","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None","None"],
            ["None","Magic","None","None","None","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","News","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","Add2","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None","None"],
            ["None","Add2","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None","None"],
            ["None","Game","Road","Road","Road","Road","Shop","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","Mis2","None","None","None","None"],
            ["None","None","None","None","None","None","Add1C","None","None","None","None","None","None","None","Lott","Add1C","Road","SM_H","None"],
            ["None","None","None","None","None","None","News","LGHH","LG_H","None","None","None","None","None","LGHH","LG_H","Road","SM_H","None"],
            ["None","None","None","None","None","None","Mis2","LG_H","LG_H","None","SM_H","SM_H","SM_H","None","LG_H","LG_H","Road","SM_H","None"],
            ["None","None","None","None","HOSP","HOSP","Road","Road","Road","Magic","Road","Road","Road","Game","Road","Road","Road","SM_H","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Dubai():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","Road","Road","Road","Road","Road","Road","SM_H","SM_H","SM_H","None","None","None","None","None","None"],
            ["None","None","None","Road","None","None","None","None","None","Mis2","Road","Road","Road","None","None","None","None","None","None"],
            ["None","None","None","Road","Jail","Jail","None","None","None","None","None","None","Shop","None","None","None","None","None","None"],
            ["None","None","None","Add5","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","Road","Road","Road","Add1C","None","None","None","None","None","Road","SM_H","LGHH","LG_H","None","None","None"],
            ["None","None","None","None","None","None","Bank","None","None","None","None","None","Road","SM_H","LG_H","LG_H","None","None","None"],
            ["None","None","None","SM_H","SM_H","SM_H","News","None","None","None","None","None","Add2","Road","Road","Road","SM_H","None","None"],
            ["None","None","None","Road","Road","Road","Magic","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","LGHH","LG_H","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","LG_H","LG_H","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","None"],
            ["None","Road","Road","Game","None","None","None","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","None"],
            ["None","Add2","None","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","Road","SM_H","None","None"],
            ["None","Lott","None","None","None","None","None","SM_H","SM_H","SM_H","LG_H","LG_H","None","None","None","Road","SM_H","None","None"],
            ["None","Mis2","SM_H","SM_H","SM_H","SM_H","Bank","Road","Road","Road","Road","Road","SM_H","SM_H","SM_H","Road","SM_H","None","None"],
            ["None","Shop","Road","Road","Road","Road","News","None","None","None","None","Add1C","Road","Road","Road","Add5","HOSP","HOSP","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Africa():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Shop","Road","Road","Road","Road","Road","Road","Add10","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","Game","SM_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None"],
            ["None","None","None","SM_H","SM_H","SM_H","SM_H","Road","SM_H","None","None","None","None","None","Add1C","Road","Road","Road","Road","Road","LGHH","LG_H","None","None","None","None","None"],
            ["None","None","None","Road","Road","Road","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Magic","LG_H","LG_H","None","None","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Bank","Road","Road","HOSP","HOSP","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","News","Lott","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Shop","Jail","Jail","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","News","Road","SM_H","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Bank","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add1C","Mis2","None","None","None"],
            ["None","Shop","Road","Road","LGHH","LG_H","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Magic","LG_H","LG_H","Road","Road","Road","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","None","Game","Road","Road","Add1C","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Add2","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","News","Add1C","Road","SM_H","None","None","None","None","None","None","None","Lott","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Bank","Road","SM_H","None","None","None","None","None","None","Add1C","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","News","Road","SM_H","None","None","None","None","SM_H","SM_H","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None","Road","Road","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","LGHH","LG_H","None","Road","SM_H","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Lott","Add10","Magic","LG_H","LG_H","News","Road","SM_H","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","Game","Road","Road","Shop","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Venice():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","LG_H","LG_H","SM_H","SM_H","SM_H","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None","None"],
            ["None","None","None","Lott","Road","Road","Road","Road","Road","None","None","None","SM_H","SM_H","SM_H","LG_H","LG_H","None","None","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","News","SM_H","SM_H","SM_H","Road","Road","Road","Road","Road","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","Road","Road","Road","Road","Add1C","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","SM_H","None","None","None"],
            ["None","Game","Add1C","Mis2","None","None","None","None","None","None","None","None","None","None","None","Magic","None","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","News","SM_H","SM_H","SM_H","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","Game","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None"],
            ["None","News","SM_H","SM_H","SM_H","SM_H","LGHH","LG_H","None","None","None","None","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","Road","SM_H","None"],
            ["None","Road","Road","Road","Road","Road","LG_H","LG_H","SM_H","None","None","Bank","Road","Road","Road","Road","Road","Road","Road","Road","None","None"],
            ["None","None","None","None","None","Magic","Road","Road","Road","None","None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","None","Road","LG_H","LG_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","None","Road","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","Road","Road","Road","Road","Road","SM_H","None","Magic","Lott","Road","Road","Road","Road","Road","None","None","None","None"],
            ["None","None","None","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","LGHH","LG_H","Road","None","None","None","None"],
            ["None","None","None","Road","LG_H","LG_H","SM_H","SM_H","None","None","None","None","None","SM_H","SM_H","LG_H","LG_H","Road","None","None","None","None"],
            ["None","None","None","Shop","Road","Road","Road","Road","Road","None","None","None","Road","Road","Road","Road","Road","Shop","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Mis5","None","None","None","Mis5","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","Jail","Jail","Road","Add2","Bank","Add2","Road","HOSP","HOSP","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class London():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","None","None","None"],
            ["None","None","None","None","None","SM_H","SM_H","SM_H","None","SM_H","SM_H","LG_H","LG_H","None","None","None","None"],
            ["None","None","None","None","None","Road","Road","Road","Add1C","Road","Road","Road","Road","None","None","None","None"],
            ["None","HOSP","None","LGHH","LG_H","Road","SM_H","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","HOSP","None","LG_H","LG_H","Road","SM_H","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Add2","Mis5","Road","Road","Add5","None","None","None","None","None","None","Road","Road","SM_H","None","None"],
            ["None","Game","None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","SM_H","SM_H","Road","SM_H","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","Road","Road","Magic","Jail","Jail","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","Bank","None","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","None","None","None","News","SM_H","SM_H","SM_H","None","None"],
            ["None","Mis2","SM_H","SM_H","None","None","None","None","None","None","None","Road","Road","Road","Road","None","None"],
            ["None","Magic","Road","Road","Shop","None","None","None","None","None","None","None","None","None","Road","SM_H","None"],
            ["None","None","None","None","Road","None","None","None","None","None","None","SM_H","SM_H","SM_H","Road","SM_H","None"],
            ["None","None","None","None","News","None","None","None","None","None","None","Road","Road","Road","Road","None","None"],
            ["None","None","None","None","Road","None","None","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","Road","LGHH","LG_H","None","None","None","None","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","Road","LG_H","LG_H","None","SM_H","SM_H","SM_H","Road","LGHH","LG_H","None","None","None"],
            ["None","None","None","None","Mis2","SM_H","SM_H","SM_H","Road","Road","Road","Road","LG_H","LG_H","None","None","None"],
            ["None","None","None","None","Lott","Road","Road","Road","Add1C","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class NewYork():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","LGHH","LG_H","HOSP","None","None","None","None"],
            ["None","None","SM_H","SM_H","SM_H","LG_H","LG_H","HOSP","None","None","None","None"],
            ["None","None","Road","Road","Road","Road","Road","Add1C","None","None","None","None"],
            ["None","None","News","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","Road","SM_H","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","Road","SM_H","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","Road","SM_H","None","None","None","Add2","None","None","None","None"],
            ["None","None","Bank","None","None","None","None","Lott","Road","LGHH","LG_H","None"],
            ["None","None","Road","SM_H","None","None","None","None","Road","LG_H","LG_H","None"],
            ["None","None","Road","SM_H","None","None","None","None","Road","SM_H","None","None"],
            ["None","Magic","Road","SM_H","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","Add2C","Game","None","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","Road","SM_H","None"],
            ["None","Add2","None","None","None","None","None","None","None","Road","SM_H","None"],
            ["None","Road","LGHH","LG_H","None","None","None","None","None","Road","SM_H","None"],
            ["None","Road","LG_H","LG_H","None","None","None","None","None","Road","SM_H","None"],
            ["None","Lott","Road","SM_H","None","None","None","None","Mis2","Road","SM_H","None"],
            ["None","None","Road","SM_H","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","Road","SM_H","None","None","None","None","Road","SM_H","None","None"],
            ["None","None","Road","SM_H","None","None","None","None","Road","SM_H","None","None"],
            ["None","Game","Road","SM_H","None","None","None","None","Magic","None","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","SM_H","None","None","None","None","None","Road","SM_H","None","None"],
            ["None","Road","SM_H","None","None","None","None","Bank","Road","SM_H","None","None"],
            ["None","Road","SM_H","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Add1C","None","None","None","None","None","Road","SM_H","None","None","None"],
            ["None","Mis2","SM_H","SM_H","None","None","None","Road","LGHH","LG_H","None","None"],
            ["None","Shop","Road","Road","LGHH","LG_H","Add1C","Road","LG_H","LG_H","None","None"],
            ["None","None","None","Mis2","LG_H","LG_H","News","None","None","None","None","None"],
            ["None","None","None","Add5","Road","Road","Mis5","Jail","Jail","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class HolidayTown():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","HOSP","None","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","None"],
            ["None","HOSP","None","None","None","SM_H","Road","Road","Road","Road","SM_H","None","None","None","None","None"],
            ["None","Add5","Road","Mis2","None","Road","Road","None","None","Road","Road","SM_H","None","None","None","None"],
            ["None","Road","None","Road","SM_H","Road","SM_H","LGHH","LG_H","None","Road","Road","SM_H","SM_H","None","None"],
            ["None","Road","None","Road","SM_H","Road","Magic","LG_H","LG_H","None","None","Road","Road","Road","None","None"],
            ["None","Road","None","Road","SM_H","None","Add20","Road","Road","SM_H","None","None","None","Road","SM_H","None"],
            ["None","Road","None","News","None","None","None","None","Mis20","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","None","Shop","Road","SM_H","None","None","None","Add20","Road","None","None","Road","SM_H","None"],
            ["None","Road","None","None","Add2","None","None","None","None","None","Road","SM_H","None","Game","None","None"],
            ["Magic","Lott","None","None","Mis2","Road","SM_H","None","None","SM_H","Road","SM_H","None","Road","SM_H","None"],
            ["Road","SM_H","None","None","None","Add5","SM_H","None","None","Road","News","None","None","Road","SM_H","None"],
            ["Road","SM_H","None","None","None","Mis5","Road","LGHH","LG_H","Mis10","None","None","None","Road","SM_H","None"],
            ["Road","SM_H","None","LGHH","LG_H","None","Road","LG_H","LG_H","Add10","None","None","Add2","Lott","None","None"],
            ["Game","SM_H","SM_H","LG_H","LG_H","None","Road","Road","Road","Road","None","None","Road","None","None","None"],
            ["News","Road","Road","Road","Road","None","LGHH","LG_H","None","None","None","None","Road","Jail","Jail","None"],
            ["None","None","None","None","Road","SM_H","LG_H","LG_H","SM_H","None","None","None","Road","None","None","None"],
            ["None","None","None","None","Add2C","Road","Road","Road","Road","None","LGHH","LG_H","Road","Road","None","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","LG_H","LG_H","SM_H","Road","None","None"],
            ["None","None","None","None","None","None","None","None","Shop","Road","Road","Road","Road","Bank","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]
        self.BG = None

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class Taiwan():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","SM_H","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Road","Road","SM_H","LGHH","LG_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","SM_H","Road","Add5","Land","Add5","Road","LG_H","LG_H","LGHH","LG_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","LG_H","LG_H","Road","Add5","Land","Land","Land","Add5","Road","Road","LG_H","LG_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Road","Shop","Land","Land","Land","Land","Land","Land","Add2","Road","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Road","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Add2","Road","HOSP","HOSP","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Road","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Road","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","SM_H","Road","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LGHH","LG_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Bank","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LG_H","LG_H","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Lott","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Shop","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Shop","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","News","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Shop","Road","SM_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Magic","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LGHH","LG_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LG_H","LG_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","Road","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","News","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Add1C","Magic","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","Road","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","Add2C","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Mis2","Road","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","News","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LGHH","LG_H","None","None","None","None","None","None","None","None"],
            ["None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LG_H","LG_H","None","None","None","None","None","None","None","None"],
            ["None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Mis2","Road","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None"],
            ["None","News","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Shop","Jail","Jail","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","Mis2","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","News","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","Road","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","Road","Road","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","Road","LGHH","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Land","Road","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","Road","LG_H","LG_H","Land","Land","Land","Land","Land","Land","Land","Land","Shop","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","Road","Lott","SM_H","Land","Land","Land","Land","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","Add2","Road","SM_H","LGHH","LG_H","Land","Land","Land","Land","News","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","Bank","Road","LG_H","LG_H","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Game","Road","Road","Land","Land","Land","Land","Road","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","Road","Road","LGHH","LG_H","Road","Mis2","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Road","LG_H","LG_H","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","Road","Road","SM_H","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","SM_H","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Game","Bank","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = "Sea"
        self.Land = rgb(85,125,70)

        self.width = len(self.Map[0])
        self.height = len(self.Map)


class CirclilyWorld():
    def __init__(self):
        self.Map = [
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","None","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","SM_H","None","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","SM_H","LG_H","LG_H","Add1C","Road","Road","Road","Road","Road","Road","Road","Road","Road","Add1C","LG_H","LG_H","SM_H","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","SM_H","LG_H","LG_H","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","LG_H","LG_H","SM_H","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","LGHH","LG_H","SM_H","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","SM_H","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","LG_H","LG_H","Road","Road","None","None","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","SM_H","SM_H","SM_H","SM_H","None","None","None","None","None","Road","Road","LG_H","LG_H","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","SM_H","Road","Road","Road","None","LGHH","LG_H","SM_H","SM_H","SM_H","Road","Road","Road","Road","SM_H","None","SM_H","Road","Road","Road","Road","SM_H","SM_H","SM_H","LGHH","LG_H","None","Road","Road","Road","SM_H","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","SM_H","Road","Road","None","None","None","LG_H","LG_H","Road","Road","Road","Road","None","None","Road","Road","None","Road","Road","None","None","Road","Road","Road","Road","LG_H","LG_H","None","None","None","Road","Road","SM_H","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","SM_H","Road","Bank","None","None","None","SM_H","Road","Road","Road","None","None","None","LGHH","LG_H","SM_H","Road","None","Road","SM_H","LGHH","LG_H","None","None","None","Road","Road","Road","SM_H","None","None","None","Bank","Road","SM_H","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","SM_H","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","None","None","LG_H","LG_H","Road","Road","None","Road","Road","LG_H","LG_H","None","None","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","SM_H","None","None","None","None","None","None"],
            ["None","None","None","None","None","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","SM_H","SM_H","SM_H","Road","Road","Road","None","None","None","Road","Road","Road","SM_H","SM_H","SM_H","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","None","None","None","None","None","None"],
            ["None","None","None","Jail","None","News","None","None","None","SM_H","Road","Road","None","None","None","SM_H","Road","Road","Road","Road","None","None","None","None","None","None","None","Road","Road","Road","Road","SM_H","None","None","None","Road","Road","SM_H","None","None","None","News","None","HOSP","None","None","None","None"],
            ["None","None","None","Jail","Road","Road","None","None","SM_H","Road","Road","None","None","SM_H","SM_H","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","SM_H","SM_H","None","None","Road","Road","SM_H","None","None","Road","Road","HOSP","None","None","None","None"],
            ["None","None","None","Road","Road","None","None","SM_H","Road","Road","None","None","SM_H","Road","Road","Road","None","None","None","SM_H","SM_H","SM_H","None","None","None","SM_H","SM_H","SM_H","None","None","None","Road","Road","Road","SM_H","None","None","Road","Road","SM_H","None","None","Road","Road","None","None","None","None"],
            ["None","None","None","Road","None","None","None","Road","Road","None","None","None","Road","Road","None","None","None","None","SM_H","Road","Road","Road","None","None","None","Road","Road","Road","SM_H","None","None","None","None","Road","Road","None","None","None","Road","Road","None","None","None","Road","None","None","None","None"],
            ["None","None","None","Road","None","None","None","Road","None","None","None","SM_H","Road","None","None","None","None","Road","Road","Road","None","Road","Road","None","Road","Road","None","Road","Road","Road","None","None","None","None","Road","SM_H","None","None","None","Road","None","None","None","Road","None","None","None","None"],
            ["None","None","News","Road","None","None","Bank","Road","None","None","SM_H","Road","Bank","None","None","None","Road","Road","None","None","None","SM_H","Road","None","Road","SM_H","None","None","None","Road","Road","None","None","None","Bank","Road","SM_H","None","None","Road","Bank","None","None","Road","News","None","None","None"],
            ["None","None","Road","None","None","None","Road","None","None","None","Road","Road","None","None","None","Add1C","Road","None","None","None","SM_H","Road","Road","None","Road","Road","SM_H","None","None","None","Road","Add1C","None","None","None","Road","Road","SM_H","None","None","Road","None","None","None","Road","None","None","None"],
            ["None","None","Road","None","None","None","Road","None","None","None","Road","SM_H","None","None","News","Magic","None","None","None","SM_H","Road","Road","None","None","None","Road","Road","SM_H","None","None","None","Magic","News","None","None","None","Road","SM_H","None","None","Road","None","None","None","Road","None","None","None"],
            ["None","Add1C","Road","None","None","Road","Road","None","None","None","Road","SM_H","None","None","Road","None","None","None","SM_H","Road","Road","None","None","None","None","None","Road","Road","SM_H","None","None","None","Road","None","None","None","Road","SM_H","None","None","Road","Road","SM_H","None","Road","Add1C","None","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","Road","SM_H","None","Road","Road","None","None","SM_H","Road","Road","None","None","None","None","None","None","None","Road","Road","SM_H","None","None","Road","Road","SM_H","None","Road","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","Road","None","None","None","None","None","None","None","None","None","Road","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Mis20","Mis2","Add3C","Mis2","Mis20","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Add5","None","None","None","Add2","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Add20","None","None","None","Add10","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Add10","None","None","None","Add20","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","None","None","None","Add2","None","None","None","Add5","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","SM_H","None","None","Road","SM_H","None","None","Road","None","None","None","Road","None","None","None","Road","Road","None","None","Road","Road","None","Road","Road","None","None","Road","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Road","None","None","None","Road","None","None","None","News","Road","None","None","Road","Add2","None","None","None","News","Road","SM_H","SM_H","Road","None","Road","SM_H","SM_H","Road","Bank","None","None","None","Mis2","Road","SM_H","None","News","Road","None","None","None","Road","SM_H","None","None","Road","SM_H","None"],
            ["None","Add1C","Road","SM_H","None","Road","Road","SM_H","None","None","Road","None","None","None","Add5","None","None","None","None","Road","Road","Road","Game","None","Game","Road","Road","Road","None","None","None","None","Mis5","None","None","None","Road","None","None","None","Road","Road","SM_H","None","Road","Add1C","None","None"],
            ["None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","SM_H","None","None","Road","Bank","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Bank","Road","None","None","SM_H","Road","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None"],
            ["None","None","Road","SM_H","None","None","Road","None","None","None","Magic","Road","SM_H","None","None","Road","Road","None","LGHH","LG_H","None","None","None","None","None","None","None","LGHH","LG_H","None","Road","Road","None","None","SM_H","Road","Magic","None","None","None","Road","SM_H","None","None","Road","SM_H","None","None"],
            ["None","None","Road","Road","SM_H","None","Road","Road","SM_H","None","None","Road","Road","None","None","None","Road","Road","LG_H","LG_H","LGHH","LG_H","None","None","None","LGHH","LG_H","LG_H","LG_H","Road","Road","None","None","None","Road","Road","None","None","None","SM_H","Road","SM_H","None","News","Road","SM_H","None","None"],
            ["None","None","None","Road","SM_H","None","None","Road","SM_H","None","None","None","Road","SM_H","LGHH","LG_H","None","Road","Road","Road","LG_H","LG_H","None","None","None","LG_H","LG_H","Road","Road","Road","None","LGHH","LG_H","SM_H","Road","None","None","None","SM_H","Road","Road","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","Road","SM_H","None","None","Road","Road","SM_H","None","None","Road","Road","LG_H","LG_H","None","None","None","Road","Road","Road","None","None","None","Road","Road","Road","None","None","None","LG_H","LG_H","Road","Road","None","None","SM_H","Road","Road","None","None","None","Road","SM_H","None","None","None"],
            ["None","None","None","Road","Road","SM_H","None","None","Road","Road","SM_H","None","None","Bank","Road","Road","SM_H","None","LGHH","LG_H","None","Road","Road","None","Road","Road","None","LGHH","LG_H","None","SM_H","Road","Road","Bank","None","None","SM_H","Road","Road","None","None","None","Road","Road","SM_H","None","None","None"],
            ["None","None","None","None","Road","Road","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","SM_H","LG_H","LG_H","None","SM_H","Road","None","Road","SM_H","None","LG_H","LG_H","SM_H","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","Road","Road","SM_H","None","None","None","None"],
            ["None","None","None","None","None","Road","SM_H","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","Road","Road","SM_H","Road","Road","None","Road","Road","SM_H","Road","Road","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","SM_H","Road","None","None","None","None","None","None"],
            ["None","None","None","None","None","News","Road","SM_H","None","None","None","Road","Road","SM_H","None","None","None","None","None","Road","Road","Road","None","None","None","Road","Road","Road","None","None","None","None","None","SM_H","Road","Road","None","None","None","SM_H","Road","News","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","SM_H","SM_H","LGHH","LG_H","None","None","None","None","None","None","None","None","None","None","None","LGHH","LG_H","SM_H","SM_H","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","Road","Road","SM_H","None","None","None","Road","Road","Road","LG_H","LG_H","SM_H","LGHH","LG_H","None","None","None","None","None","LGHH","LG_H","SM_H","LG_H","LG_H","Road","Road","Road","None","None","None","SM_H","Road","Road","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","Bank","Road","SM_H","SM_H","None","None","None","Road","Road","Road","Road","LG_H","LG_H","SM_H","None","None","None","SM_H","LG_H","LG_H","Road","Road","Road","Road","None","None","None","SM_H","SM_H","Road","Bank","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","Road","Road","Road","SM_H","LGHH","LG_H","None","None","None","Road","Road","Road","Road","SM_H","None","SM_H","Road","Road","Road","Road","None","None","None","LGHH","LG_H","SM_H","Road","Road","Road","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","Road","Road","LG_H","LG_H","SM_H","None","None","None","None","None","Road","Road","None","Road","Road","None","None","None","None","None","SM_H","LG_H","LG_H","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","SM_H","SM_H","SM_H","LGHH","LG_H","SM_H","Road","None","Road","SM_H","LGHH","LG_H","SM_H","SM_H","SM_H","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Road","Road","Road","Road","LG_H","LG_H","Road","Road","None","Road","Road","LG_H","LG_H","Road","Road","Road","Road","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","Add1C","Road","Road","Road","None","None","None","Road","Road","Road","Add1C","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"],
            ["None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None","None"]
        ]

        self.BG = "OverCast"

        self.width = len(self.Map[0])
        self.height = len(self.Map)





###########################################################################
#----------------------------Map Builder Class----------------------------#
###########################################################################
class Maps():
    def __init__(self):
        self.Walkable = ["Lott","Game",
        "Add1C","Add2C","Add3C","Magic","Road","Bank",
        "Add2","Add5","Add10","Add20","Mis2","Mis5","Mis10","Mis20",
        "News","Shop"]
        self.All_Maps = [
            Shanghai,Taiwan,RichManCity,SpaceStation,Paris,Japan,SnowKingdom,Greece,Dubai,Africa,Venice,London,NewYork,HolidayTown,CirclilyWorld
        ]

    def SelectRandomMap(self):
        return self.All_Maps[randint(0, len(self.All_Maps)-1)]()

    def SelectTestMap(self, Map):
        self.Map = Map()
        return self.Map

    def Build(self, Map):
        Sky(choice=Map.BG) #天空渲染
        Block_Bindings = {} #地圖容器
        Walkable_Bindings = {}
        self.Binded = set() #儲存綁定過的格子
        PlayerFloor = set() #儲存可放置玩家的格子
        Hospital_Jail = {}

        #生成地圖
        for x in range(Map.width):
            for z in range(Map.height):
                BlockInfo = Map.Map[z][x]
                if BlockInfo != "None":
                    #道路格
                    if BlockInfo in self.Walkable:
                        if BlockInfo == "Road":
                            Walkable_Bindings[(z,x)] = Road(pos=(x,0,Map.height-z), Arrpos=(z,x), Color=color.black)
                        else:
                            if BlockInfo == "Bank":
                                _ = Bank(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo == "News":
                                _ = News(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo == "Shop":
                                _ = Shop(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo == "Lott":
                                _ = Lott(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo == "Game":
                                _ = Game(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo == "Magic":
                                _ = Magic(pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo[0:3] == "Add":
                                if BlockInfo[-1] == "C":
                                    _ = AddCard(int(BlockInfo[3:-1]), pos=(x,0,Map.height-z), Arrpos=(z,x))
                                else:
                                    _ = Add(int(BlockInfo[3:]), pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                            elif BlockInfo[0:3] == "Mis":
                                _ = Mis(int(BlockInfo[3:]), pos=(x,0,Map.height-z), Arrpos=(z,x))
                                Block_Bindings[(z,x)] = _
                                Walkable_Bindings[(z,x)] = _
                        PlayerFloor.add((x, Map.height-z))
                    
                    #房屋格
                    else:
                        if BlockInfo == "LGHH":
                            #找非特殊格子的道路來綁定大型建築
                            if Map.Map[z+2][x]=="Road" and Map.Map[z+2][x+1]=="Road" and (z+2,x) not in self.Binded and (z+2,x+1) not in self.Binded:
                                _ = LargeBuilding(bindWith=[(z+2,x), (z+2,x+1)], pos=(x+0.5,0,Map.height-z-0.5))
                                Block_Bindings[(z+2,x)] = _
                                Block_Bindings[(z+2,x+1)] = _
                                self.Binded.add((z+2,x))
                                self.Binded.add((z+2,x+1))
                            elif Map.Map[z][x-1]=="Road" and Map.Map[z+1][x-1]=="Road" and (z,x-1) not in self.Binded and (z+1,x-1) not in self.Binded:
                                _ = LargeBuilding(bindWith=[(z,x-1), (z+1,x-1)], pos=(x+0.5,0,Map.height-z-0.5))
                                Block_Bindings[(z,x-1)] = _
                                Block_Bindings[(z+1,x-1)] = _
                                self.Binded.add((z,x-1))
                                self.Binded.add((z+1,x-1))
                        elif BlockInfo == "SM_H":
                            #找非特殊格子的道路來綁定普通房屋
                            if Map.Map[z+1][x]=="Road" and (z+1,x) not in self.Binded:
                                _ = SmallBuilding(bindWith=[(z+1,x)], pos=(x,0,Map.height-z), faceDown=True)
                                Block_Bindings[(z+1,x)] = _
                                self.Binded.add((z+1,x))
                            elif Map.Map[z][x-1]=="Road" and (z,x-1) not in self.Binded:
                                _ = SmallBuilding(bindWith=[(z,x-1)], pos=(x,0,Map.height-z), faceDown=False)
                                Block_Bindings[(z,x-1)] = _
                                self.Binded.add((z,x-1))
                        elif BlockInfo == "Land" and Map.Land:
                            Road(pos=(x,0,Map.height-z), Color=Map.Land)
                        elif BlockInfo == "HOSP" or BlockInfo == "Jail":
                            IsBuilding = False
                            if Map.Map[z-1][x] == BlockInfo:
                                if Map.Map[z-2][x] in self.Walkable:
                                    IsBuilding = True
                            if Map.Map[z+1][x] == BlockInfo:
                                if Map.Map[z+2][x] in self.Walkable:
                                    IsBuilding = True
                            if Map.Map[z][x-1] == BlockInfo:
                                if Map.Map[z][x-2] in self.Walkable:
                                    IsBuilding = True
                            if Map.Map[z][x+1] == BlockInfo:
                                if Map.Map[z][x+2] in self.Walkable:
                                    IsBuilding = True
                            if IsBuilding:
                                if BlockInfo == "Jail":
                                    Jail(pos=(x,0,Map.height-z), Texture=load_texture(f"assets/UVmap/{BlockInfo}.png"), IsBuilding=True)
                                elif BlockInfo == "HOSP":
                                    Hospital(pos=(x,0,Map.height-z), Texture=load_texture(f"assets/UVmap/{BlockInfo}.png"), IsBuilding=True)
                            else:
                                if BlockInfo == "Jail":
                                    Jail(pos=(x,0,Map.height-z), Texture=load_texture(f"assets/UVmap/{BlockInfo}.png"))
                                    Hospital_Jail["Jail"] = (x,0,Map.height-z)
                                elif BlockInfo == "HOSP":
                                    Hospital(pos=(x,0,Map.height-z), Texture=load_texture(f"assets/UVmap/{BlockInfo}.png"))
                                    Hospital_Jail["HOSP"] = (x,0,Map.height-z)
        return list(PlayerFloor), Block_Bindings, Walkable_Bindings, Hospital_Jail