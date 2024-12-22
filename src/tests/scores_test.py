from os import remove
from os.path import isfile
from unittest import TestCase

from game.scores import set_database_name, save_score, get_scores

class TestScores(TestCase):
    def setUp(self):
        if isfile("test_scores.db"):
            remove("test_scores.db")

        set_database_name("test_scores.db")

        save_score(10, "Eemeli", 10, 10, 10)
        save_score(30, "Sergei", 10, 10, 10)
        save_score(20, "Polina", 10, 10, 10)

        save_score(100, "Hannu Hanhi", 30, 16, 99)
        save_score(99, "Hannu Hanhi", 30, 16, 99)

    def tearDown(self):
        if isfile("test_scores.db"):
            remove("test_scores.db")

    def test_get_scores_returns_correct_number_of_scores(self):
        scores = get_scores(10, 10, 10)
        self.assertEqual(len(scores), 3)

        scores = get_scores(30, 16, 99)
        self.assertEqual(len(scores), 2)

        scores = get_scores(16, 16, 40)
        self.assertEqual(len(scores), 0)

    def test_get_scores_returns_correctly_ordered_scores(self):
        scores = get_scores(10, 10, 10)

        self.assertEqual(scores[0].value, 10)
        self.assertEqual(scores[1].value, 20)
        self.assertEqual(scores[2].value, 30)

        scores = get_scores(30, 16, 99)

        self.assertEqual(scores[0].value, 99)
        self.assertEqual(scores[1].value, 100)
