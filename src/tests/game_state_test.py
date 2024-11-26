from unittest import TestCase
from game.game_state import GameState

class TestGameState(TestCase):
    def setUp(self):
        mines = [
                0,0,0,0,0,0,0,0,0,0,
                0,0,1,0,0,0,0,0,0,0,
                0,0,0,0,0,0,1,1,0,0,
                0,1,0,0,1,0,0,0,0,0,
                0,0,0,0,0,0,0,1,0,0,
                0,0,0,0,0,1,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,
                0,0,1,1,0,0,0,0,0,0,
                0,0,0,0,0,0,0,1,0,0,
                0,0,0,0,0,0,0,0,0,0,
        ]

        self.preset_board = GameState(10, 10, 10)

        for i in range(100):
            self.preset_board.mines[i] = mines[i]

        self.preset_board.mines_laid = True

    def test_number_of_generated_mines_is_correct(self):
        configurations = (
                (10, 10, 10),
                (20, 15, 30),
                (20, 15, 60)
        )

        for conf in configurations:
            for _ in range(10):
                state = GameState(conf[0], conf[1], conf[2])
                state.lay_mines(-1, -1)
                self.assertEqual(state.mines.count(), conf[2])

    def test_number_of_surrounding_mines_is_correct(self):
        expected = [
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,0,1,0,1,2,2,1,0],
            [1,2,2,2,1,2,0,0,1,0],
            [1,0,1,1,0,2,3,3,2,0],
            [1,1,1,1,2,2,2,0,1,0],
            [0,0,0,0,1,0,2,1,1,0],
            [0,1,2,2,2,1,1,0,0,0],
            [0,1,0,0,1,0,1,1,1,0],
            [0,1,2,2,1,0,1,0,1,0],
            [0,0,0,0,0,0,1,1,1,0]
        ]

        for x in range(10):
            for y in range(10):
                if self.preset_board.is_mine(x, y):
                    continue

                self.assertEqual(self.preset_board.num_surrounding_mines(x, y), expected[y][x])

    def test_open(self):
        tiles_to_open = [(1, 4), (0, 9), (2, 1)]
        expected = [
            [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
            ], [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,0,0,0,0],
                [1,1,1,1,1,0,0,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
                [1,1,0,0,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
            ], [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,0,0,0,0],
                [1,1,1,1,1,0,0,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
                [1,1,0,0,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,0,0,0],
            ]
        ]

        for i in range(3):
            self.preset_board.open(*tiles_to_open[i])
            for x in range(10):
                for y in range(10):
                    self.assertEqual(self.preset_board.is_open(x, y), expected[i][y][x])
