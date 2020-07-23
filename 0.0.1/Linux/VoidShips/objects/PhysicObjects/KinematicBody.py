from PhysicBody import *

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

class KinematicBody(PhysicBody):
    def __init__(self, game, x, y, groups):
        PhysicBody.__init__(self, game, x, y, groups)
        self.vel = vec(0, 0)

    def move_and_collide(self, velocity):

        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += velocity * self.game.delta

        # Move the player and collide if necesary
        self.hit_rect.centerx = self.pos.x
        #collide_with_walls(self, self.game.collidables, "x")
        self.hit_rect.y = self.pos.y + self.hitrect_offset
        #collide_with_walls(self, self.game.collidables, "y")

        # Move the player's rect with its position
        self.rect.center = self.pos

        # Find the position measured in tiles or chunks of the player
        self.tilepos = vec(int(self.pos.x / TILESIZE), int(self.pos.y / TILESIZE))
        self.chunkpos = vec(int(self.tilepos.x / CHUNKSIZE), int(self.tilepos.y / CHUNKSIZE))

        if self.pos.x < XLIMIT:
            print("You have reached the edge of the world!")
            self.pos.x = XLIMIT
        if self.pos.y < YLIMIT:
            print("You have reached the edge of the world!")
            self.pos.y = YLIMIT
