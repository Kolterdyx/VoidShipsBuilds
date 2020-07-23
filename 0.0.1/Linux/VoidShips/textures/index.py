import sys
import os
import pygame as pg

PLAYER_IMG = pg.image.load("textures/player/player.png")

TERRAIN = {
    "void": pg.image.load("textures/void/void0000.png"),
    "grass": pg.image.load("textures/terrain/grass.png"),
    "rock": pg.image.load("textures/terrain/rock.png"),
    "mountain": pg.image.load("textures/terrain/mountain.png")
}
TERRAIN_v2 = {
    "grass": ["",
              pg.image.load("textures/terrain/suelo/suelo_00.png"),
              pg.image.load("textures/terrain/suelo/suelo_01.png"),
              pg.image.load("textures/terrain/suelo/suelo_02.png"),
              pg.image.load("textures/terrain/suelo/suelo_03.png"),
              pg.image.load("textures/terrain/suelo/suelo_04.png"),
              pg.image.load("textures/terrain/suelo/suelo_05.png"),
              pg.image.load("textures/terrain/suelo/suelo_06.png"),
              pg.image.load("textures/terrain/suelo/suelo_07.png"),
              pg.image.load("textures/terrain/suelo/suelo_08.png"),
              pg.image.load("textures/terrain/suelo/suelo_09.png"),
              pg.image.load("textures/terrain/suelo/suelo_10.png"),
              pg.image.load("textures/terrain/suelo/suelo_11.png"),
              pg.image.load("textures/terrain/suelo/suelo_12.png")
              ]
}

ITEMS = {
"empty": pg.image.load("textures/items/empty_invisible.png"),
"branch": pg.image.load("textures/items/branch.png"),
"stick": pg.image.load("textures/items/stick.png"),
"major_branch": pg.image.load("textures/items/major_branch.png"),
"log": pg.image.load("textures/items/log.png"),
"rock": pg.image.load("textures/items/rock.png"),
"stone": pg.image.load("textures/items/stone.png"),
"flint": pg.image.load("textures/items/flint.png")
}

UI = {
    "pinv": pg.image.load("textures/UI/Inventory/inventory.png"),
    "HUD": {
        "hotbar": pg.image.load("textures/UI/HUD/hotbar.png"),
        "hb_pointer": pg.image.load("textures/UI/HUD/hb_pointer.png")
    }
}
