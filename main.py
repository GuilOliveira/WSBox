import pygame as pg
import sprites
from settings import *

pg.init()

display = pg.display.set_mode((SCREEN_W, SCREEN_H))
captions = "WSBox"
clock = pg.time.Clock()
global block_list


blockGroup = pg.sprite.Group()
aim = sprites.Square_aim()
picker = sprites.block_picker()


def draw():
    display.fill([50, 50, 50])


def normalize_blocks(num, size, grid_pos):
    return int((num - size / 2) / BLOCKSIZE + 0.5) + grid_pos


def create_blocks(pos, size, state):
    global block_list
    for x in range(0, int(size / BLOCKSIZE)):
        for y in range(0, int(size / BLOCKSIZE)):
            if block_list[normalize_blocks(pos[0], size, x)][ normalize_blocks(pos[1], size, y)] == "air":
                if state == "stone":
                    sprites.Stone(normalize_blocks(pos[0], size, x), normalize_blocks(pos[1], size, y), blockGroup)
                    block_list[normalize_blocks(pos[0], size, x)][normalize_blocks(pos[1], size, y)] = "stone"
                if state=="sand":
                    sprites.Sand(normalize_blocks(pos[0], size, x), normalize_blocks(pos[1], size, y), blockGroup)
                    block_list[normalize_blocks(pos[0], size, x)][normalize_blocks(pos[1], size, y)] = "sand"
                if state=="water":
                    sprites.Stone(normalize_blocks(pos[0], size, x), normalize_blocks(pos[1], size, y), blockGroup)
                    block_list[normalize_blocks(pos[0], size, x)][normalize_blocks(pos[1], size, y)] = "water"


def delete_blocks(pos, size):
    global block_list
    for x in range(0, int(size / BLOCKSIZE)):
        for y in range(0, int(size / BLOCKSIZE)):
            if block_list[normalize_blocks(pos[0], size, x)][ normalize_blocks(pos[1], size, y)] != "air":
                for obj in blockGroup:
                    if obj.x == normalize_blocks(pos[0], size, x) and obj.y == normalize_blocks(pos[1], size, y):
                        obj.kill()
                block_list[normalize_blocks(pos[0], size, x)][normalize_blocks(pos[1], size, y)] = "air"



gameloop = True
while gameloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameloop = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                picker.set_stone()
                print("a")
            elif event.key == pg.K_2:
                picker.set_sand()
            elif event.key == pg.K_3:
                picker.set_water()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                aim.add_size()
            elif event.button == 5:
                aim.rmv_size()
    time = clock.tick(90)

    if pg.mouse.get_pressed() == (1, 0, 0):
        create_blocks(pg.mouse.get_pos(), aim.width, picker.get_state())
    if pg.mouse.get_pressed() == (0, 0, 1):
        delete_blocks(pg.mouse.get_pos(), aim.width)

    draw()
    blockGroup.update()
    blockGroup.draw(display)
    pg.draw.rect(display, picker.get_aim(),
                 (aim.centralize(pg.mouse.get_pos()[0]), aim.centralize(pg.mouse.get_pos()[1]), aim.width, aim.width), 2)
    pg.display.flip()
