from decimal import Decimal


def calculate_probability(amount_people: int) -> Decimal:
    # Formel von Laplace
    # https://de.wikipedia.org/wiki/Laplace-Formel
    no_birthday_equality = 1
    for i in range(amount_people):
        no_birthday_equality = no_birthday_equality * (365 - i) / 365
    birthday_equality = round((1 - no_birthday_equality) * 100, 1)
    return birthday_equality
