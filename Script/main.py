import os, sys

sys.path.append('..\Lib')

import pygame
from Level import *
from Setting import *
import sys
from  miniChallenge import *
from miniChallenge3 import invertedPendulum


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Sprout land')
        self.clock = pygame.time.Clock()
        self.level = Level()
        # self.dialogue_box = DialogueBox()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Kiểm tra xem có phải là nút trái chuột không
                        print("Left mouse button clicked at:", event.pos)

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            if self.level.dialogue_box.challenge == "XiemHoang":
                game_maze()
                self.level.dialogue_box.challenge = None
            if self.level.dialogue_box.challenge == "ThanhVan":
                invertedPendulum()
                self.level.dialogue_box.challenge = None
            if self.level.dialogue_box.challenge == "DuyHung":
                sys.path.append('..\Lib\miniChallenge_2')
                from maingame import miniChallenge2
                miniChallenge2()
                self.level.dialogue_box.challenge = None
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
