from view import View

RESOLUTION = (600, 600)


def main():
    game = View(RESOLUTION)
    try:
        game.run()
    except:
        print("Game Over")


if __name__ == "__main__":
    main()
