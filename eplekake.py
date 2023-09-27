
import pygame as pg

pg.init()

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

pos_x = 100
pos_y = 100

size_x = 50
size_y = 50

screen = pg.display.set_mode((600, 400))

clock = pg.time.Clock()

i = 0
playing = True

while playing:
    clock.tick(120)
    print("FPS:", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos_y -= 5
    if keys[pg.K_a]:
        pos_x -= 5
    if keys[pg.K_s]:
        pos_y += 5
    if keys[pg.K_d]:
        pos_x += 5

    if pos_x > 600-size_x:
        pos_x = 600-size_x
    if pos_x < 0:
        pos_x = 0
    if pos_y > 400-size_y:
        pos_y = 400-size_y
    if pos_y < 0:
        pos_y = 0
    

    screen.fill(BLACK)
    player_box = pg.Rect(pos_x,pos_y,size_x,size_y)

    pg.draw.rect(screen, YELLOW, player_box,)

    pg.display.update()