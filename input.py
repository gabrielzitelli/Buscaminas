import pygame

# Define some colors
BACKGROUND_COLOR = (192, 192, 192)
COLOR_INACTIVE = (128, 128, 128)
COLOR_ACTIVE = (255, 255, 255)

class InputBox:
    def __init__(self, x, y, w, h, font, text='', label=''):
        self.FONT = font

        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.label = label
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def get_text(self):
        return self.text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the label
        screen.blit(self.FONT.render(self.label, True, COLOR_INACTIVE), (self.rect.x, self.rect.y-25))

        # Blit the text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

        # Blit the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

        # Blit white border around the bottom and right side of the input box
        border_width = 3
        pygame.draw.rect(screen, COLOR_INACTIVE, (self.rect.x, self.rect.y, self.rect.w, border_width))
        pygame.draw.rect(screen, COLOR_INACTIVE, (self.rect.x, self.rect.y, border_width, self.rect.h))

        # Blit dark grey border around the top and left side of the input box
        pygame.draw.rect(screen, COLOR_ACTIVE, (self.rect.x, self.rect.y + self.rect.h - border_width, self.rect.w, border_width))
        pygame.draw.rect(screen, COLOR_ACTIVE, (self.rect.x + self.rect.w - border_width, self.rect.y, border_width, self.rect.h))

class Button:
    def __init__(self, x, y, w, h, text='Click', font=None, on_click=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.on_click = on_click

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos) and self.on_click is not None:
                    self.on_click()

    def draw(self, screen):
        # Draw button with padding
        button_padding = 10
        button_text = self.font.render(self.text, True, COLOR_INACTIVE)
        button_text_rect = button_text.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))
        button_rect = pygame.Rect(button_text_rect.x - button_padding * 2, button_text_rect.y - button_padding, button_text_rect.width + button_padding * 4, button_text_rect.height + button_padding * 2)
        pygame.draw.rect(screen, BACKGROUND_COLOR, button_rect)
        screen.blit(button_text, button_text_rect)

        # Draw white border around the left and top side of the button
        border_width = 3
        pygame.draw.rect(screen, COLOR_ACTIVE, (button_rect.x, button_rect.y, button_rect.w, border_width))
        pygame.draw.rect(screen, COLOR_ACTIVE, (button_rect.x, button_rect.y, border_width, button_rect.h))

        # Draw dark grey border around the right and bottom side of the button
        pygame.draw.rect(screen, COLOR_INACTIVE, (button_rect.x, button_rect.y + button_rect.h - border_width, button_rect.w, border_width))
        pygame.draw.rect(screen, COLOR_INACTIVE, (button_rect.x + button_rect.w - border_width, button_rect.y, border_width, button_rect.h))
