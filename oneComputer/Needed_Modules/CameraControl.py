from ursina import *

#接受視窗滑鼠輸入輸出控制鏡頭移動
def CameraControlFunction(key):
    global X_o, Y_o, X_e, Y_e
    #取得滑鼠點擊位置
    if key=="left mouse down":
        O_pos = mouse.position
        X_o, Y_o, _ = O_pos


    #取得滑鼠釋放位置
    if key == "left mouse up":
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



    #鏡頭縮放控制
    #鏡頭縮進
    if key=="scroll up":
        if camera.position[1] >= 8:
            camera.position = (
                camera.position[0]+0.5,
                camera.position[1]-1,
                camera.position[2]+1
            )

    #鏡頭拉遠
    if key=="scroll down":
        if camera.position[1] <= 30:
            camera.position = (
                camera.position[0]-0.5,
                camera.position[1]+1,
                camera.position[2]-1
            )