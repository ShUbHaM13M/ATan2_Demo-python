import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height, angle):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.angle = angle
