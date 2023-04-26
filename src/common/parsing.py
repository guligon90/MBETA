from typing import Optional

from src.common.types import NumericArray


def join(A: NumericArray, separator: Optional[str]=',') -> str:
    return separator.join([str(v) for v in A])
