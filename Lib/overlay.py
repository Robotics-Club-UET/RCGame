import pygame
from Setting import *

class Overlay:
    def __init__(self,player):
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        #imports
        self.tools_surf = {}