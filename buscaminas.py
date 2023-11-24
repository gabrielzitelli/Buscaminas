class BuscaMinas:
    def __init__(self, width=9, height=9):
        self.width = width
        self.height = height
        self.grid = [[Cell(0) for _ in range(width)] for _ in range(height)]
    
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

