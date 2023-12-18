# TP Análisis de la Información: Buscaminas

Practical work for the Information Analysis course at the Faculty of Engineering of the University of Buenos Aires (FIUBA).

## The game and its rules

Minesweeper is a computer game that originated in the 1960s and became popular with its inclusion in the Windows operating system. The objective of the game is to clear a minefield without detonating a mine. The field is represented as a grid of square cells, some of which contain hidden mines. The player clicks on cells to uncover what's underneath. Each cell reveals a number indicating the number of adjacent mines (within a radius of 1 square around it). Using this information, the player must deduce the location of the mines and mark them with flags.
The game is based on logic and deduction, and players must avoid clicking on mined cells. Clicking on a mine results in the loss of the game. The challenge lies in using the information provided by the numbers to make strategic decisions and avoid mines. The game has different difficulty levels, adjusting the field size and the number of mines to increase complexity. The ultimate goal is to reveal all non-mined cells without detonating any mines.

## Technologies

For this project, it was decided to use [Python](https://www.python.org) (Compatible with versions 3.9 and above).

The graphical interface was created using [Pygame](https://www.pygame.org/tags/framework).

To create the executable, the [Pyinstaller](https://pyinstaller.org/) library was used.

## How to run the game

The game is available only on Windows and is executed using the .exe found in the latest release.

## How to contribute to the project

To start development, you should install the necessary dependencies with the following command:

```shell
# On Windows
py -m pip install pygame
# On Linux
pip install pygame
```

Then, you should clone the repository to work on the latest available version.

To test changes locally, use the following line:

```shell
python main.py
```

Group

- Member 1 - Gabriel Zitelli-
- Member 2 - Francisco Strambini
- Member 3 - Julio Piñango
- Member 4 - Walter Mamani
- Member 5 - Gian Keberlein
