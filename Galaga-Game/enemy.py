import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 470, self.image.get_height() - 360))
        self.is_destroyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - 30)
        self.rect.y = -self.rect.height
        self.hp = 3
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()


    def destroy(self):
        self.kill()