import pygame

from input import InputBox
from buscaminas import BuscaMinas

FRAMERATE = 120

BOARD_CONTOUR_WIDTH = 75
BOARD_CONTOUR_HEIGHT = 75

# Colors
BACKGROUND_COLOR = (192, 192, 192)

# Board settings
BOARD_WIDTH = 16
BOARD_HEIGHT = 16
NUMBER_OF_BOMBS = 16

class MenuView:
    def __init__(self, screen):
        self.screen = screen

        self.input_boxes = []
        self.input_boxes.append(InputBox(100, 100, 140, 32, pygame.font.Font(None, 32), "16"))
        self.input_boxes.append(InputBox(100, 300, 140, 32, pygame.font.Font(None, 32), "16"))

    def handle_event(self, event):
        for box in self.input_boxes:
            box.handle_event(event)

    def display(self, display):
        self.screen.fill(BACKGROUND_COLOR)

        for box in self.input_boxes:
            box.update()
            box.draw(self.screen)

class View:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption("Buscaminas")
        self.screen = pygame.display.set_mode(self.screen_size)

        # Initialize menu
        self.menu = MenuView(self.screen)

        # Initialize board (probably should be initialized after menu configuration)
        self.board = BuscaMinas(BOARD_WIDTH, BOARD_HEIGHT, NUMBER_OF_BOMBS)
        sprites, cell_sprite_size = self.board.load_sprites(screen_size)

        # Initialize display
        self.display = Display(sprites, cell_sprite_size, self.screen)

        # Create state map and initialize state
        self.state = "GAME"
        self.state_map = {
            "MENU": self.menu,
            "GAME": self.board
        }

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue

                # Handle events based on state
                self.state_map[self.state].handle_event(event)

            # Update screen based on state
            self.state_map[self.state].display(self.display)
            pygame.display.flip()
            self.clock.tick(FRAMERATE)

        pygame.quit()

class Display:
    def __init__(self, sprites, sprite_size, screen):
        self.sprites = sprites
        self.sprite_size = sprite_size
        self.screen = screen

    def draw_cell(self, cell, index_pos):
        top_left_corner = (index_pos[0] * self.sprite_size[0] + BOARD_CONTOUR_WIDTH,
                           index_pos[1] * self.sprite_size[1] + BOARD_CONTOUR_HEIGHT)
        self.screen.blit(self.sprites[cell], top_left_corner)
