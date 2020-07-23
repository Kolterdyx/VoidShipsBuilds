#!/usr/bin/python3.7
import pygame as pg
from settings import *
from textures import *
from PhysicBody import *
from types import *

class StaticBody(PhysicBody):
    def __init__(self, game, x, y, groups):
        PhysicBody.__init__(self, game, x, y, groups)
