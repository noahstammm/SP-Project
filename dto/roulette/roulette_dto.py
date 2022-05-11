from dataclasses import dataclass


@dataclass
class RouletteDto:
    budget: int
    bet: int
    amount_rounds: int
