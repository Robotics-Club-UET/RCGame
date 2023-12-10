import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trò Chơi Của Tôi")

# Kích thước cửa sổ thoại
dialogue_width, dialogue_height = 400, 200
dialogue_surface = pygame.Surface((dialogue_width, dialogue_height))
background_image = pygame.image.load('../Graphics/Dialog/Dialogue.png')
dialogue_surface.blit(background_image, (0, 0))

font = pygame.font.Font(None, 24)
text = font.render("Chào bạn! Đây là cuộc hội thoại.", True, (0, 0, 0))  # Văn bản màu đen

# Vị trí của cửa sổ thoại
dialogue_x = (screen_width - dialogue_width) // 2
dialogue_y = (screen_height - dialogue_height) // 2

running = True
show_dialogue = True  # Hiển thị đối thoại ban đầu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_dialogue = not show_dialogue  # Đảo trạng thái hiển thị đối thoại

    screen.fill((0, 0, 0))  # Màu nền đen

    # Vẽ màn hình chính của game

    if show_dialogue:
        # Vẽ cửa sổ thoại và văn bản lên màn hình chính
        screen.blit(dialogue_surface, (dialogue_x, dialogue_y))
        screen.blit(text, (dialogue_x + 10, dialogue_y + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
