import pygame


class Triangle(pygame.sprite.Sprite):

    def __init__(self, width=32, height=32, x=0, y=0):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Triangle.png")
        self.image = pygame.transform.scale(self.image, (width, height))

        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def rotate(self, screen, deg):

        pos = (self.rect.x, self.rect.y)

        width, height = self.width, self.height
        box = [pygame.math.Vector2(p) for p in [(
            0, 0), (width, 0), (width, -height), (0, -height)]]

        box_rotate = [p.rotate(deg) for p in box]

        min_box = [min(box_rotate, key=lambda p: p[0])[0],
                   min(box_rotate, key=lambda p: p[1])[1]]

        max_box = [max(box_rotate, key=lambda p: p[0])[0],
                   max(box_rotate, key=lambda p: p[1])[1]]

        pivot = pygame.math.Vector2(width / 2, -height)
        pivot_rotate = pivot.rotate(deg)
        pivot_move = pivot_rotate - pivot

        origin = (pos[0] + min_box[0] - pivot_move[0],
                  pos[1] - max_box[1] + pivot_move[1])

        rotated_image = pygame.transform.rotate(self.image, deg)
        screen.blit(rotated_image, origin)
