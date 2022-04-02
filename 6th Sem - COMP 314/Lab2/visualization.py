"""Time Complexity visualiztion for sorting algorithms"""

import time
import random

from matplotlib import pyplot as plt

from sorting import insertion_sort, merge_sort, merge_sort_internal


def generate_random_list(size):
    return [random.choice(range(size)) for i in range(size)]


# def calculate_time(func, *args, **kwargs):
#     """Function for calculating time"""

#     tic = time.time_ns()
#     func(*args, **kwargs)
#     toc = time.time_ns()

#     return toc - tic


def calculate_time(func):
    """Decorator function for calculating time"""

    def inner(*args, **kwargs):

        tic = time.time_ns()
        func(*args, **kwargs)
        toc = time.time_ns()

        return toc - tic

    return inner


@calculate_time
def calculate_time_insertion_sort(arr):
    return insertion_sort(arr)


@calculate_time
def calculate_time_merge_sort(arr):
    return merge_sort(arr)


@calculate_time
def calculate_time_merge_sort_internal(start, end, arr):
    return merge_sort_internal(start, end, arr)


if __name__ == "__main__":
    samples = [generate_random_list(i) for i in range(0, 1000, 10)]

    sample_sizes = []
    insertion_sort_times = []
    merge_sort_times = []
    merge_sort_new_times = []

    for sample in samples:
        sample_sizes.append(len(sample))
        insertion_sort_times.append(calculate_time_insertion_sort(sample))
        merge_sort_times.append(
            calculate_time_merge_sort_internal(0, len(sample) - 1, sample)
        )
        merge_sort_new_times.append(calculate_time_merge_sort(sample))

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.xlabel("Sample Size (n)")
    plt.ylabel("Time Elasped (ns)")

    # Insertion sort
    # plt.title("Time Complexity for Insertion sort")
    # plt.plot(sample_sizes, insertion_sort_times, ".-", label="Insertion Sort")

    # Merge Sort
    # plt.title("Time Complexity for Merge sort")
    # plt.plot(sample_sizes, merge_sort_times, ".-", label="Merge Sort")

    # Merge Sort 2
    # plt.title("Time Complexity for Merge sort")
    # plt.plot(sample_sizes, merge_sort_new_times, ".-", label="Merge Sort type 2")

    # Insertion vs Merge vs Merge (second algo)
    plt.title("Time Complexity: Insertion sort vs Merge Sort")
    plt.plot(sample_sizes, insertion_sort_times, ",-", label="Insertion Sort")
    plt.plot(sample_sizes, merge_sort_times, ",-", label="Merge Sort")
    plt.plot(sample_sizes, merge_sort_new_times, ",-", label="Merge Sort Type 2")

    plt.legend()
    plt.show()
    print("done")
