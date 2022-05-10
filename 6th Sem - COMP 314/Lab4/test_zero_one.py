from zero_one_knapsack import ZeroOneKnapsack


test_items = [
    dict(
        input=(16, [4, 6, 8, 10], [2, 4, 10, 12]),
        expected=([0, 1, 0, 1], 16),
    ),
    dict(
        input=(22, [6, 8, 10, 18, 8], [6, 8, 8, 20, 8]),
        expected=([1, 1, 0, 0, 1], 22),
    ),
    dict(
        input=(28, [24, 4, 2, 2, 8], [8, 4, 2, 4, 20]),
        expected=([0, 1, 1, 1, 1], 30),
    ),
]


def test_bruteforce():
    for item in test_items:
        zero_one = ZeroOneKnapsack(*item["input"])
        actual = zero_one.bruteforce()
        assert actual == item["expected"]


def test_dynamic():
    for item in test_items:
        zero_one = ZeroOneKnapsack(*item["input"])
        actual = zero_one.dynamic()
        assert actual == item["expected"]
