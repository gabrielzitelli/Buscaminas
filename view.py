import pygame

from input import InputBox, Button
from buscaminas import BuscaMinas

FRAMERATE = 120

BOARD_CONTOUR_WIDTH = 75
BOARD_CONTOUR_HEIGHT = 75

# Colors
BACKGROUND_COLOR = (192, 192, 192)

# Board settings
BOARD_SIZE = 16
NUMBER_OF_BOMBS = 16

class MenuView:
    def __init__(self, screen):
        self.screen = screen

        # Calculate measurements
        half_width = screen.get_width() // 2
        fifth_height = screen.get_height() // 5
        input_box_width = 100
        input_box_height = 32

        # Create input boxes
        self.input_boxes = []
        self.input_boxes.append(InputBox(half_width - input_box_width, (fifth_height * 2) - input_box_height, input_box_width, input_box_height, pygame.font.Font(None, 32), str(BOARD_SIZE), "Board Size:"))
        self.input_boxes.append(InputBox(half_width - input_box_width, (fifth_height * 3) - input_box_height, input_box_width, input_box_height, pygame.font.Font(None, 32), str(BOARD_SIZE), "Bomb Count:"))

        # Create button
        self.start_button = Button(
            half_width - input_box_width // 2, 
            fifth_height * 4, 
            input_box_width, 
            input_box_height, 
            "Play", 
            pygame.font.Font(None, 32), 
            self.start_game
        )

    def start_game(self):
        print("Start game")

    def handle_event(self, event):
        # Handle events for button
        self.start_button.handle_event(event)

        # Handle events for input boxes
        for box in self.input_boxes:
            box.handle_event(event)

    def display(self, display):
        # Draw background
        self.screen.fill(BACKGROUND_COLOR)

        # Draw title
        title_font = pygame.font.Font(None, 96)
        title_text = title_font.render("Buscaminas", True, (96, 96, 96))
        title_text_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 7))
        self.screen.blit(title_text, title_text_rect)

        # Draw button with padding
        self.start_button.draw(self.screen)

        # Draw input boxes
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
        self.board = BuscaMinas(BOARD_SIZE, BOARD_SIZE, NUMBER_OF_BOMBS)
        sprites, cell_sprite_size = self.board.load_sprites(screen_size)

        # Initialize display
        self.display = Display(sprites, cell_sprite_size, self.screen)

        # Create state map and initialize state
        self.state = "MENU"
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
