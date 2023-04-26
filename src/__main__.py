from src.common import join
from src.problems.one.magic_drawer import get_coin_count
from src.problems.two.algorithm.sorting import mergesort


def problem_one() -> None:
    transactions = [1, -1, 2, 0, 4]
    total_coins = get_coin_count(transactions)

    print(f"Transactions: {join(transactions)}\t Total coins on the {len(transactions)}th day: {total_coins}")


def problem_two() -> None:
    A = [2, 4, 1, 6, 8, 5, 3, 7]
    B = [7, 3, 2, 16, 24, 4, 11, 9]

    ord_A = mergesort(A)
    ord_B = mergesort(B)

    print(f'A = {join(A)}\t Ordered A = {join(ord_A)}')
    print(f'B = {join(B)}\t Ordered B = {join(ord_B)}')


if __name__ == '__main__':
    try:
        problem_one()
        # problem_two()
    except KeyboardInterrupt:
        SystemExit(0)
    except Exception as exc:
        print(f'{exc.__class__.__name__}: {str(exc)}')
