import pygame
from Setting import *
from support import *
from Timer import Timer


class Npc(pygame.sprite.Sprite):
    def __init__(self, group,NpcName):
        super().__init__(group)
        self.frame_index = 0

        # general setup
        self.NpcName = NpcName
        self.image = pygame.image.load("../Graphics/NPC/XH.gif")
        self.image = pygame.transform.scale(self.image, (45, 45))

        self.rect = self.image.get_rect(center=NPC_Position[self.NpcName])
        self.z = LAYERS['main']
    def animate(self, dt):
        self.frame_index += 4 * dt
        self.animations = import_folder('../Graphics/NPC/' + self.NpcName)
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (50, 50))
    def update(self, dt):
        self.animate(dt)