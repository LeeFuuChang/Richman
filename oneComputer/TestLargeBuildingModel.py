"""
測試建築與方塊用檔案
"""
from ursina import *
from Classes import *
from Systems import *
MIN_ZOOM_IN = 3
NORMAL_ZOOM = 10
MAX_ZOOM_IN = 30
app = Ursina()
window.title = "RichManYeah"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

camera.position = (-6, NORMAL_ZOOM, -20) # 預設鏡頭位置
camera.rotation_x = 30 #x軸正向順時針旋轉30度
camera.rotation_y = 30 #y軸正向順時針旋轉30度


a = Road(Color=color.black)

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
app.run()