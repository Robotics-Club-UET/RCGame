from Setting import *
import pygame
from ConversationContent import *
import time


class DialogueBox(pygame.sprite.Sprite):
    def __init__(self, NpcContent="Jon", group=None):
        super().__init__()

        # General setup
        self.width = DIALOGUE_WIDTH
        self.height = DIALOGUE_HEIGHT
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (DIALOGUE_CENTER_X-20, DIALOGUE_CENTER_Y)
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        self.dialogue_image = pygame.image.load(DIALOGUE)
        self.dialogue_image = pygame.transform.scale(self.dialogue_image, (self.width, self.height+15))
        self.text = ""
        self.options = []
        self.selected_option = -1
        self.text_speed = 35
        self.text_index = 0
        self.show_dialogue = True
        self.z = LAYERS['main']

        # Content setup
        self.select_options = True
        self.content = Content
        self.NpcContent = NpcContent
        self.conversation_content = Content[NpcContent]
        self.set_text(content=self.conversation_content['Start'][0])
        self.list_options = list(self.conversation_content.keys())
        self.chat_index = 0

        self.challenge = None

    def set_text(self, content):
        self.text = content
        self.lines = self.cut_line()
        self.text_index = [0] * len(self.lines)
        self.line_index = 0

        # Option ??
        self.options = self.conversation_content['Option'].values()

    def set_font(self, font_name, font_size):
        self.font = pygame.font.Font(font_name, font_size)

    def set_position(self, x, y):
        self.rect.topleft = (x, y)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.rect.x, self.rect.y)

    def cut_line(self):
        lines = []
        current_line = ""
        words = self.text.split()
        for word in words:
            test_line = current_line + word + " "
            test_text = self.font.render(test_line, True, (0, 0, 0))
            if test_text.get_width() <= self.width - 20:  # Đảm bảo không vượt quá chiều rộng của khung thoại
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        if current_line:
            lines.append(current_line)
        return lines

    def draw_text(self, screen):
        if self.select_options:
            current_text = self.text
            text_render = self.font.render(current_text, True, (0, 0, 0))
            screen.blit(text_render, (self.rect.x + 30, self.rect.y + 10))
        else:
            if self.text_index[self.line_index] < len(self.lines[self.line_index]):
                self.text_index[self.line_index] += 1
            else:
                if self.line_index < len(self.lines) - 1:
                    self.line_index += 1
            text_y = self.rect.y
            for index in range(len(self.lines)):
                current_text = self.lines[index][:self.text_index[index]]
                text_render = self.font.render(current_text, True, (0, 0, 0))
                screen.blit(text_render, (self.rect.x + 30, text_y + 10))
                text_y += text_render.get_height()
            time.sleep(1 / self.text_speed)

    def draw_options(self, screen):
        option_y = self.rect.y + 35
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                option_text = "> " + option
                option_render = self.font.render(option_text, True,
                                                 (255, 0, 0))  # Đổi màu chữ của dòng đang được chọn thành đỏ
            else:
                option_text = "  " + option
                option_render = self.font.render(option_text, True, (0, 0, 0))
            screen.blit(option_render, (self.rect.x + 30, option_y))
            option_y += 23

    def select_option(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.select_options:
                self.chat_index = 0
                self.set_text(self.conversation_content[self.list_options[self.selected_option + 1]][self.chat_index])
                self.select_options = False
            else:
                if self.chat_index < len(self.conversation_content[self.list_options[self.selected_option + 1]]) - 1:
                    self.chat_index += 1
                    self.set_text(
                        self.conversation_content[self.list_options[self.selected_option + 1]][self.chat_index])
                else:
                    if self.list_options[self.selected_option + 1] == "End":
                        self.show_dialogue = False
                    elif self.list_options[self.selected_option + 1] == "ChallengeforMe":
                        self.challenge = self.NpcContent
                        self.show_dialogue = False
                    self.select_options = True
            time.sleep(0.08)
        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
            time.sleep(0.08)
        if keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)
            time.sleep(0.08)

    def clear_data(self, NpcContent):
        self.selected_option = -1
        self.conversation_content = Content[NpcContent]
        self.set_text(content=self.conversation_content['Start'][0])
        self.list_options = list(self.conversation_content.keys())
        self.NpcContent = NpcContent

    def update(self):
        pass

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        screen.blit(self.dialogue_image, self.rect.topleft)  # Vẽ ảnh lên khung thoại
        self.draw_text(screen)
        if self.select_options:
            self.draw_options(screen)
        self.select_option()
