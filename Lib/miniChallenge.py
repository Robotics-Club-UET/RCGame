import pygame
from maze_generator import *
import random


def check_goal(player,goal):
    global time, score
    if player.rect.collidepoint(goal.rect.center):
        goal.set_pos()
        # score += 1
        return True
    return False


class Goal(pygame.sprite.Sprite):
    def __init__(self):
        super(Goal, self).__init__()
        self.animations = import_folder("../Graphics/NPC/start")

        self.img = pygame.image.load('../Graphics/NPC/XH.gif')  # .convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.set_pos()
        self.frame_index = 0
    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + TILE * 0.25, randrange(rows) * TILE + TILE * 0.25
    def update(self, dt):
        self.frame_index += 6 * dt
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]


def game_maze():
    def is_collide(x, y):
        tmp_rect = player.rect.move(x, y)
        if tmp_rect.collidelist(walls_collide_list) == -1:
            return False
        return True

    class Robot(pygame.sprite.Sprite):
        def __init__(self):
            super(Robot, self).__init__()
            self.animations = import_folder("../Graphics/NPC/robot_agent")
            print(len(self.animations))
            self.img = pygame.image.load('../Graphics/NPC/XH.gif')  # .convert_alpha()
            self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
            self.rect = self.img.get_rect()
            self.frame_index = 0

            # for player settings
            self.player_speed = 3
            self.rect.center = TILE // 2, TILE // 2
            self.directions = {'a': (-self.player_speed, 0), 'd': (self.player_speed, 0), 'w': (0, -self.player_speed),
                               's': (0, self.player_speed)}
            self.keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
            self.direction = (0, 0)

        def move(self):
            global time, score
            pressed_key = pygame.key.get_pressed()
            for key, key_value in self.keys.items():
                # print(pressed_key[key_value],is_collide(*self.directions[key]))
                if pressed_key[key_value] and not is_collide(*self.directions[key]):
                    self.direction = self.directions[key]
                    # time += 1
                    break
                else:
                    self.direction = (0, 0)
            if not is_collide(*self.direction):
                self.rect.move_ip(self.direction)
            # self.rect.center = (self.rect.center[0]+1,self.rect.center[1]+1)

        def update(self, dt):
            self.frame_index += 6 * dt
            if self.frame_index >= len(self.animations):
                self.frame_index = 0
            self.image = self.animations[int(self.frame_index)]
            self.move()

    time = 0
    score = 0

    pygame.init()
    screen = pygame.display.set_mode(RES)
    game_surface = pygame.Surface(RES)
    # surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    surface = pygame.display.set_mode((WIDTH, HEIGHT + 25))
    clock = pygame.time.Clock()

    grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0]
    stack = []
    goal = Goal()
    player = Robot()
    group = pygame.sprite.Group(goal, player)

    running = True

    walls_collide_list = sum([cell.get_rects() for cell in grid_cells], [])
    break_count = 1
    get_walls_collide_list = True

    # fonts
    # font = pygame.font.Font('Font/RetroGaming.ttf', 15)
    text_font = pygame.font.Font('../Font/RetroGaming.ttf', 15)

    while running:

        surface.blit(game_surface, (0, 0))
        game_surface.fill(pygame.Color("gray4"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                time -= 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        if keys[pygame.K_ESCAPE]:
            running = False
            print("ESC")

        [cell.draw(game_surface) for cell in grid_cells]
        current_cell.visited = True
        current_cell.draw(game_surface)
        current_cell.get_rects(game_surface)

        check_goal(player,goal)

        next_cell = current_cell.check_neighbors(grid_cells)
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
            break_count += 1
        elif stack:
            current_cell = stack.pop()
        walls_collide_list = sum([cell.get_rects() for cell in grid_cells], [])

        dt = clock.tick(60) / 1000
        group.update(dt)
        group.draw(game_surface)
        pygame.display.flip()

        surface.blit(text_font.render('R: Re-initialize the maze', True, pygame.Color('lightblue'), True), (10, HEIGHT))
        surface.blit(text_font.render('ESC: Break of mini challenge', True, pygame.Color('lightblue'), True), (300, HEIGHT))

# game_maze()