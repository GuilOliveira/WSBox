BLOCKSIZE = 8
SCREEN_W, SCREEN_H = 800, 800
GRID_W, GRID_H = SCREEN_W/BLOCKSIZE, SCREEN_H/BLOCKSIZE

block_list = []
for x in range (0,int(GRID_W+30)):
    block_list.append([])
    for y in range (0,int(GRID_H+30)):
        block_list[x].append("air")

#colors
STONE_COLOR = [130, 130, 130]
WATER_COLOR = [39, 122, 230]
SAND_COLOR = [209, 195, 65]