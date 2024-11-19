from bitarray import bitarray
from random import random

class GameState():
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines

        num_tiles = width * height

        self.mines = bitarray(num_tiles)
        mines_left = num_mines
        tiles_left = num_tiles

        for i in range(num_tiles):
            lay_mine = random() < mines_left / tiles_left
            self.mines[i] = lay_mine
            mines_left -= lay_mine
            tiles_left -= 1

        self.opened = bitarray(num_tiles)
        self.opened.setall(False)

    def is_valid_tile(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def is_mine(self, x, y):
        return self.mines[x + y * self.width]

    def is_open(self, x, y):
        return self.opened[x + y * self.width]

    def surrounding_tiles(self, x, y):
        left = x > 0
        right = x < self.width - 1
        up = y > 0
        down = y < self.height - 1

        if left: yield (x - 1, y)
        if right: yield (x + 1, y)
        if up: yield (x, y - 1)
        if down: yield (x, y + 1)

        if left and up: yield (x - 1, y - 1)
        if left and down: yield (x - 1, y + 1)
        if right and up: yield (x + 1, y - 1)
        if right and down: yield (x + 1, y + 1)

    def num_surrounding_mines(self, x, y):
        return sum(self.is_mine(u, v) for u, v in self.surrounding_tiles(x, y))

    def open(self, x, y):
        index = x + y * self.width

        if self.opened[index]:
            return False

        self.opened[index] = True

        if self.is_mine(x, y):
            return True

        if not self.num_surrounding_mines(x, y):
            for u, v in self.surrounding_tiles(x, y):
                mine = self.open(u, v)
                assert not mine

        return False
