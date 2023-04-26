from typing import Optional, Tuple

from src.common.types import NumericArray


def get_increments(trans_value: int, curr_count: int) -> Tuple[int, int]:
    """Apply the coin increment rules, given a transaction value and the current count."""

    def inc_lonely_coin(count: int) -> int:
        """If the drawer has only one coin, add another one"""
        return 1 if count == 1 else 0

    def inc_transaction(trans_value: int) -> int:
        """For each removed coin, another must disappear"""
        return 2*trans_value if trans_value < 0 else trans_value

    return inc_lonely_coin(curr_count), inc_transaction(trans_value)


def get_coin_count(transactions: NumericArray, count: Optional[int]=0):
    """Evaluates the count of all coin for a given sequence of transactions."""

    if len(transactions):
        increments = get_increments(transactions[0], count)

        # If the user is withdrawing more coins
        # than the drawer have store.
        # If so, sets the count to zero to avoid negative values
        updated_count = count + sum(increments) if count + sum(increments) > 0 else 0

        # Calls recursively get_coin_count, passing
        # Passing as sliced transaction array and the
        # updated count value
        return get_coin_count(transactions[1:], updated_count)
    else:
        return count if count > 0 else 0
