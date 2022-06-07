"""
此程式用來測試地圖是否正常運作
讓四位玩家環繞地圖移動
"""
from random import randint
from ursina import *
from Classes import *
from MapClasses import *


def pp(inf):
    for _ in inf.items():
        if type(_)==dict:
            for _z in inf.items():
                print(_z[1])
        else:
            print(_[1])


#最小 正常 最大 縮放值
MIN_ZOOM_IN = 8
NORMAL_ZOOM = 10
MAX_ZOOM_IN = 50


PLAYERS = [color.red, color.green, color.white, color.orange]

#載入地圖
MAP = Maps().SelectTestMap(SpaceStation)

#地圖寬度 地圖長度
MAP_WIDTH = MAP.width
MAP_LENGTH = MAP.height

#主程式
Game = Ursina()
window.borderless = True
window.exit_button.visible = False
window.fps_counter.visible = False

camera.position = (-6, NORMAL_ZOOM, -20) # 預設鏡頭位置
camera.rotation_x = 30 #x軸正向順時針旋轉30度
camera.rotation_y = 30 #y軸正向順時針旋轉30度

# a = GUI(color.red)

putPlayer, Bindings, WalkableBlocks, Hospital_Jail = Maps().Build(MAP)

#隨機放置玩家
players = []
for i in range(4):
    px, pz = putPlayer.pop(randint(0, len(putPlayer)-1))
    g = len(putPlayer)
    print(px, pz)
    players.append(
        Player(
                Idenity=PLAYERS[i], map=MAP, mapBindings=Bindings, start=(px, 0, pz), 
                Walkable_Bindings=WalkableBlocks, Hospital_Jail=Hospital_Jail,
                ID=i+1, SoundPlayer=[False]*10, DefaultBalance=0, DefaultBank=0, speed=1
            )
    )

dice = Dice(pos=(10,3,9), Scale=0.5, Color=color.white, Model="CubeModel")

g = t = dc = 0
sp = 10
go = False
States = [
    20
]
k=[0, 0, 0]
go = None
Dice_Animation = refreshed = point = d = Stop = None
def update():
    global States, point, go, Dice_Animation, refreshed, k, d, Stop, g, t, dc, sp
    if g%2500==0:
        for i in range(len(players)): players[i].move(10)
        g=0
    else:
        g+=1

def input(key):
    #取得滑鼠點擊位置
    global X_o, Y_o, X_e, Y_e
    if key=="left mouse down":
        O_pos = mouse.position
        X_o, Y_o, _ = O_pos

    #取得滑鼠釋放位置
    if key=="left mouse up":
        E_pos = mouse.position
        X_e, Y_e, _ = E_pos
        #鏡頭移動三角函數示意圖見 -> 附圖(一)
        X_move_x = ((X_o-X_e) * 10) #x變化量
        Y_move_y = ((Y_o-Y_e) * 10) #y變化量
        X_move_y = ((X_o-X_e) * 10) / (3**0.5) #y要移動(回縮) x變化量*tan(30度)
        Y_move_x = ((Y_o-Y_e) * 10) / (3**0.5) #x要移動(補回) y變化量*tan(30度)
        Total_X_move = X_move_x+Y_move_x
        Total_Y_move = X_move_y-Y_move_y
        if int(abs(Total_X_move*10))>1 or int(abs(Total_Y_move*10))>1:
            camera.position = (
                camera.position[0]+Total_X_move,
                camera.position[1], 
                camera.position[2]-Total_Y_move
            )

    #鏡頭縮進
    if key=="scroll up":
        if camera.position[1] >= MIN_ZOOM_IN:
            camera.position = (
                camera.position[0]+0.5,
                camera.position[1]-1,
                camera.position[2]+1
            )

    #鏡頭拉遠
    if key=="scroll down":
        if camera.position[1] <= MAX_ZOOM_IN:
            camera.position = (
                camera.position[0]-0.5,
                camera.position[1]+1,
                camera.position[2]-1
            )

Game.run()