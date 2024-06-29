import pygame

class Camera:
    CAMERA_WIDTH = 20
    CAMERA_HEIGHT = 15

    world_width = 40
    world_height = 15

    CAMERA_LEFT_EDGE = 5
    CAMERA_RIGHT_EDGE = 10
    CAMERA_TOP_EDGE = 1
    CAMERA_BOTTOM_EDGE = 13

    def __init__(self, level_image: str, level: list[list[int]]) -> None:
        self.x = 0
        self.y = 0

        level.clear()

        level_data = pygame.image.load(level_image)

        Camera.world_width = level_data.get_width()
        Camera.world_height = level_data.get_height()

        for h in range(self.world_height):
            level.append([])
            for w in range(self.world_width):
                block = 0
                if (level_data.get_at((w, h)) == (0, 0, 0)):
                    block = 1
                level[h].append(block)