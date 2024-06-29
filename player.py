import pygame
from pygame import *

from block import Block
from camera import Camera
from globals import *

class Player:
    PLAYER_VEL = 7
    PLAYER_SIZE = BLOCK_SIZE
    GRAVITY = 0.5
    MAX_ACCELERATION = 13

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.acceleration = -self.MAX_ACCELERATION
        self.isJumping = True

    def move(self, blocks: list[Block], camera: Camera):
        keys = pygame.key.get_pressed()
        direction = 0

        if keys[K_LEFT]:
            self.x -= self.PLAYER_VEL
            direction = -1
        elif keys[K_RIGHT]:
            self.x += self.PLAYER_VEL
            direction = 1

        for block in blocks:
            if (pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE).colliderect(block.rect)):
                if (direction == -1):
                    self.x = block.x+block.BLOCK_SIZE
                else:
                    self.x = block.x-self.PLAYER_SIZE

        if (keys[K_SPACE] or keys[K_UP]) and not self.isJumping:
            self.isJumping = True
            self.acceleration = -self.MAX_ACCELERATION

        self.acceleration += self.GRAVITY
        if self.acceleration > self.MAX_ACCELERATION:
            self.acceleration = self.MAX_ACCELERATION
        self.y += self.acceleration

        for block in blocks:
            if (pygame.Rect(self.x, self.y, self.PLAYER_SIZE, self.PLAYER_SIZE).colliderect(block.rect)):
                if (self.acceleration > 0):
                    self.y = block.y - self.PLAYER_SIZE
                    self.isJumping = False
                else:
                    self.y = block.y + Block.BLOCK_SIZE
                    self.acceleration = 0
                break

        if self.x - camera.x < Camera.CAMERA_LEFT_EDGE*BLOCK_SIZE:
            camera.x -= Camera.CAMERA_LEFT_EDGE*BLOCK_SIZE - (self.x - camera.x)
            if camera.x < 0:
                camera.x = 0
        elif self.x - camera.x > Camera.CAMERA_RIGHT_EDGE*BLOCK_SIZE:
            camera.x += (self.x - camera.x) - camera.CAMERA_RIGHT_EDGE*BLOCK_SIZE
            if camera.x > (Camera.world_width - Camera.CAMERA_WIDTH)*BLOCK_SIZE:
                camera.x = (Camera.world_width - Camera.CAMERA_WIDTH)*BLOCK_SIZE

        if self.y - camera.y < Camera.CAMERA_TOP_EDGE*BLOCK_SIZE:
            camera.y -= Camera.CAMERA_TOP_EDGE*BLOCK_SIZE - (self.y - camera.y)
            if camera.y < 0:
                camera.y = 0
        elif self.y - camera.y > Camera.CAMERA_BOTTOM_EDGE*BLOCK_SIZE:
            camera.y += (self.y - camera.y) - camera.CAMERA_BOTTOM_EDGE*BLOCK_SIZE
            if camera.y > (Camera.world_height - Camera.CAMERA_HEIGHT)*BLOCK_SIZE:
                camera.y = (Camera.world_height - Camera.CAMERA_HEIGHT)*BLOCK_SIZE

    def draw(self, surface, camera: Camera):
        pygame.draw.rect(surface, (255, 0, 0), (self.x - camera.x, self.y - camera.y, self.PLAYER_SIZE, self.PLAYER_SIZE))