import sys

class Ship:
    def __init__(self, size: int):
        self.size = size
        self.hits = 0
        self.positions = []

    def place(self, positions: list[tuple[int, int]]) -> None:
        self.positions = positions

    def hit(self) -> bool:
        if self.hits < self.size:
            self.hits += 1
        return self.is_sunk()

    def is_sunk(self) -> bool:
        return self.hits >= self.size


class Battleship(Ship):
    def __init__(self):
        super().__init__(4)


class Cruiser(Ship):
    def __init__(self):
        super().__init__(3)


class Destroyer(Ship):
    def __init__(self):
        super().__init__(2)


class Submarine(Ship):
    def __init__(self):
        super().__init__(1)


class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship: Ship, start_row: int, start_col: int, horizontal: bool = True) -> bool:
        positions = []
        for i in range(ship.size):
            r = start_row
            c = start_col
            if horizontal:
                c += i
            else:
                r += i

            if r >= self.size or c >= self.size or self.grid[r][c] != ' ':
                return False
            positions.append((r, c))

        for r, c in positions:
            self.grid[r][c] = 'S'
        ship.place(positions)
        self.ships.append(ship)
        return True

    def receive_shot(self, row: int, col: int) -> bool:
        if self.grid[row][col] == 'X' or self.grid[row][col] == 'O':
            return False
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            for ship in self.ships:
                if (row, col) in ship.positions:
                    ship.hit()
                    break
            return True
        else:
            self.grid[row][col] = 'O'
            return False

    def display(self) -> list[list[str]]:
        return self.grid

    def display_hidden(self) -> list[list[str]]:
        return [[' ' if cell == 'S' else cell for cell in row] for row in self.grid]

    def all_ships_sunk(self) -> bool:
        return all(ship.is_sunk() for ship in self.ships)


exec(sys.stdin.read())
