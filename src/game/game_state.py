from random import random
from bitarray import bitarray

class GameState():
    """
    Sisältää pelitilan ja huolehtii metodeillaan pelilogiikasta.
    """

    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines

        num_tiles = width * height

        self.mines = bitarray(num_tiles)
        self.mines_laid = False

        self.opened = bitarray(num_tiles)
        self.opened.setall(False)

    def is_valid_tile(self, x, y):
        """Palauttaa totuusarvona, onko (x, y) pelikentän rajojen sisällä."""
        return 0 <= x < self.width and 0 <= y < self.height

    def is_mine(self, x, y):
        return self.mines[x + y * self.width]

    def is_open(self, x, y):
        return self.opened[x + y * self.width]

    def surrounding_tiles(self, x, y):
        """Iteroi ruutua (x, y) ympäröivien ruutujen yli."""
        left = x > 0
        right = x < self.width - 1
        up = y > 0
        down = y < self.height - 1

        if left:
            yield (x - 1, y)
        if right:
            yield (x + 1, y)
        if up:
            yield (x, y - 1)
        if down:
            yield (x, y + 1)

        if left and up:
            yield (x - 1, y - 1)
        if left and down:
            yield (x - 1, y + 1)
        if right and up:
            yield (x + 1, y - 1)
        if right and down:
            yield (x + 1, y + 1)

    def num_surrounding_mines(self, x, y):
        return sum(self.is_mine(u, v) for u, v in self.surrounding_tiles(x, y))

    def open(self, x, y):
        """
        Avaa ruudun. Mikäli tässä tai tätä ympäröivissä ruuduissa ei
        ole miinoja, avaa myös ympäröivät ruudut ja niin edelleen.
        """

        if not self.mines_laid:
            self.lay_mines(x, y)

        index = x + y * self.width

        if self.opened[index]:
            return

        self.opened[index] = True

        if not self.is_mine(x, y) and not self.num_surrounding_mines(x, y):
            for u, v in self.surrounding_tiles(x, y):
                assert not self.is_mine(u, v)
                self.open(u, v)

    def lay_mines(self, exclude_x, exclude_y):
        """Asettelee miinat satunnaisesti pelikentälle."""

        num_tiles = self.width * self.height
        mines_left = self.num_mines
        tiles_left = num_tiles - 1 if self.is_valid_tile(exclude_x, exclude_y) else num_tiles
        exclude = exclude_x + exclude_y * self.width

        for i in range(num_tiles):
            if i == exclude:
                continue

            lay_mine = random() < mines_left / tiles_left
            self.mines[i] = lay_mine
            mines_left -= lay_mine
            tiles_left -= 1

        self.mines_laid = True

    def solved(self):
        """Palauttaa totuusarvona, onko peli voitettu."""
        return (self.mines ^ self.opened).all()

    def lost(self):
        """Palauttaa totuusarvona, onko peli hävitty."""
        return (self.mines & self.opened).any()
