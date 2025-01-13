from functools import reduce
from operator import add
from typing import Any

def my_sum(*args) -> list[Any]:
    return reduce(add, list(args))
