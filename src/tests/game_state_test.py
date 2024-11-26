from unittest import TestCase
from game.game_state import GameState

class TestGameState(TestCase):
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
