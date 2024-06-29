import pygame

from camera import Camera
from globals import *

class Block:
    BLOCK_SIZE = BLOCK_SIZE

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE)

    def draw(self, surface, camera : Camera):
        pygame.draw.rect(surface, (0, 0, 0), (self.x - camera.x, self.y - camera.y, self.BLOCK_SIZE, self.BLOCK_SIZE))