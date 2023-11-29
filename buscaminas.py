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
    
    def display(self):
        print()
        for row in self.grid:
            for col in row:
                print(". " if col.hidden else f"{col.content} ", end="")
            print()
        print()


class Cell:
    def __init__(self, content) -> None:
        self.hidden = True
        self.content = content

    def isBomb(self) -> bool:
        return self.content == -1

