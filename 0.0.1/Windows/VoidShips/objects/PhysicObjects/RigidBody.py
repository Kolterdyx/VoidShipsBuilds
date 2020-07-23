#!/usr/bin/python3.7
from PhysicBody import *
from types import *

def collide_with_walls(sprite, group, dir):
    if dir == "x":
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            # From the left side
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            # From the right side
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == "y":
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            # From bottom
            if hits[0].rect.centery > sprite.hit_rect.y:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height - sprite.hitrect_offset
            # From top
            if hits[0].rect.centery < sprite.hit_rect.y:
                sprite.pos.y = hits[0].rect.bottom - sprite.hitrect_offset
            sprite.vel.y = 0
            sprite.hit_rect.y = sprite.pos.y + sprite.hitrect_offset

class RigidBody(PhysicBody):
    def __init__(self, game, x, y, groups):
        PhysicBody.__init__(self, game, x, y, groups)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.friction = vec(5, 5)

    def apply_force(self, target, force):
        apply_force(target, force)

    def apply_impulse(self, target, impulse):
        apply_impulse(target, impulse)

    def is_on_floor(self):
        pass

    def move(self):
        physics_process(self)
        self.pos += self.vel
        self.vel += self.acc
        self.rect.center = self.pos
        self.tilepos = (int(self.pos.x / TILESIZE), int(self.pos.y / TILESIZE))
        self.chunkpos = (int(self.tilepos[0] / CHUNKSIZE), int(self.tilepos[1] / CHUNKSIZE))
    def move_and_collide():
        pass
