import unittest
from io import StringIO
import sys
from buscaminas import Cell, BuscaMinas

class TestCell(unittest.TestCase):
    def test_cell_initial_state(self):
        cell = Cell(0)
        self.assertTrue(cell.hidden)
        self.assertEqual(cell.content, 0)

class TestBuscaMinas(unittest.TestCase):
    def test_grid_initialization(self):
        game = BuscaMinas(5, 4)
        self.assertEqual(len(game.grid), 4)
        for row in game.grid:
            self.assertEqual(len(row), 5)

    def test_display_output(self):
        game = BuscaMinas(2, 2, 1)
        expected_output = "\n. . \n. . \n\n"

        original_stdout = sys.stdout  # Save a reference to the original standard output
        sys.stdout = StringIO()       # Redirect standard output to a string
        game.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        sys.stdout = original_stdout  # Reset the standard output to its original value
    
    def test_bomb_spread(self):
        numberOfBomb = 0
        game = BuscaMinas()
        for row in game.grid:
            for col in row:
                if col.isBomb():
                    numberOfBomb += 1
        
        self.assertEqual(game.numberOfBombs, numberOfBomb)
        
    def test_select_cell_with_bomb(self):
        game = BuscaMinas()
        bomb_x, bomb_y = None, None

        # Find the position of a bomb
        for i in range(game.height):
            for j in range(game.width):
                if game.grid[i][j].isBomb():
                    bomb_x, bomb_y = i, j
                    break
        
        # It inst' verified yet the game over
        original_stdout = sys.stdout  
        sys.stdout = StringIO()      
        game.select_cell(bomb_x, bomb_y)
        output = sys.stdout.getvalue()  
        sys.stdout = original_stdout   
        self.assertIn("¡Boom!", output)
    
    def test_select_cell_without_bomb(self):
        game = BuscaMinas()
        empty_x, empty_y = None, None

        for i in range(game.height):
            for j in range(game.width):
                if not game.grid[i][j].isBomb():
                    empty_x, empty_y = i, j
                    break
        game.select_cell(empty_x, empty_y)
        self.assertFalse(game.grid[empty_x][empty_y].hidden)
    
    def test_add_numbers_no_bombs(self):
        game = BuscaMinas(3, 3, 0)
        game.add_numbers()

        expected_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.assertListEqual([[cell.content for cell in row] for row in game.grid], expected_grid)

    def test_add_numbers_with_bombs(self):
        game = BuscaMinas(3, 3, 3)
        game.add_numbers()

        for i in range(game.height):
            for j in range(game.width):
                if game.grid[i][j].isBomb():
                    self.assertEqual(game.grid[i][j].content, -1)

        for i in range(game.height):
            for j in range(game.width):
                if not game.grid[i][j].isBomb():
                    total_bombs_adjacent = sum(1 for ni in range(max(0, i - 1), min(game.height, i + 2))
                        for nj in range(max(0, j - 1), min(game.width, j + 2))
                            if game.grid[ni][nj].isBomb())
                    self.assertEqual(game.grid[i][j].content, total_bombs_adjacent)

        
if __name__ == '__main__':
    unittest.main()