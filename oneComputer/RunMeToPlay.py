from random import randint

import pygame
from ursina import *

from Needed_Modules.CameraControl import *
from Needed_Modules.CardSystems import *
from Needed_Modules.Classes import *
from Needed_Modules.GUISystems import *
from Needed_Modules.MapClasses import *
from Needed_Modules.MiniGame import MiniGame
from Needed_Modules.Systems import *

Game = Ursina()





#主程式 3D引擎初始化
window.title = "RichManYeah"
window.borderless = False
window.exit_button.visible = False
window.exit_button.disabled = True
window.fps_counter.visible = False





pygame.init()
BG_MusicPlayer = pygame.mixer.music
BG_MusicPlayer.load("assets/music/audio1.mp3")

Walking_Sound = pygame.mixer.Sound("assets/music/Walking.mp3")

Music_Sound_Players = [
    BG_MusicPlayer,
    Walking_Sound
]





#預載入系統
preloader = Preloader()
preloader.Show_Loading_Bar()
preload_Function = preloader.Preload_Models()
#遊戲狀態
GameStat = {
    "Turn":[True, False, False, False],
    "GUIstuff":False,
    "Game":False,
    "Play":False,
    "Round":1,
    "DefaultRising":0,
    "LotteryOpening": False
}





players = []
Result = Result_Function = None
idx = 0





def Main(Map, PlayerColors, DefaultBalance, DefaultBank, DefaultPriceRising):
    global update, input, Game, players, GameStat, Result_Function, Result, idx, system, EndTurn, Card_system, GUI_system, preloader, preload_Function, Music_Sound_Players, MAP_WIDTH, MAP_LENGTH
    #載入地圖 地圖寬度 地圖長度
    MAP = Map
    MAP_WIDTH = MAP.width
    MAP_LENGTH = MAP.height
    PLAYERS_COLOR = PlayerColors
    GameStat["DefaultRising"] = DefaultPriceRising




    #初始化鏡頭參數
    camera.position = (-6, NORMAL_ZOOM, -20) # 預設鏡頭位置
    camera.rotation_x = 30 #x軸正向順時針旋轉30度
    camera.rotation_y = 30 #y軸正向順時針旋轉30度





    #建立地圖 取得建築格子綁定 玩家可放置格子
    putPlayer, Bindings, WalkableBlocks, Hospital_Jail = Maps().Build(MAP)





    #隨機放置電腦玩家
    for i in range(4):
        px, pz = putPlayer.pop(randint(0, len(putPlayer)-1))
        _player = Player(
            Idenity = PLAYERS_COLOR[i], 
            map = MAP,
            Walkable_Bindings = WalkableBlocks,
            mapBindings = Bindings, 
            Hospital_Jail = Hospital_Jail, 
            ID = i+1, 
            start = (px, 0, pz), 
            speed = 1, 
            SoundPlayer = Music_Sound_Players[1:],
            DefaultBalance = DefaultBalance,
            DefaultBank = DefaultBank
        )
        Ui = GUI(_player, _player.Property)
        _player.Bind_UI(Ui)
        _player.AddCard(1, TurnBackCrd)
        _player.AddCard(1, StopHereCrd)
        _player.AddCard(1, MoveAtSleep)
        _player.AddCard(1, ControlDice)
        players.append(_player)
    #綁定各玩家 (為了讓各玩家之前可以直接使用對方物件屬性
    for _player in players:
        _player.Bind_Other_Player(PlayerList=players)
    EndTurn = False





    #綁定遊戲GUI系統
    system = {
        "ChooseLargeBuilding":ChooseLargeBuilding(),
        "ChooseLottery":ChooseLottery(),
        "ChooseMagic":ChooseMagic(),
        "ChooseYesNo":ChooseYesNo(),
        "ShowNews":NewsAnnouncment(),
        "ShowShop":BuyCardShop(),
        "ShowBank":ShowBank(),
        "ShowGame":MiniGame(orgin=(100000, 100000, 100000)),
        "Wait":WaitDelay()
    }
    Make_System(syst=system)
    #綁定卡片使用系統
    Card_system = {
        "ChooseLargeBuilding":ChooseLargeBuilding(),
        "ChooseTarget":ChooseTarget(players),
        "ChoosePoint":ChoosePoint(),
        "ChooseYesNo":ChooseYesNo(),
    }
    Make_Card_Use_System(syst=Card_system)
    #綁定其他GUI系統
    GUI_system = {
        "Adjust":SettingsGUI(BG_MusicPlayer=Music_Sound_Players[0], Effect_SoundPlayer=Music_Sound_Players[1:]),
        "ChooseYesNo":ChooseYesNo(),
        "Help":HelpGUI(),
    }




