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



if __name__ == '__main__':
    unittest.main()