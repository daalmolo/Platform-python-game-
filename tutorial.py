import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

HEIGHT, WIDTH = 768, 960
FPS = 60
# PLAYER_VEL = 5

game_window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))

    x, y, img_width, img_height = image.get_rect()
    tiles = []

    for i in range(WIDTH // img_width):
        for j in range(HEIGHT // img_height):
            pos = (i * img_width, j * img_height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_img):
    for tile in background:
        window.blit(bg_img, tile)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_img = get_background("Gray.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_img)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(game_window)
