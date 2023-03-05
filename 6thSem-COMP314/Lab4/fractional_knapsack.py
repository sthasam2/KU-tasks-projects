class FractionalKnapsack:

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
        """Fractional knapsack problem using bruteforce approach."""

        w = self.weight_list
        p = self.profit_list
        cap = self.capacity

        n = len(w)
        max_profit = 0
        max_weight = 0
        solution = None

        solution_set = [list(map(int, bin(x)[2:].rjust(n, "0"))) for x in range(2**n)]

        for entry in solution_set:
            weight = 0
            profit = 0
            for idx, value in enumerate(entry):
                weight += w[idx] * value
                profit += p[idx] * value

            if weight <= cap and profit > max_profit:
                max_profit = profit
                solution = entry
                max_weight = weight

        remaining_capacity = cap - max_weight

        max_fractional_profit = 0
        for idx, weight in enumerate(w):
            if remaining_capacity > 0 and solution[idx] == 0:
                ratio = round(remaining_capacity / weight, 2)
                fractional_profit = ratio * p[idx]
                if fractional_profit > max_fractional_profit:
                    max_fractional_profit = fractional_profit
                    solution[idx] = ratio

        return solution, max_profit + max_fractional_profit

    def greedy(self):
        """Using Greedy approach to solve Fractional knapsack"""

        w = self.weight_list
        p = self.profit_list
        cap = self.capacity

        max_profit = 0
        remaining_capacity = cap
        solution = [0] * len(w)

        profit_per_weight = [profit / weight for (profit, weight) in zip(p, w)]

        while remaining_capacity != 0:
            max_idx = 0
            for index, value in enumerate(profit_per_weight):
                if value > profit_per_weight[max_idx]:
                    max_idx = index
            profit_per_weight[max_idx] = 0

            if w[max_idx] <= remaining_capacity:
                solution[max_idx] = 1
                max_profit += p[max_idx]
                remaining_capacity -= w[max_idx]
            else:
                frac = round(remaining_capacity / w[max_idx], 2)
                solution[max_idx] = frac
                max_profit += frac * p[max_idx]
                remaining_capacity = 0

        return solution, max_profit
