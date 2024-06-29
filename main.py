import pygame
from pygame import *

from block import *
from player import *
from camera import *
from globals import *

if __name__=="__main__":

    pygame.display.set_mode((Block.BLOCK_SIZE*Camera.CAMERA_WIDTH, Block.BLOCK_SIZE*Camera.CAMERA_HEIGHT))

    level = []
    camera = Camera("level.png", level)
    print(len(level))
    print(len(level[0]))

    player = Player(400, 300)

    blocks = []

    for h in range(len(level)):
        for w in range(len(level[h])):
            if (level[h][w] == 1):
                blocks.append(Block(Block.BLOCK_SIZE*w, Block.BLOCK_SIZE*h))

    clock = pygame.time.Clock()

    run = True;
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False;
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False;
        
        player.move(blocks, camera)

        pygame.display.get_surface().fill((255, 255, 255))

        for block in blocks:
            block.draw(pygame.display.get_surface(), camera);
        
        player.draw(pygame.display.get_surface(), camera)


        pygame.display.flip()

        clock.tick(60)

    pygame.quit();