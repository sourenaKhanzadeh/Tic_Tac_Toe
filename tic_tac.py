import pygame as pg
from pygame.locals import *

#board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
#display
def display(l):
    for row in l:
        print(row)


#play game
def play():
    pass
#handle turn
def handle_turn():
    pass

def check(l):
    pass
#check win
    #check row
    #check col
    #check diagnol
#check tie
def flip():
    pass

#flip player
color = {
    'white':(0xff, 0xff, 0xff),
    'black':(0, 0, 0)

}
class Settings:

    def __init__(self):
        self.screen_h = 600
        self.screen_w = 600
        self.title = "Tic Tac Toe"
        self.scene = []

        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        pg.display.set_caption(self.title)


class Board(Settings):

    def __init__(self, r, c):
        super().__init__()
        self.r = r
        self.c = c
        self.offset = 200
        self.img = pg.image.load('./res/xxx.png').convert_alpha()
        self.board  = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.team = True

    def draw(self):
        block_size = 100
        for y in range(self.r):
            for x in range(self.c):
                if self.board[y][x] == 1:
                    self.img = pg.image.load('./res/xxx.png').convert_alpha()
                    self.img = pg.transform.scale(self.img, (block_size, block_size))
                    self.screen.blit(self.img, (x*block_size, y*block_size))
                elif self.board[y][x] == 2:
                    self.img = pg.image.load('./res/ooo.jpg').convert_alpha()
                    self.img = pg.transform.scale(self.img, (block_size, block_size))
                    self.screen.blit(self.img, (x*block_size, y*block_size))

                rect = pg.Rect(x*block_size, y*block_size, block_size, block_size)
                pg.draw.rect(self.screen, color['black'], rect, 1)
        mouse_pos = pg.mouse.get_pos()
        mouse = pg.mouse.get_pressed()[0]
        if mouse:
            if self.team:
                self.board[mouse_pos[1]//block_size][mouse_pos[0]//block_size] = 1
                self.team = False
            else:
                self.board[mouse_pos[1]//block_size][mouse_pos[0]//block_size] = 2
                self.team = True
            print(self.board)

    def update(self):
        self.draw()


class Game(Settings):

    def __init__(self):
        super().__init__()
        self.awake()
        self.run()

    def awake(self):
        self.scene.append(Board(3, 3))

    def run(self):
        run = True
        while run:
            pg.time.delay(150)
            for ev in pg.event.get():
                if ev.type == QUIT:
                    run = False
            self.update()

    def update(self):
            self.screen.fill(color['white'])
            for gameObejct in self.scene:
                gameObejct.update()
            pg.display.update()

if __name__ == "__main__":
    Game()
