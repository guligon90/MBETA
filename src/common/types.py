from typing import Callable, List, Union


Number = Union[int, float]
NumericArray = List[Number]
Comparator = Callable[[Number, Number], bool]