def Gaming_Update_Function():
    global GameStat, update, Result, Result_Function, idx, EndTurn
    #主遊戲
    for player_idx, player in enumerate(players):
        if player.Property["Broke"]:
            if player.UI.Built:
                player.UI.Destroy_GUI()
            
            if player.Broke_Animater.play_Broken_Animation():
                system["ChooseLottery"].wipe(player)
                GameStat["Turn"].pop(player_idx)
                players.remove(player)

                for _player in players:
                    _player.Bind_Other_Player(PlayerList=players)

                system["Wait"].Wait(2)

                if GameStat["Turn"][player_idx]:
                    if player_idx+1<len(players):
                        GameStat["Turn"][player_idx+1] = True #下個玩家回合設置為True
                    else:
                        GameStat["Turn"][0] = True #下個玩家回合設置為True
                idx = GameStat["Turn"].index(True)
            return
    
    if len(players) == 1:
        Result = False
        update = GameOver_Upate_Function

    if GameStat["LotteryOpening"]:
        if system["ChooseLottery"].Open() != False:
            system["Wait"].Wait(2)
            GameStat["LotteryOpening"] = False

    if not any(player.Property["Announcing"] for player in players) and system["Wait"].finish:
        idx = GameStat["Turn"].index(True)
        if EndTurn:
            for player in players:
                player.Property["Round"] = GameStat["Round"]
                if player.UI.Built:
                    player.UI.Destroy_GUI()
                if player.Property["Balance"]+player.Property["Bank"] <= 0:
                    player.Broke()
                    return
            for EveryLargeBuilding in players[idx].Property["LargeHouse"].keys():
                EveryLargeBuilding.Building.Roundly_Function()
            EndTurn = False
            players[idx].Camera_Follow()
        if GameStat["Game"]:
            GameOver, Score = Result_Function()
            if GameOver:
                Print(f"Game Final Score: {Score}")
                EndTurn = True #結束回合
                players[idx].updateProperty() #刷新玩家資產
                players[idx].UI.Build_GUI() #將移除了的GUI建置回來
                camera.position = (-6, NORMAL_ZOOM, -20) # 預設鏡頭位置
                camera.rotation_x = 30 #x軸正向順時針旋轉30度
                camera.rotation_y = 30 #y軸正向順時針旋轉30度
                GameStat["Play"] = True
                GameStat["Game"] = False
            else:
                return

        elif GameStat["Play"]:
            #等待玩家回合結束
            if not Result:
                if not players[idx].UI.Built:
                    players[idx].UI.Build_GUI()
                Result, Result_Function = players[idx].Play_Step()
            else:
                #停止播放走路音效
                players[idx].Property["SoundEffects"]["Walking"].stop()
                #玩家結束 檢查回傳結果
                if Result == True: #回傳True: 回合結束 未觸發特殊事件
                    EndTurn = True
                else:
                    if players[idx].UI.Built:
                        players[idx].UI.Destroy_GUI() #移除GUI

                    if Result == "Pausefunction": #回傳函式: 暫停回合 (包含使用卡片、觸發特殊事件)
                        if Result_Function(): #建置回傳事件GUI同時檢查是否取得回傳值
                            players[idx].updateProperty() #刷新玩家資產
                            players[idx].UI.Build_GUI() #將移除了的GUI建置回來
                            Result = False #重置結果 繼續回合
                            return

                    elif Result == "Stopfunction": #回傳函式: 回合結束 觸發特殊事件
                        if Result_Function(): #建置回傳事件GUI同時檢查是否取得回傳值 取得則結束回合
                            EndTurn = True #結束回合
                            players[idx].updateProperty() #刷新玩家資產
                            players[idx].UI.Build_GUI() #將移除了的GUI建置回來

                    elif Result == "Game":
                        GameStat["Play"] = False
                        GameStat["Game"] = True
                        return

        if players[idx].UI.Built:
            GameStat["GUIstuff"] = players[idx].UI.refresh() #刷新GUI
            if GameStat["GUIstuff"]:
                update = GUI_Stuff_Upate_Function
                return

        if EndTurn: #如果回合結束了
            GameStat["Turn"][idx] = Result = False #把執行結果與該回合玩家重置為False
            if idx+1<len(players):
                GameStat["Turn"][idx+1] = True #下個玩家回合設置為True
            else:
                GameStat["Turn"][0] = True #下個玩家回合設置為True
                GameStat["Round"] += 1 #總回合數 ( 四位玩家都玩過的次數 ) += 1
                if GameStat["Round"]%GameStat["DefaultRising"] == 0:
                    for player in players:
                        player.Property["Rising"]+=1
                if GameStat["Round"]%30==0:
                    for player in players:
                        player.Property["Round"] = GameStat["Round"]
                        if players[player.ID-1].UI.Built:
                            players[player.ID-1].UI.Destroy_GUI()
                    GameStat["LotteryOpening"] = True
            system["Wait"].Wait(2)

    else:
        if idx < len(players):
            if not players[idx].UI.Built:
                players[idx].UI.Build_GUI()
            else:
                GameStat["GUIstuff"] = players[idx].UI.refresh() #刷新GUI
                if GameStat["GUIstuff"]:
                    for player in players:
                        if player.UI.Built:
                            player.UI.Destroy_GUI()
                    update = GUI_Stuff_Upate_Function
                    return
        else:
            idx -= 1





