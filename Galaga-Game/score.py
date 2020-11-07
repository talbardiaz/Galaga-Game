import pygame
import constants as c


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.font_size = 32
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)

        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - 135
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 8.3


    def update(self):
        pass


    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - 135
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 8.3