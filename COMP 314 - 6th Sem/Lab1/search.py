def linear_search(values: list, target: int) -> int:
    """Linear Search Implementation"""

    for key, value in enumerate(values):
        if value == target:
            return key

    return -1


def binary_search(values: list, target: int) -> int:
    """Binary search implementation"""

    low = 0
    high = values.__len__() - 1

    while high >= low:
        mid = (high + low) // 2
        if values[mid] == target:
            return mid
        if target > values[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [5, 4, 9, 8, 11, 2, 6]
    print(linear_search(arr, 9))
    arr.sort()
    print(binary_search(arr, 9))
