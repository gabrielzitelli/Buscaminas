class BuscaMinas:
    def __init__(self, width=9, height=9):
        self.grid = [[". " for x in range(width)] for y in range(height)]
    
    def display(self):
        for row in self.grid:
            print(r" ".join(row))
                        
def main():
    game = BuscaMinas()
    game.display()
    

if __name__ == "__main__":
    main()