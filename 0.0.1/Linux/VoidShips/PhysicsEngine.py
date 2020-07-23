#!/usr/bin/python3.7
import pygame as pg
from pygame import *
import random
from types import *

vec = pg.math.Vector2
vec3 = pg.math.Vector3

default_friction = 5

#Get force: force = weight * acc
#Get acc: acc = force/weight
#Get weight: weight = force/acc

def physics_process(target) -> vec:
    if target.applied_force.length() > vec(0,0).length():
        target.applied_force -= target.friction
    else:
        force = vec(0,0)
    if target.applied_impulse.length() > vec(0,0).length():
        target.applied_impulse -= target.friction
    else:
        force = vec(0,0)

    target.acc = target.applied_force
    target.vel = target.applied_impulse
    print(target)

def calculate(target, force: vec=vec(0,0), weight: int=1000,friction: vec=vec(0,0)) -> vec:
    result = (force - friction) / weight
    return result


def apply_force(target, force: vec):
    target.applied_force += calculate(target, force, 1000, target.friction)

def apply_impulse(target, impulse: vec=vec(0,0)):
    target.applied_impulse += calculate(target, impulse, 1000, target.friction)
