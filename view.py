import pygame
import os

from buscaminas import BuscaMinas, GameOverWin, GameOverLose

FRAMERATE = 120

BOARD_CONTOUR_WIDTH = 75
BOARD_CONTOUR_HEIGHT = 75

# Board settings
BOARD_WIDTH = 4
BOARD_HEIGHT = 4
NUMBER_OF_BOMBS = 4


class View:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption("Buscaminas")
        self.screen = pygame.display.set_mode(self.screen_size)

        self.board = BuscaMinas(BOARD_WIDTH, BOARD_HEIGHT, NUMBER_OF_BOMBS)

        self.cell_sprite_size = ((screen_size[0] - BOARD_CONTOUR_WIDTH * 2) // BOARD_WIDTH,
                                 (screen_size[1] - BOARD_CONTOUR_HEIGHT * 2) // BOARD_HEIGHT)
        self.sprites = {}
        self.load_sprites()
        self.display = Display(self.sprites, self.cell_sprite_size, self.screen)

    def load_sprites(self):
        cells_path = "sprites/cells"
        for filename in os.listdir(cells_path):
            sprite = pygame.image.load(cells_path + "/" + filename)
            sprite = sprite.convert()
            sprite = pygame.transform.scale(sprite, self.cell_sprite_size)
            self.sprites[filename.split(".")[0]] = sprite

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue

                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        self.interact(event.pos[0], event.pos[1], pygame.mouse.get_pressed(num_buttons=3)[2])
                        self.board.check_game_over()
                    except GameOverWin as e:
                        pass
                    except GameOverLose as e:
                        pass

            self.board.display(self.display)
            pygame.display.flip()
            self.clock.tick(FRAMERATE)

        pygame.quit()

    def interact(self, x, y, flag):
        index = (int((x - BOARD_CONTOUR_WIDTH) // self.cell_sprite_size[0]),
                 int((y - BOARD_CONTOUR_HEIGHT) // self.cell_sprite_size[1]))
        if index[0] < 0 or index[0] >= BOARD_WIDTH or index[1] < 0 or index[1] >= BOARD_HEIGHT:
            return

        if flag:
            self.board.mark_cell(index[0], index[1])
        else:
            self.board.select_cell(index[0], index[1])


class Display:
    def __init__(self, sprites, sprite_size, screen):
        self.sprites = sprites
        self.sprite_size = sprite_size
        self.screen = screen

    def draw_cell(self, cell, index_pos):
        top_left_corner = (index_pos[0] * self.sprite_size[0] + BOARD_CONTOUR_WIDTH,
                           index_pos[1] * self.sprite_size[1] + BOARD_CONTOUR_HEIGHT)
        self.screen.blit(self.sprites[cell], top_left_corner)
