import random
import noise

import pygame as pg

from settings import *
from textures import *
from PhysicObjects import *


class Block(StaticBody):
    def __init__(self, game, x, y, type):
        self.groups = game.all_sprites, game.blocks
        StaticBody.__init__(self, game, x, y, self.groups)
        if type != "void":
            self.image = pg.transform.scale(TERRAIN[type], (TILESIZE, TILESIZE))
        else:
            self.image = pg.transform.scale(TERRAIN["void"], (TILESIZE, TILESIZE))
            game.collidables.add(self)
        # self.cellular_automata()

    def change(self, type):
        self.type = type
        self.image = TERRAIN[type]

    # def cellular_automata(self):
    #     # cellular automata
    #     seed = self.game.worldmanager.get_seed()
    #     oct = 1
    #     floor_void_diff = 0.3
    #
    #     pos = self.tilepos
    #     nb = [
    #         (pos[0]-1, pos[1]-1),    (pos[0], pos[1]-1),    (pos[0]+1, pos[1]-1),
    #
    #         (pos[0]-1, pos[1]),      (pos[0], pos[1]),      (pos[0]+1, pos[1]),
    #
    #         (pos[0]-1, pos[1]+1),    (pos[0], pos[1]+1),    (pos[0]+1, pos[1]+1)
    #     ]
    #     topleft = nb[0]
    #     top = nb[1]
    #     topright = nb[2]
    #     left = nb[3]
    #     right = nb[5]
    #     bottomleft = nb[6]
    #     bottom = nb[7]
    #     bottomright = nb[8]
    #
    #     cpos1 = (int(topleft[0] / CHUNKSIZE), int(topleft[1] / CHUNKSIZE))
    #     cpos2 = (int(top[0] / CHUNKSIZE), int(top[1] / CHUNKSIZE))
    #     cpos3 = (int(topright[0] / CHUNKSIZE), int(topright[1] / CHUNKSIZE))
    #     cpos4 = (int(left[0] / CHUNKSIZE), int(left[1] / CHUNKSIZE))
    #     cpos5 = (int(right[0] / CHUNKSIZE), int(right[1] / CHUNKSIZE))
    #     cpos6 = (int(bottomleft[0] / CHUNKSIZE), int(bottomleft[1] / CHUNKSIZE))
    #     cpos7 = (int(bottom[0] / CHUNKSIZE), int(bottom[1] / CHUNKSIZE))
    #     cpos8 = (int(bottomright[0] / CHUNKSIZE), int(bottomright[1] / CHUNKSIZE))
    #
    #
    #     try:
    #         p1 = self.game.world_data["map"][cpos1]["floor"][topleft] != "void"
    #     except:
    #         p1 = false
    #     try:
    #         p2 = self.game.world_data["map"][cpos2]["floor"][top] != "void"
    #     except:
    #         p2 = false
    #     try:
    #         p3 = self.game.world_data["map"][cpos3]["floor"][topright] != "void"
    #     except:
    #         p3 = false
    #     try:
    #         p4 = self.game.world_data["map"][cpos4]["floor"][left] != "void"
    #     except:
    #         p4 = false
    #     try:
    #         p5 = self.game.world_data["map"][cpos5]["floor"][right] != "void"
    #     except:
    #         p5 = false
    #     try:
    #         p6 = self.game.world_data["map"][cpos6]["floor"][bottomleft] != "void"
    #     except:
    #         p6 = false
    #     try:
    #         p7 = self.game.world_data["map"][cpos7]["floor"][bottom] != "void"
    #     except:
    #         p7 = false
    #     try:
    #         p8 = self.game.world_data["map"][cpos8]["floor"][bottomright] != "void"
    #     except:
    #         p8 = false
    #
    #     neighbourhood = [
    #     [p1, p2, p3],
    #     [p4,  1, p5],
    #     [p6, p7, p8]
    #     ]
    #
    #     # print(p1, p2, p3, p4, p5, p6, p7, p8)
    #
    #     '''
    #     1 2 3
    #     4 - 5
    #     6 7 8
    #     '''
    #
    #     # 1
    #     # ###
    #     # ###
    #     # ###
    #
    #     l1 = [
    #     [1,1,1],
    #     [1,1,1],
    #     [1,1,1]
    #     ]
    #
    #     if l1 == neighbourhood:
    #         tiletype = 1
    #
    #     # 2
    #     # *·* | *·* | ##* | *##
    #     # ##· | ·## | ##· | ·##
    #     # ##* | *## | *·* | *·*
    #
    #     l2 = [
    #     #-----------------------
    #         [
    #         [0,0,0],
    #         [1,1,0],
    #         [1,1,0]
    #         ],
    #         [
    #         [0,0,0],
    #         [0,1,1],
    #         [0,1,1]
    #         ],
    #         [
    #         [1,1,0],
    #         [1,1,0],
    #         [0,0,0]
    #         ],
    #         [
    #         [0,1,1],
    #         [0,1,1],
    #         [0,0,0]
    #         ],
    #     #-----------------------
    #         [
    #         [1,0,1],
    #         [1,1,0],
    #         [1,1,1]
    #         ],
    #         [
    #         [1,0,1],
    #         [0,1,1],
    #         [1,1,1]
    #         ],
    #         [
    #         [1,1,1],
    #         [1,1,0],
    #         [1,0,1]
    #         ],
    #         [
    #         [1,1,1],
    #         [0,1,1],
    #         [1,0,1]
    #         ],
    #     #-----------------------
    #         [
    #         [0,0,1],
    #         [1,1,0],
    #         [1,1,0]
    #         ],
    #         [
    #         [1,0,0],
    #         [0,1,1],
    #         [0,1,1]
    #         ],
    #         [
    #         [1,1,0],
    #         [1,1,0],
    #         [0,0,1]
    #         ],
    #         [
    #         [0,1,1],
    #         [0,1,1],
    #         [1,0,0]
    #         ],
    #     #-----------------------
    #         [
    #         [1,0,0],
    #         [1,1,0],
    #         [1,1,0]
    #         ],
    #         [
    #         [0,0,1],
    #         [0,1,1],
    #         [0,1,1]
    #         ],
    #         [
    #         [1,1,0],
    #         [1,1,0],
    #         [1,0,0]
    #         ],
    #         [
    #         [0,1,1],
    #         [0,1,1],
    #         [0,0,1]
    #         ],
    #     #-----------------------
    #         [
    #         [0,0,0],
    #         [1,1,0],
    #         [1,1,1]
    #         ],
    #         [
    #         [0,0,0],
    #         [0,1,1],
    #         [1,1,1]
    #         ],
    #         [
    #         [1,1,1],
    #         [1,1,0],
    #         [0,0,0]
    #         ],
    #         [
    #         [1,1,1],
    #         [0,1,1],
    #         [0,0,0]
    #         ],
    #     #-----------------------
    #         # [
    #         # [1,0,1],
    #         # [1,1,0],
    #         # [1,1,0]
    #         # ],
    #         # [
    #         # [1,0,1],
    #         # [0,1,1],
    #         # [0,1,1]
    #         # ],
    #         # [
    #         # [1,1,0],
    #         # [1,1,0],
    #         # [1,0,1]
    #         # ],
    #         # [
    #         # [0,1,1],
    #         # [0,1,1],
    #         # [1,0,1]
    #         # ],
    #     #-----------------------
    #         # [
    #         # [0,0,1],
    #         # [1,1,0],
    #         # [1,1,1]
    #         # ],
    #         # [
    #         # [1,0,0],
    #         # [0,1,1],
    #         # [1,1,1]
    #         # ],
    #         # [
    #         # [1,1,1],
    #         # [1,1,0],
    #         # [0,0,1]
    #         # ],
    #         # [
    #         # [1,1,1],
    #         # [0,1,1],
    #         # [1,0,0]
    #         # ],
    #     #-----------------------
    #         # [
    #         # [1,0,0],
    #         # [1,1,0],
    #         # [1,1,1]
    #         # ],
    #         # [
    #         # [0,0,1],
    #         # [0,1,1],
    #         # [1,1,1]
    #         # ],
    #         # [
    #         # [1,1,1],
    #         # [1,1,0],
    #         # [1,0,0]
    #         # ],
    #         # [
    #         # [1,1,1],
    #         # [0,1,1],
    #         # [0,0,1]
    #         # ],
    #     ]
    #
    #     for i, j in enumerate(l2):
    #         if i % 4 == 0:
    #             if j == neighbourhood:
    #                 tiletype = 2
    #                 rotate = 0
    #         if i-1 % 4 == 0:
    #             if j == neighbourhood:
    #                 tiletype = 2
    #                 rotate = 90
    #         if i-2 % 4 == 0:
    #             if j == neighbourhood:
    #                 tiletype = 2
    #                 rotate = -90
    #         if i-3 % 4 == 0:
    #             if j == neighbourhood:
    #                 tiletype = 2
    #                 rotate = 180
    #
    #     # 3
    #     # *·* | ### | ##* | *##
    #     # ### | ### | ##· | ·##
    #     # ### | *·* | ##* | *##
    #     #
    #     # if p4 and p5 and p6 and p7 and p8 and not (p1 or p2 or p3):
    #     #     tiletype = 3
    #     #     rotate = 0
    #     # if p1 and p2 and p3 and p4 and p5 and not (p6 or p7 or p8):
    #     #     tiletype = 3
    #     #     rotate = 180
    #     # if p1 and p2 and p4 and p6 and p7 and not (p3 or p5 or p8):
    #     #     tiletype = 3
    #     #     rotate = -90
    #     # if p2 and p3 and p5 and p7 and p8 and not (p1 or p4 or p6):
    #     #     tiletype = 3
    #     #     rotate = -270
    #     """
    #     # -------------------------------------------------------------------------------
    #
    #
    #     # 4
    #     # ··· | ·#· | ··· | ···
    #     # ·#· | ·#· | ·## | ##·
    #     # ·#· | ··· | ··· | ···
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 5
    #     # ·#· | ···
    #     # ·#· | ###
    #     # ·#· | ···
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 6
    #     # ·#·
    #     # ###
    #     # ·#·
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 7
    #     # ##· | ·##
    #     # ### | ###
    #     # ·## | ##·
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 8
    #     # ·#· | ·#· | ·## | ##·
    #     # ### | ### | ### | ###
    #     # # · | ·## | ·#· | ·#·
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 9
    #     # ##· | ### | ### | ·##
    #     # ### | ### | ### | ###
    #     # ### | ##· | ·## | ###
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #     # 10
    #     # ·#· | ##· | ### | ·##
    #     # ### | ### | ### | ###
    #     # ### | ##· | ·#· | ·##
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 11
    #     # ··· | ·#· | ··· | ·#·
    #     # ##· | ##· | ·## | ·##
    #     # ·#· | ··· | ·#· | ···
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #     # 12
    #     # ··· | ·#· | ·#· | ·#·
    #     # ·#· | ·## | ### | ##·
    #     # ·#· | ·#· | ··· | ·#·
    #
    #
    #     if p4 and p6 and p7 and not (p1 or p2 or p3 or p4 or p8):
    #         tiletype = 2
    #         rotate = 0
    #     if p1 and p2 and p4 and not (p3 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = -90
    #     if p2 and p3 and p4 and not (p1 or p5 or p6 or p7 or p8):
    #         tiletype = 2
    #         rotate = 180
    #     if p5 and p7 and p8 and not (p1 or p2 or p3 or p4 or p6):
    #         tiletype = 2
    #         rotate = 90
    #
    #
    #
    #
    #
    #     # 13
    #     # ···
    #     # ·#·
    #     # ···
    #
    #
    #     if not p1 and not p2 and not p3 and not p4 and not p5 and not p6 and not p7 and not p8:
    #         tiletype = 13
    #         """
    #
    #     try:
    #         self.image = pg.transform.rotate(pg.transform.scale(
    #             TERRAIN_v2["grass"][tiletype], (TILESIZE, TILESIZE)), rotate)
    #     except:
    #         pass
