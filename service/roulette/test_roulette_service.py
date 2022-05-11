from unittest import TestCase
from unittest.mock import patch

from service.roulette.roulette_service import RouletteService


class TestRouletteService(TestCase):

    def setUp(self) -> None:
        self.service = RouletteService(budget=500, bet=5)

    def test_play_once_zero(self):
        with patch('roulette_service.random.randint') as mocked_randint:
            mocked_randint.return_value = 0
            result = self.service.play_once()
            self.assertFalse(result)

    def test_play_once_uneven_number(self):
        with patch('roulette_service.random.randint') as mocked_randint:
            mocked_randint.return_value = 1
            result = self.service.play_once()
            self.assertFalse(result)

    def test_play_once_even_number(self):
        with patch('roulette_service.random.randint') as mocked_randint:
            mocked_randint.return_value = 2
            result = self.service.play_once()
            self.assertTrue(result)

    def test_calculate_probability(self):
        probability = self.service.calculate_probability(amount_values=100, possible_values=50)
        self.assertEqual(probability, 0.5)

        probability = self.service.calculate_probability(amount_values=100, possible_values=10)
        self.assertEqual(probability, 0.1)

        probability = self.service.calculate_probability(amount_values=100, possible_values=120)
        self.assertEqual(probability, 1)
