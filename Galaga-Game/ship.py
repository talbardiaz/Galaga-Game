import pygame
import constants as c
from bullet import Bullet
from  hud import HUD



class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()-1050, self.image.get_height()-1050))
        self.rect = self.image.get_rect()
        self.rect.x = 173
        self.rect.y = 540
        self.bullets = pygame.sprite.Group()
        self.max_hp = 10
        self.hp = self.max_hp
        self.hud = HUD(self.hp)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.hp = 10
        self.lives = 1
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 8

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= -45:
            self.rect.x = -45
        elif self.rect.x >= c.DISPLAY_WIDTH - 101:
            self.rect.x = c.DISPLAY_WIDTH - 101
        self.rect.y += self.vel_y


    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + 72
        new_bullet.rect.y = self.rect.y + 52
        self.bullets.add(new_bullet)


    def get_hit(self):
        self.hp -= 1
        self.hud.health_bar.decrease_hp_value()
        if self.hp <= 0:
            self.hp = 0
            self.death()

    def death(self):
        self.lives = 0
        if self.lives <= 0:
            self.lives = 0