def GameOver_Upate_Function():
    global players, Result, update
    if not Result:
        if players[0].UI.Built:
            players[0].UI.Destroy_GUI()
        Result = players[0].Win_Animater.play_Win_Animation()
    else:
        if not players[0].UI.Built:
            players[0].UI.Build_GUI()
        else:
            GameStat["GUIstuff"] = players[0].UI.refresh() #刷新GUI
            if GameStat["GUIstuff"]:
                update = GUI_Stuff_Upate_Function
                return





def GUI_Stuff_Upate_Function():
    global GameStat, update, input
    #正在查看或欲退出遊戲
    idx = GameStat["Turn"].index(True)
    players[idx].UI.Destroy_GUI()
    if GameStat["GUIstuff"] == "Exit":
        if not system["ChooseYesNo"].Built:
            system["ChooseYesNo"].Build_GUI(text=f"Sure You want to Exit?")
            input = TempInputFunction
            return
        else:
            if system["ChooseYesNo"].Check():
                if system["ChooseYesNo"].Result:
                    application.quit()
                    quit()
            else:
                return

    elif GameStat["GUIstuff"] == "Help":
        if not GUI_system["Help"].Built:
            input = GUI_system["Help"].Build_GUI()
            return
        else:
            if not GUI_system["Help"].Check():
                return

    elif GameStat["GUIstuff"] == "Adjust":
        if not GUI_system["Adjust"].Built:
            GUI_system["Adjust"].Build_GUI()
            input = TempInputFunction
            return
        else:
            if not GUI_system["Adjust"].Check():
                return
    GameStat["GUIstuff"] = False
    players[idx].UI.Build_GUI()
    update = Gaming_Update_Function
    input = Temp_Input_Function





def PreLoad_Update_Function():
    global GameStat, update, input
    if not preloader.Loaded:
        next(preload_Function)
    else:
        preloader.Destory_Loading_Screen()
        Main(
            Map=StartGame.StartGameInfo["Map"], PlayerColors=StartGame.StartGameInfo["playerColors"],
            DefaultBalance=StartGame.StartGameInfo["DefaultBalance"], 
            DefaultBank=StartGame.StartGameInfo["DefaultBank"], 
            DefaultPriceRising=StartGame.StartGameInfo["DefaultPriceRising"]
        )
        GameStat["Play"] = True
        update = Gaming_Update_Function
        input = Temp_Input_Function
        Music_Sound_Players[0].play(loops=-1)
    return





def Temp_Input_Function(key):
    #用來過度其他視窗輸入輸出過程的切換
    #等待滑鼠並沒有按住
    #才切換成真正的鏡頭控制函式
    global input
    if key != "left mouse down":
        input = CameraControlFunction
#用來暫時取代輸入函數的無作用函數
def TempInputFunction(key):
    pass





StartGame = Start_RichMan_System()
def update():
    global update, StartGame
    if StartGame.Check():
        update = PreLoad_Update_Function

Game.run()
