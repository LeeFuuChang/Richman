from queue import PriorityQueue
import pygame
import os


WIDTH = 800
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Draw Map")


WHITE = (255, 255, 255)
BorderColor = (128, 128, 128)
Road_Color = (0, 0, 0)
LGHH_Color = (0, 0, 122)
LG_H_Color = (0, 0, 255)
SM_H_Color = (255, 0, 0)
Add2_Color = (0, 255, 0)
Add5_Color = (0, 122, 0)
Add10_Color = (122, 0, 0)
Add20_Color = (122, 122, 0)
Mis2_Color = (122, 0, 122)
Mis5_Color = (0, 122, 122)
Mis10_Color = (122, 255, 122)
Mis20_Color = (255, 0, 122)
Add1C_Color = (255, 122, 0)
Add2C_Color = (122, 255, 255)
Add3C_Color = (196, 255, 14)
Jail_Color = (122, 122, 122)
HOSP_Color = (255, 255, 0)
Magic_Color = (122, 122, 255)
Shop_Color = (255, 122, 122)
News_Color = (255, 122, 255)
Lott_Color = (185, 122, 86)
Game_Color = (92, 84, 149)
Bank_Color = (170, 60, 180)

class Point:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neightbor = []
        self.width = width
        self.total_rows = total_rows
        self.f = [self.make_LGHH,self.make_LG_H,self.make_SM_H,self.make_Add2,self.make_Add5,self.make_Add10,self.make_Add20,self.make_Mis2,self.make_Mis5,self.make_Mis10,self.make_Mis20,self.make_Add1C,self.make_Add2C,self.make_Add3C,self.make_Jail,self.make_HOSP,self.make_Magic,self.make_Shop,self.make_News,self.make_Lott,self.make_Game,self.make_Bank]

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.color = WHITE
        return "None"

    def make_Road(self):
        self.color = Road_Color
        return "Road"
    def make_LGHH(self):
        self.color = LGHH_Color
        return "LGHH"
    def make_LG_H(self):
        self.color = LG_H_Color
        return "LG_H"
    def make_SM_H(self):
        self.color = SM_H_Color
        return "SM_H"
    def make_Add2(self):
        self.color = Add2_Color
        return "Add2"
    def make_Add5(self):
        self.color = Add5_Color
        return "Add5"
    def make_Add10(self):
        self.color = Add10_Color
        return "Add10"
    def make_Add20(self):
        self.color = Add20_Color
        return "Add20"
    def make_Mis2(self):
        self.color = Mis2_Color
        return "Mis2"
    def make_Mis5(self):
        self.color = Mis5_Color
        return "Mis5"
    def make_Mis10(self):
        self.color = Mis10_Color
        return "Mis10"
    def make_Mis20(self):
        self.color = Mis20_Color
        return "Mis20"
    def make_Add1C(self):
        self.color = Add1C_Color
        return "Add1C"
    def make_Add2C(self):
        self.color = Add2C_Color
        return "Add2C"
    def make_Add3C(self):
        self.color = Add3C_Color
        return "Add3C"
    def make_Jail(self):
        self.color = Jail_Color
        return "Jail"
    def make_HOSP(self):
        self.color = HOSP_Color
        return "HOSP"
    def make_Magic(self):
        self.color = Magic_Color
        return "Magic"
    def make_Shop(self):
        self.color = Shop_Color
        return "Shop"
    def make_News(self):
        self.color = News_Color
        return "News"
    def make_Lott(self):
        self.color = Lott_Color
        return "Lott"
    def make_Game(self):
        self.color = Game_Color
        return "Game"
    def make_Bank(self):
        self.color = Bank_Color
        return "Bank"
    
    def ff(self,i):
        return self.f[i]

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    

def h(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2) + abs(y1-y2)


def reconstruct(come_from, current, draw, start):
    t=0
    _ = current
    while(_ in come_from):
        t+=1
        _ = come_from[_]
    print(t)
    while(current in come_from and t>1):
        t-=1
        current = come_from[current]
        current.make_path()
        draw()
    print(len(come_from))


def make_grid(rows, width):
    grid = []
    endMap = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            point = Point(i, j, gap, rows)
            grid[i].append(point)
    for i in range(rows):
        endMap.append([])
        for j in range(rows):
            endMap[i].append("None")
    return grid, endMap


def Update_UI(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, BorderColor, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, BorderColor, (j*gap, 0), (j*gap, width))


def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for point in row:
            point.draw(window)

    Update_UI(window, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(window, width):
    ROWS = 50
    grid, EndMap = make_grid(ROWS, width)
    os.system("cls")
    for _ in EndMap:
        print(*_)

    run = True
    started = False
    ended = True

    while(run):
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started and not ended:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                point = grid[row][col]

                EndMap[col][row] = point.make_Road()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                point = grid[row][col]
                
                EndMap[col][row] = point.reset()

            elif event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                point = grid[row][col]
                if event.key == pygame.K_a:
                    EndMap[col][row] = point.ff(0)()
                elif event.key == pygame.K_b:
                    EndMap[col][row] = point.ff(1)()
                elif event.key == pygame.K_c:
                    EndMap[col][row] = point.ff(2)()
                elif event.key == pygame.K_d:
                    EndMap[col][row] = point.ff(3)()
                elif event.key == pygame.K_e:
                    EndMap[col][row] = point.ff(4)()
                elif event.key == pygame.K_f:
                    EndMap[col][row] = point.ff(5)()
                elif event.key == pygame.K_g:
                    EndMap[col][row] = point.ff(6)()
                elif event.key == pygame.K_h:
                    EndMap[col][row] = point.ff(7)()
                elif event.key == pygame.K_i:
                    EndMap[col][row] = point.ff(8)()
                elif event.key == pygame.K_j:
                    EndMap[col][row] = point.ff(9)()
                elif event.key == pygame.K_k:
                    EndMap[col][row] = point.ff(10)()
                elif event.key == pygame.K_l:
                    EndMap[col][row] = point.ff(11)()
                elif event.key == pygame.K_m:
                    EndMap[col][row] = point.ff(12)()
                elif event.key == pygame.K_n:
                    EndMap[col][row] = point.ff(13)()
                elif event.key == pygame.K_o:
                    EndMap[col][row] = point.ff(14)()
                elif event.key == pygame.K_p:
                    EndMap[col][row] = point.ff(15)()
                elif event.key == pygame.K_q:
                    EndMap[col][row] = point.ff(16)()
                elif event.key == pygame.K_r:
                    EndMap[col][row] = point.ff(17)()
                elif event.key == pygame.K_s:
                    EndMap[col][row] = point.ff(18)()
                elif event.key == pygame.K_t:
                    EndMap[col][row] = point.ff(19)()
                elif event.key == pygame.K_u:
                    EndMap[col][row] = point.ff(20)()
                elif event.key == pygame.K_v:
                    EndMap[col][row] = point.ff(21)()
                elif event.key == pygame.K_RETURN:
                    os.system("cls")
                    with open("SavedMap.txt", "w") as mf:
                        mf.write("[\n")
                        for _ in EndMap:
                            mf.write("[")
                            for _z in range(len(_)):
                                if _z == len(_)-1:
                                    mf.write(f"\"{_[_z]}\"")
                                else:
                                    mf.write(f"\"{_[_z]}\",")
                            mf.write("],\n")
                            print(*_)
                        mf.write("]")
    
    pygame.quit()


if __name__ == "__main__":
    main(SCREEN, WIDTH)