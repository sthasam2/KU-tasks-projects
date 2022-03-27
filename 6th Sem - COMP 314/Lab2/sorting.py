"""Implementation of sorting algorithms: insertion and merge sort"""


# Insertion Sort


def insertion_sort(arr: list):
    """
    Sort array using Insertion sort algorithm
    """

    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1

        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value


# Merge Sort


def merge_sort(arr: list):
    """Recursively sort array using merge sort"""

    arr_size = len(arr)
    # return if array is empty or only single element
    if arr_size < 2:
        return

    # if array len is greater than 2, divide and sort
    mid = arr_size // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, arr)


def merge(left_arr: list, right_arr: list, arr: list):
    """Merge left and right array by comparing and sorting"""

    i = j = k = 0
    # loop until total elements of left and right
    size = len(left_arr) + len(right_arr)
    while k < size:
        # assign left arr element (left_arr[i])
        # if right arr has no elements left (j) to be extracted
        # OR if left arr has elements left for extraction and that element is < right arr element
        if j == len(right_arr) or (i < len(left_arr) and left_arr[i] < right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1


if __name__ == "__main__":
    arr = [5, 7, 2, 9, 6, 8, 11, 3]

    sample1 = [777, 69, 420]
    sample2 = [13, 7, 2022]
    combined = [0] * 6
    merge(sample1, sample2, combined)

    # insertion_sort(arr)
    # merge_sort(arr)
    print(arr)
