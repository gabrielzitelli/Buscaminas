from buscaminas import BuscaMinas


def main():
    game = BuscaMinas()
    game.display()

    while True:
        x = int(input("X: "))
        y = int(input("Y: "))
        if x <= -1 or y <= -1:
            break

        mark = input("Mark? (y/n): ")
        if mark.lower() == "y":
            game.mark_cell(x, y)
        else:
            game.select_cell(x, y)

        game.display()


if __name__ == "__main__":
    main()
