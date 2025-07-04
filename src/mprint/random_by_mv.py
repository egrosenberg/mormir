from random import randint
from .constants import DEFAULT_CARD


# ------------------------------------------------------------
# Filters inputted cards by mana value
# ------------------------------------------------------------
def filterByMv(cards, mv):
    # Filter function
    def filterFunction(card):
        return card["cmc"] == mv

    return list(filter(filterFunction, cards))


# ------------------------------------------------------------
# finds a random card with specified mana value from cards
# ------------------------------------------------------------
def randomByMv(cards, mv):
    filtered = filterByMv(cards, mv)
    count = len(filtered)
    if count == 0:
        print(f"NO CARDS FOUND AT MV {mv}")
        return DEFAULT_CARD
    return filtered[randint(0, count-1)]
