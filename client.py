# battle ship command line game
from network import Network


class Battleship:
    def __init__(self) -> None:
        self.client = Network()


if __name__ == "__main__":
    Battleship()