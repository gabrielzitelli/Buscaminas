import pygame, random, os

BOARD_CONTOUR_WIDTH = 75
BOARD_CONTOUR_HEIGHT = 75

BOARD_WIDTH = 16
BOARD_HEIGHT = 16

class BuscaMinas:
    def __init__(self, width=9, height=9, number_of_bombs=10):
        self.width = width
        self.height = height
        self.numberOfBombs = number_of_bombs
        self.grid = [[Cell(0) for _ in range(width)] for _ in range(height)]
        self.bombsFounds = 0

        if self.width * self.height < number_of_bombs:
            raise Exception("It is not possible to spread all bombs")

        self.spawn_bombs(number_of_bombs)
        self.add_numbers()

    def load_sprites(self, screen_size):
        # Calculate sprite size
        self.cell_sprite_size = (
            (screen_size[0] - BOARD_CONTOUR_WIDTH * 2) // BOARD_WIDTH,
            (screen_size[1] - BOARD_CONTOUR_HEIGHT * 2) // BOARD_HEIGHT,
        )

        # Load sprites and scale them
        self.sprites = {}
        cells_path = "sprites/cells"
        for filename in os.listdir(cells_path):
            sprite = pygame.image.load(cells_path + "/" + filename)
            sprite = sprite.convert()
            sprite = pygame.transform.scale(sprite, self.cell_sprite_size)
            self.sprites[filename.split(".")[0]] = sprite

        return self.sprites, self.cell_sprite_size

    def spawn_bombs(self, number_of_bombs):
        while number_of_bombs != 0:
            rand_x = random.randint(0, self.height - 1)
            rand_y = random.randint(0, self.width - 1)

            if self.grid[rand_x][rand_y].is_bomb():
                continue
            else:
                self.grid[rand_x][rand_y].content = -1

            number_of_bombs -= 1

    def interact(self, x, y, flag):
        index = (int((x - BOARD_CONTOUR_WIDTH) // self.cell_sprite_size[0]),
                 int((y - BOARD_CONTOUR_HEIGHT) // self.cell_sprite_size[1]))
        if index[0] < 0 or index[0] >= BOARD_WIDTH or index[1] < 0 or index[1] >= BOARD_HEIGHT:
            return

        if flag:
            self.mark_cell(index[0], index[1])
        else:
            self.select_cell(index[0], index[1])

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                self.interact(event.pos[0], event.pos[1], pygame.mouse.get_pressed(num_buttons=3)[2])
            except GameOverWin as e:
                pass
            except GameOverLose as e:
                pass

    def display(self, display):
        for i in range(self.height):
            for j in range(self.width):
                display.draw_cell(self.grid[i][j].display(), (i, j))

    def select_cell(self, x, y):
        cell = self.grid[x][y]

        if cell.is_bomb():
            self.game_over_lose(cell)
        else:
            self.reveal_cell_and_adjacent(x, y)

    def reveal_cell_and_adjacent(self, x, y):
        cell = self.grid[x][y]
        if cell.hidden:
            cell.reveal()
            if cell.content == 0:
                self.reveal_empty_cells(x, y)

    def reveal_empty_cells(self, x, y):
        for i in range(max(0, x - 1), min(self.height, x + 2)):
            for j in range(max(0, y - 1), min(self.width, y + 2)):
                self.reveal_cell_and_adjacent(i, j)

    def add_numbers(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].content == 0:
                    for ni in range(max(0, i - 1), min(self.height, i + 2)):
                        for nj in range(max(0, j - 1), min(self.width, j + 2)):
                            if self.grid[ni][nj].is_bomb():
                                self.grid[i][j].content += 1

    def mark_cell(self, x, y):
        cell = self.grid[x][y]
        if cell.hidden:
            cell.mark()
            self.bombsFounds += 1
            if self.bombsFounds == self.numberOfBombs:
                self.game_over_win()

    def game_over_win(self):
        print("¡You win!")
        self.show_bombs("bomb")
        raise GameOverWin()

    def game_over_lose(self, cell_clicked):
        print("You lose!")
        self.show_bombs("bomb_detonated")
        cell_clicked.content = "bomb_clicked"
        raise GameOverLose()

    def show_bombs(self, content):
        for row in self.grid:
            for col in row:
                if col.is_bomb():
                    col.reveal()
                    col.content = content


class Cell:
    def __init__(self, content) -> None:
        self.hidden = True
        self.marked = False
        self.content = content

    def is_bomb(self) -> bool:
        return self.content == -1

    def mark(self):
        self.marked = not self.marked

    def reveal(self):
        self.hidden = False
        self.marked = False

    def display(self):
        if self.marked:
            return "marked"
        elif self.hidden:
            return "hidden"
        else:
            return str(self.content)


class GameOverWin(Exception):
    pass


class GameOverLose(Exception):
    pass
