from typing import Optional
import operator

from src.common.types import Comparator, NumericArray



def merge(left: NumericArray, right: NumericArray, compare) -> NumericArray:
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if len(left) == i:
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    
    return result


def mergesort(L: NumericArray, compare: Optional[Comparator]=operator.lt) -> NumericArray:
    if len(L) < 2:
        return L[:]
    
    middle = int(len(L) / 2)
    left = mergesort(L[:middle], compare)
    right = mergesort(L[middle:], compare)
    
    return merge(left, right, compare)
