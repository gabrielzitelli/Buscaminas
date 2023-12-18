import pygame

from input import Button

class Popup:
    """
    View that displays a popup with a message and two buttons
    """
    def __init__(self, screen, message, button1_text, button2_text, on_button1_click, on_button2_click):
        self.screen = screen
        self.message = message
        self.button1_text = button1_text
        self.button2_text = button2_text
        self.on_button1_click = on_button1_click
        self.on_button2_click = on_button2_click

        # Calculate measurements
        half_width = screen.get_width() // 2
        half_height = screen.get_height() // 2
        input_box_width = 100
        input_box_height = 32

        # Create buttons
        self.button1 = Button(
            half_width - input_box_width * 1.5, 
            half_height + input_box_height, 
            input_box_width, 
            input_box_height, 
            button1_text, 
            pygame.font.Font(None, 32), 
            self.on_button1_click
        )
        self.button2 = Button(
            half_width + input_box_width * 0.5, 
            half_height + input_box_height, 
            input_box_width, 
            input_box_height, 
            button2_text, 
            pygame.font.Font(None, 32), 
            self.on_button2_click
        )

    def handle_event(self, event):
        # Handle events for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)
        return "POPUP", {}

    def display(self, display):
        # Draw low opacity background
        background = pygame.Surface(self.screen.get_size())
        background.fill((192, 192, 192))
        background.set_alpha(8)
        self.screen.blit(background, (0, 0))

        # Draw message
        message_font = pygame.font.Font(None, 48)
        message_text = message_font.render(self.message, True, (96, 96, 96))
        message_text_rect = message_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 3))
        self.screen.blit(message_text, message_text_rect)

        # Draw buttons
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)

class EndgamePopup(Popup):
    """
    View that displays a popup with a message and two buttons
    """
    def __init__(self, screen, message):
        self.must_restart = False
        self.must_go_to_menu = False
        self.board_size = None
        self.bomb_count = None
        super().__init__(screen, message, "Restart", "Main Menu", self.handle_restart, self.handle_menu)

    def handle_restart(self):
        self.must_restart = True

    def handle_menu(self):
        self.must_go_to_menu = True

    def handle_event(self, event):
        # Handle events for buttons
        self.button1.handle_event(event)
        self.button2.handle_event(event)

        # Check if buttons were clicked
        if self.must_restart:
            self.must_restart = False
            return "RESTART", {
                "board_size": self.board_size,
                "bomb_count": self.bomb_count
            }
        elif self.must_go_to_menu:
            self.must_go_to_menu = False
            return "MENU", {}
        
        return "POPUP", {}
    
    def store_game_info(self, board_size, bomb_count):
        self.board_size = board_size
        self.bomb_count = bomb_count