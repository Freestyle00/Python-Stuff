import unittest
from program import (wincheck, ROCK, PAPER, SCISSORS,
    human_readable_converter)


class TestRockPaperScissors(unittest.TestCase):

    def test_wincheck(self):
        ergebnis=1/3
        self.assertTrue(0.3333332 < ergebnis < 0.3333334)
        self.assertEqual(wincheck(ROCK, ROCK), "draw")
        self.assertEqual(wincheck(ROCK, PAPER), False)
        self.assertEqual(wincheck(ROCK, SCISSORS), True)

        self.assertEqual(wincheck(PAPER, ROCK), True)
        self.assertEqual(wincheck(PAPER, SCISSORS), False)

        self.assertEqual(wincheck(SCISSORS, ROCK), False)
        self.assertEqual(wincheck(SCISSORS, PAPER), True)

    def test_human_readable_converter(self):
        self.assertEqual(human_readable_converter(ROCK), "Rock")
        self.assertEqual(human_readable_converter(PAPER), "Paper")
        self.assertEqual(human_readable_converter(SCISSORS), "Scissors")


    def test_exception_in_human_readable_converter(self):
        self.assertRaises(Exception, human_readable_converter,"xyz")
        try:
            human_readable_converter("xyz")
        except Exception as exp:
            self.assertEqual(str(exp), "Not translatable input detected \"xyz\" please check what has gone wrong")






