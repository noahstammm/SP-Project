from dataclasses import dataclass
from decimal import Decimal


@dataclass
class BirthdayDto:
    amount_people: int
    probability: Decimal
