import unittest
import guessing_game

class TestGuessingGame(unittest.TestCase):

    def test_game1(self):
        test_answer = 10
        test_guess = 10
        result = guessing_game.run_guess(test_guess, test_answer)
        self.assertTrue(result)

    def test_wrong_answer(self):
        test_answer = 10
        test_guess = 0
        result = guessing_game.run_guess(test_guess, test_answer)
        self.assertFalse(result)

    def test_wrong_input(self):
        test_answer = 10
        test_guess = 15
        result = guessing_game.run_guess(test_guess, test_answer)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()