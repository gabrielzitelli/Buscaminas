import pygame

# Define some colors
COLOR_INACTIVE = (128, 128, 128)
COLOR_ACTIVE = (255, 255, 255)

class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.FONT = font

        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
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
                    print(self.text)
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