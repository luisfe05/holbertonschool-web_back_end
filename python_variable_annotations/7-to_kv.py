#!/usr/bin/env python3
"""Module that provides a type-annotated key/value tuple function."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple pairing a string key with the square of a number."""
    return (k, v ** 2)
