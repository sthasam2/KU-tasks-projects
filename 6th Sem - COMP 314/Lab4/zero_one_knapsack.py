class ZeroOneKnapsack:
    capacity = None
    weight_list = None
    profit_list = None
    solution_set = None
    solution = None

    def __init__(self, capacity, weight_list, profit_list):
        self.capacity = capacity
        self.weight_list = weight_list
        self.profit_list = profit_list
        self._check_weight_profit_len()

    def _check_weight_profit_len(self):
        """
        Check whether profit and weights have same length
        i.e. one profit corresponds to on weight
        """

        assert len(self.profit_list) == len(
            self.weight_list
        ), "profit_list and weight_list must have the same length"

    def bruteforce(self):
        """0/1 knapsack problem using bruteforce approach."""

        w = self.weight_list
        p = self.profit_list
        capacity = self.capacity

        max_profit = 0
        n = len(w)
        solution_set = [list(map(int, bin(x)[2:].rjust(n, "0"))) for x in range(2**n)]

        for entry in solution_set:
            weight = 0
            profit = 0
            for idx, value in enumerate(entry):
                weight += w[idx] * value
                profit += p[idx] * value

            if weight <= capacity and profit > max_profit:
                max_profit = profit
                solution = entry

        return solution, max_profit

    def dynamic(self):
        """0/1 knapsack problem using dynamic programming."""

        w = self.weight_list
        p = self.profit_list
        capacity = self.capacity

        n = len(w)
        knapsack_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if j - w[i - 1] < 0:
                    knapsack_table[i][j] = knapsack_table[i - 1][j]
                else:
                    knapsack_table[i][j] = max(
                        knapsack_table[i - 1][j],
                        knapsack_table[i - 1][j - w[i - 1]] + p[i - 1],
                    )

        max_profit = knapsack_table[n][capacity]
        row = n
        col = capacity
        solution = [0] * n

        # Traverse the knapsack_table from bottom to top to find the solution set.
        while row > 0 and col > 0:
            if knapsack_table[row][col] != knapsack_table[row - 1][col]:
                solution[row - 1] = 1
                col -= w[n - 1]
            row -= 1

        return solution, max_profit
