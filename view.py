import pygame

from popup import EndgamePopup
from input import InputBox, Button
from buscaminas import BuscaMinas

FRAMERATE = 120

BOARD_CONTOUR_WIDTH = 75
BOARD_CONTOUR_HEIGHT = 75

# Colors
BACKGROUND_COLOR = (192, 192, 192)

# Board settings
INITIAL_BOARD_SIZE = 16
INITIAL_NUMBER_OF_BOMBS = 16

class MenuView:
    def __init__(self, screen):
        self.screen = screen
        self.game_started = False

        # Calculate measurements
        half_width = screen.get_width() // 2
        fifth_height = screen.get_height() // 5
        input_box_width = 100
        input_box_height = 32

        # Create input boxes
        self.input_boxes = []
        self.input_boxes.append(InputBox(half_width - input_box_width, (fifth_height * 2) - input_box_height, input_box_width, input_box_height, pygame.font.Font(None, 32), str(INITIAL_BOARD_SIZE), "Board Size:"))
        self.input_boxes.append(InputBox(half_width - input_box_width, (fifth_height * 3) - input_box_height, input_box_width, input_box_height, pygame.font.Font(None, 32), str(INITIAL_NUMBER_OF_BOMBS), "Bomb Count:"))

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

    def input_is_valid(self):
        board_size = self.input_boxes[0].get_text()
        bomb_count = self.input_boxes[1].get_text()

        # Check if input are numbers
        if not board_size.isdigit() or not bomb_count.isdigit():
            return False

        board_size = int(board_size)
        bomb_count = int(bomb_count)

        # Check if board size is in range
        if board_size < 2 or board_size > 30:
            return False

        # Check if bomb count is valid
        if bomb_count < 1:
            return False

        # Check if bomb count fits in board
        if board_size * board_size < bomb_count:
            return False

        return True

    def start_game(self):
        self.game_started = self.input_is_valid()

    def restart_game(self):
        self.game_started = False

    def handle_event(self, event):
        # Handle events for button
        self.start_button.handle_event(event)

        # Handle events for input boxes
        for box in self.input_boxes:
            box.handle_event(event)

        return (
            "GAME" if self.game_started else "MENU", 
            {
                "board_size": self.input_boxes[0].get_text(),
                "bomb_count": self.input_boxes[1].get_text(),
            }
        )

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

        # Initialize board
        self.board = None
        
        # Create display
        self.display = None

        # Create state map and initialize state
        self.state = "MENU"
        self.state_map = {
            "MENU": self.menu,
            "GAME": self.board
        }

    def run(self):
        running = True
        while running:
            next_state = self.state
            ctx = {}

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue

                # Handle events based on state
                next_state, ctx = self.state_map[self.state].handle_event(event)

            # Update screen based on state
            self.state_map[self.state].display(self.display)

            # Check if state changed
            if next_state != self.state:
                if next_state == "GAME" or next_state == "RESTART":
                    # Initialize board
                    self.board = BuscaMinas(self.screen_size, int(ctx["board_size"]), int(ctx["board_size"]), int(ctx["bomb_count"]))

                    # Create display
                    sprites, cell_sprite_size = self.board.load_sprites()
                    self.display = Display(sprites, cell_sprite_size, self.screen)
                    self.state_map["GAME"] = self.board
                    self.state_map["RESTART"] = self.board
                elif next_state == "MENU":
                    self.menu.restart_game()
                elif next_state == "POPUP":
                    self.state_map["POPUP"] = EndgamePopup(self.screen, ctx["message"])
                    self.state_map["POPUP"].store_game_info(ctx["board_size"], ctx["bomb_count"])

            # Update state
            self.state = next_state

            pygame.display.flip()
            self.clock.tick(FRAMERATE)

        pygame.quit()

class Display:
    def __init__(self, sprites, sprite_size, screen):
        self.sprites = sprites
        self.sprite_size = sprite_size
        self.screen = screen

    def draw_background(self):
        self.screen.fill(BACKGROUND_COLOR)

    def draw_cell(self, cell, index_pos):
        top_left_corner = (index_pos[0] * self.sprite_size[0] + BOARD_CONTOUR_WIDTH,
                           index_pos[1] * self.sprite_size[1] + BOARD_CONTOUR_HEIGHT)
        self.screen.blit(self.sprites[cell], top_left_corner)

    def draw_contour(self, width, height):
        contour_size = 4

        # NOTE: The order of the following draw functions is important
        # Draw right contour
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (BOARD_CONTOUR_WIDTH + width * self.sprite_size[0], BOARD_CONTOUR_HEIGHT, contour_size, height * self.sprite_size[1])
        )

        # Draw top contour
        pygame.draw.rect(
            self.screen, 
            (128, 128, 128), 
            (BOARD_CONTOUR_WIDTH - contour_size, BOARD_CONTOUR_HEIGHT - contour_size, width * self.sprite_size[0] + contour_size * 2, contour_size)
        )

        # Draw bottom contour
        pygame.draw.rect(
            self.screen, 
            (255, 255, 255), 
            (BOARD_CONTOUR_WIDTH - contour_size, BOARD_CONTOUR_HEIGHT + height * self.sprite_size[1], width * self.sprite_size[0] + contour_size * 2, contour_size)
        )

        # Draw left contour
        pygame.draw.rect(
            self.screen, 
            (128, 128, 128),
            (BOARD_CONTOUR_WIDTH - contour_size, BOARD_CONTOUR_HEIGHT, contour_size, height * self.sprite_size[1])
        )
