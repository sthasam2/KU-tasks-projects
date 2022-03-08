import time

from matplotlib import pyplot as plt

from search import binary_search, linear_search


def generate_list(entries: int) -> list:
    """Using simple for loop and range to define lists"""
    return [i for i in range(0, entries)]


def calculate_time(func):
    def inner(*args, **kwargs):

        tic = time.time_ns()
        return_item = func(*args, **kwargs)
        toc = time.time_ns()

        return return_item, toc - tic, len(args[0])

    return inner


def prepare_data_for_plot(times):
    """"""
    return dict(
        best=dict(x=[i[2] for i in times["best"]], y=[i[1] for i in times["best"]]),
        worst=dict(x=[i[2] for i in times["worst"]], y=[i[1] for i in times["worst"]]),
    )


@calculate_time
def check_time_binary(values, target) -> list:
    """
    Check the time taken by binary search
    Returns (list) 0: Found index, 1: Time Taken, 2: No. of items
    """
    return binary_search(values, target)


@calculate_time
def check_time_linear(values, target) -> list:
    """
    Check the time taken by linear search
    Returns (list) 0: Found index, 1: Time Taken, 2: No. of items
    """
    return linear_search(values, target)


if __name__ == "__main__":

    final = [
        generate_list(100),
        generate_list(500),
        generate_list(1000),
        generate_list(5000),
        generate_list(10000),
        generate_list(50000),
        generate_list(100000),
        generate_list(500000),
        generate_list(1000000),
        generate_list(5000000),
        generate_list(10000000),
    ]

    check_time_binary(
        [1, 2, 3], 1
    )  # initialize time checker for binary search to cache in memory
    check_time_linear(
        [1, 2, 3], 1
    )  # initialize time checker for linear search to cache in memory

    binary_times = dict(best=[], worst=[])
    linear_times = dict(best=[], worst=[])

    for i in final:
        # chekcing times for list of arrays in final

        b_worst = check_time_binary(i, -1)  # searching -1 in list i, -1 not present
        b_best = check_time_binary(i, i[(len(i) - 1) // 2])  # searching the mid element
        l_worst = check_time_linear(i, -1)  # searching -1 in list i, -1 not present
        l_best = check_time_linear(i, i[0])  # searching item at index 0

        # adding obtained time into prepared variables
        binary_times["best"].append([b_best[0], b_best[1], b_best[2]])
        binary_times["worst"].append([b_worst[0], b_worst[1], b_worst[2]])
        linear_times["best"].append([l_best[0], l_best[1], l_best[2]])
        linear_times["worst"].append([l_worst[0], l_worst[1], l_worst[2]])

    # Plot
    plt.figure(figsize=(10, 6))

    # LINEAR
    linear = prepare_data_for_plot(linear_times)
    # plt.plot(linear["best"]["x"], linear["best"]["y"], ".-", label="Best case")
    # plt.plot(linear["worst"]["x"], linear["worst"]["y"], ".-", label="Worst case")
    # plt.title("Linear Search: Best vs Worst Case Time Complexity")

    # BINARY
    binary = prepare_data_for_plot(binary_times)
    # plt.plot(binary["best"]["x"], binary["best"]["y"], ".-", label="Best case")
    # plt.plot(binary["worst"]["x"], binary["worst"]["y"], ".-", label="Worst case")
    # plt.title("Binary Search: Best vs Worst Case Time Complexity")

    # LINEAR VS BINARY
    plt.plot(linear["worst"]["x"], linear["worst"]["y"], ".-", label="Linear Search")
    plt.plot(binary["worst"]["x"], binary["worst"]["y"], ".-", label="Binary Search")
    plt.title("Binary Search vs Linear Search: Worst Case")

    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ns)")
    plt.legend()
    plt.show()
    print("Done")
