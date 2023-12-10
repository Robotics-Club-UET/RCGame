from os import walk
import pygame
class assassin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = import_folder("robot_assassin")

    def update(self):
        self.frame_index += 1
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]
    
def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            TILE = 50
            image_surf = pygame.transform.scale(image_surf, (TILE - TILE * 0.3, TILE - TILE * 0.3))
            surface_list.append(image_surf)

    return surface_list
