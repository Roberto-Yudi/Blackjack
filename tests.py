import blackjack
import unittest
from unittest import mock, TestCase
from blackjack import player_hit_cycle
from io import StringIO


class TestGame(TestCase):
    @mock.patch('blackjack.play')
    def test_game_starts(self, mock_game):
        blackjack.play()
        mock_game.assert_called()

    def runTest(self, given_answer, expected_out):
        with mock.patch('builtins.input', return_value=given_answer), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            player_hit_cycle()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_invalid_input(self):
        self.runTest('11', 'Invalid Input.')


if __name__ == '__main__':
    unittest.main()
