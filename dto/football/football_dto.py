from dataclasses import dataclass


@dataclass
class FootballDto:
    team: str
    wins: int
    lost: int
    probability: float


@dataclass
class StandingsDto:
    pos: int
    name: str
    playedgames: int
    won: int
    lost: int
    draw: int
    plus_minus: int
    points: int
