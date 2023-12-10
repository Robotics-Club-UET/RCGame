import pygame
from Setting import *
from Player import *
from Sprites import Generic
from NPC import *
from ConversationBox import *
from ConversationContent import *
import time


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()

        self.setup()

        # music
        self.music = pygame.mixer.Sound("../Audio/BackgroudMusic.mp3")
        self.music.set_volume(0.4)
        self.music.play(loops=-1)

        self.dialogue_box = DialogueBox()
        self.dialogue_box.show_dialogue = False




    def setup(self):
        self.player = Player((640, 360), self.all_sprites)  # Player

        self.NPC_DH = Npc(self.all_sprites, NpcName="Dam")  # NPC no.1
        self.NPC_TV = Npc(self.all_sprites, NpcName="Junie")  # NPC no.2
        self.NPC_XH = Npc(self.all_sprites, NpcName="Jon")  # NPC no.3

        # self.conversation_test = DialogueBox(self.all_sprites,NpcContent=XH_Content)

        Generic(pos=(0, 0), surf=pygame.image.load('../Graphics/World/map.png').convert_alpha(),
                groups=self.all_sprites,
                z=LAYERS['ground'])

    def conversation(self):
        if self.player.conversation != None:
            self.dialogue_box.content = self.player.conversation
            # print(self.dialogue_box.content,"_____")
            self.dialogue_box.show_dialogue = True
            self.dialogue_box.clear_data(self.player.conversation)
            self.player.conversation = None
        if self.dialogue_box.show_dialogue:
            self.dialogue_box.display(self.display_surface)
        else:
            self.player.control = True


    def run(self, dt):
        self.display_surface.fill('black')

        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        # self.all_sprites.custom_draw(self.NPC_XH)
        self.all_sprites.update(dt)
        self.conversation()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    # offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
