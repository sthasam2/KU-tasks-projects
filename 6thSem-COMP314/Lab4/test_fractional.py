import pytest
from fractional_knapsack import FractionalKnapsack


test_items = [
    dict(
        input=(20, [18, 15, 10], [25, 24, 15]),
        expected=([0, 1, 0.5], 31.5),
    ),
    dict(
        input=(60, [40, 10, 20, 24], [280, 100, 120, 120]),
        expected=([1, 1, 0.5, 0], 440.0),
    ),
    dict(
        input=(15, [2, 3, 5, 7, 1, 4, 1], [10, 5, 15, 7, 6, 18, 3]),
        expected=([1, 0.67, 1, 0, 1, 1, 1], 55.33),
    ),
]


def test_greedy():
    for item in test_items:
        fractional = FractionalKnapsack(*item["input"])
        result = fractional.greedy()
        assert pytest.approx(result, rel=1e-2) == item["expected"]


test_items2 = [
    dict(
        input=(20, [18, 15, 10], [25, 24, 15]),
        expected=([1, 0.13, 0], 28.2),
    ),
    dict(
        input=(60, [40, 10, 20, 24], [280, 100, 120, 120]),
        expected=([1, 0, 1, 0], 400),
    ),
    dict(
        input=(15, [2, 3, 5, 7, 1, 4, 1], [10, 5, 15, 7, 6, 18, 3]),
        expected=([1, 1, 1, 0, 1, 1, 0], 54),
    ),
]


def test_bruteforce():
    for item in test_items2:
        fractional = FractionalKnapsack(*item["input"])
        result = fractional.bruteforce()
        assert pytest.approx(result, rel=1e-2) == item["expected"]
