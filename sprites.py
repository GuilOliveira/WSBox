import pygame as pg
from settings import *
import random

class Square_aim():
    def __init__(self):
        self.width, self.height = BLOCKSIZE, BLOCKSIZE

    def centralize(self, number):
        number -= self.width / 2
        return int(number)

    def add_size(self):
        if self.width <= 400:
            self.width += BLOCKSIZE
            self.height += BLOCKSIZE

    def rmv_size(self):
        if self.width >= BLOCKSIZE*2:
            self.width -= BLOCKSIZE
            self.height -= BLOCKSIZE

class block_picker():
    def __init__(self):
        self.set_stone()

    def set_stone(self):
        self.state = "stone"
        self.value = 4
        self.color = STONE_COLOR

    def set_water(self):
        self.state = "water"
        self.value = 0
        self.color = WATER_COLOR

    def set_sand(self):
        self.state = "sand"
        self.value = 1
        self.color = SAND_COLOR

    def get_state(self):
        return self.state

    def get_color(self):
        return self.color

    def get_aim(self):
        return [self.color[0]-35, self.color[1]-35, self.color[2]-35]

class Stone(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.Surface((BLOCKSIZE, BLOCKSIZE))
        self.image.fill(STONE_COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * BLOCKSIZE
        self.rect.y = y * BLOCKSIZE

    def die(self):
        self.kill()



class Sand(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.Surface((BLOCKSIZE, BLOCKSIZE))
        self.image.fill(SAND_COLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * BLOCKSIZE
        self.rect.y = y * BLOCKSIZE
    def update(self):
        if block_list[self.x][self.y+1]=="air":
            self.fall()

        elif block_list[self.x-1][self.y+1]=="air" and block_list[self.x-1][self.y]=="air":
            self.fall_left()
        elif block_list[self.x+1][self.y+1]=="air" and block_list[self.x+1][self.y]=="air":
            self.fall_right()

        if self.rect.y >= SCREEN_H:
            self.kill()
    def fall(self):
        block_list[self.x][self.y] = "air"
        block_list[self.x][self.y + 1] = "sand"
        self.rect.y += BLOCKSIZE
        self.y += 1
    def fall_left(self):
        block_list[self.x][self.y] = "air"
        block_list[self.x - 1][self.y + 1] = "sand"
        self.rect.y += BLOCKSIZE
        self.rect.x -= BLOCKSIZE
        self.y += 1
        self.x -= 1
    def fall_right(self):
        block_list[self.x][self.y] = "air"
        block_list[self.x + 1][self.y + 1] = "sand"
        self.rect.y += BLOCKSIZE
        self.rect.x += BLOCKSIZE
        self.y += 1
        self.x += 1
    def die(self):
        self.kill()
