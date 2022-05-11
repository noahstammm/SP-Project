import random


class RouletteService:

    def __init__(self, budget: int, bet: int):
        self.budget = budget
        self.bet = bet
        self.highest_field = 36

    def play_once(self) -> bool:
        """
        Spin the wheel and determine if you win or lost
        :return: True if you won, False if you lost
        """
        chosen_field = random.randint(0, self.highest_field)
        if chosen_field == 0:
            return False
        elif chosen_field % 2 == 0:
            return True
        else:
            return False

    def play(self) -> int:
        """
        Play until no budget remains
        :return: The amount of rounds that can be played.
        """
        amount_rounds = 0
        amount_fields = self.highest_field + 1
        probability = self.calculate_probability(amount_values=amount_fields, possible_values=(self.highest_field // 2))
        while self.budget > self.bet:
            self.budget -= self.bet
            if self.play_once():
                self.budget += self.bet / probability
            amount_rounds += 1
        return amount_rounds

    def calculate_probability(self, amount_values: int, possible_values: int) -> float:
        """
        Calculate the probability.
        :param amount_values: Amount all values
        :param possible_values: Amount of values that can happen
        :return: The probability
        """
        if amount_values < possible_values:
            return 1
        elif amount_values == 0:
            return 0
        else:
            return possible_values / amount_values
