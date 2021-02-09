import pygame
import sys
import os
import math
import numpy
import threading
import random
import time

from triangle import Triangle
from Bullet import Bullet
from Enemy import Enemy

pygame.init()

CYAN = (0, 255, 255)
RED = (255, 0, 0)

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ATan2 demo")
start_time = time.time()

clock = pygame.time.Clock()

block = Triangle(64, 64, screen_width //
                 2 - 32, screen_height - 150)


bulletGroup = pygame.sprite.Group()
enemies = []

def spawnEnemies():

    while True:
        temp = Enemy(random.randint(40, 600), 0, RED, 20, 20)
        enemies.append(temp)
        time.sleep(1)


spawn_thread = threading.Thread(target=spawnEnemies, daemon=True)
spawn_thread.start()


def main():
    
    angle = 0
    bullet_list = []

    is_running = True
    while is_running:
        screen.fill((0, 0, 0))
        muzzlePoint = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                block_pos = (block.rect.x, block.rect.y)
                look_dir = tuple(numpy.subtract(block_pos, mouse_pos))

                angle = -(math.atan2(look_dir[1], look_dir[0]) - 90)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet_angle = (math.sin(angle), math.cos(angle))
                temp_bullet = Bullet(
                        block.rect.x + block.rect.width // 2 - 10,
                        block.rect.y + 10,
                        CYAN,
                        10,
                        10,
                        bullet_angle)
                bullet_list.append(temp_bullet)
                bulletGroup.add(temp_bullet)

        for bullet in bullet_list:
            speed = 10
            bullet.y -= speed * 2 * bullet.angle[1]
            bullet.x -= speed * 2 * bullet.angle[0]

        for bullet in bullet_list:
            if bullet.y < 0:
                bullet_list.remove(bullet)
                destroy_bullet(bullet)
            

        for bullet in bullet_list:
            screen.blit(bullet.image, (bullet.x, bullet.y))

        # for enemy in enemies:
        #     enemy.move()
        #     enemy.render(screen)

        check_collision()

        block.rotate(screen, math.degrees(angle))

        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)


def check_collision():
    for enemy in enemies:
        if (enemy.y + enemy.height) >= screen_height:
            destroy_enemy(enemy)
        if pygame.sprite.spritecollide(enemy, bulletGroup, 0):
            destroy_enemy(enemy)

def destroy_enemy(obj):
    enemies.remove(obj)
    del (obj)

def destroy_bullet(obj):
    bulletGroup.remove(obj)
    del(obj)


main()
pygame.quit()
sys.exit()
