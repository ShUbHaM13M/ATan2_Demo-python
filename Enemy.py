import pygame
import random


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.randint(2, 4)


    def move(self):
        self.y += self.speed


    def render(self, window):
        window.blit(self.image, (self.x, self.y))
    