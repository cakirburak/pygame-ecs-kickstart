from game import Game

def main():
    # 320x180 is the base resolution
    # imagine you design your game levels with that resolution
    # Game class will automatically scale it to FULLSCREEN without changing the aspect ratio
    game = Game(320, 180)
    game.run()

if __name__ == "__main__":
    main()

