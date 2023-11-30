import random


class BuscaMinas:
    def __init__(self, width=9, height=9, numberOfBombs=10):
        self.width = width
        self.height = height
        self.numberOfBombs = numberOfBombs
        self.grid = [[Cell(0) for _ in range(width)] for _ in range(height)]

        if (self.width * self.height < numberOfBombs):
            raise Exception("It is not possible to spread all bombs")

        while numberOfBombs != 0:
            rand_x = random.randint(0, height-1)
            rand_y = random.randint(0, width-1)

            if self.grid[rand_x][rand_y].isBomb():
                continue
            else:
                self.grid[rand_x][rand_y].content = -1

            numberOfBombs -= 1
        
        self.add_numbers()
    
    def display(self):
        print()
        for row in self.grid:
            for col in row:
                if col.marked:
                    cell_display = "M "
                elif col.hidden:
                    cell_display = ". "
                else:
                    cell_display = str(col.content) + " "

                print(cell_display, end="")
            print()
        print()

    def select_cell(self, x, y):
        cell = self.grid[x][y]

        if cell.isBomb():
            print("¡Boom!")
        else:
            self.reveal_cell_and_adjacent(x, y)

    def reveal_cell_and_adjacent(self, x, y):
        cell = self.grid[x][y]
        if cell.hidden:
            cell.hidden = False
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
                            if self.grid[ni][nj].isBomb():
                                self.grid[i][j].content += 1

    def mark_cell(self, x, y):
        cell = self.grid[x][y]
        if cell.hidden:
            cell.mark()


class Cell:
    def __init__(self, content) -> None:
        self.hidden = True
        self.marked = False
        self.content = content

    def isBomb(self) -> bool:
        return self.content == -1

    def mark(self):
        self.marked = not self.marked
