from unittest import TestCase

from service.birthday.birthday_service import calculate_probability


class Test(TestCase):
    def test_calculate_probability(self):
        amount_people = 1
        result = calculate_probability(amount_people=amount_people)
        self.assertEqual(result, 0)

        amount_people = 366
        result = calculate_probability(amount_people=amount_people)
        self.assertEqual(result, 100)

        amount_people = 10
        result = calculate_probability(amount_people=amount_people)
        self.assertEqual(result, 11.7)

        amount_people = 23
        result = calculate_probability(amount_people=amount_people)
        self.assertEqual(result, 50.7)
