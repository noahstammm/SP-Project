from dataclasses import dataclass


@dataclass
class FootballDto:
    team: str
    wins: int
    lost: int
    probability: float
    hint: str


