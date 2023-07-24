def knapsack(wt, val, W, n, t):
    """
    Function to calculate the maximum profit that can be obtained from the given items using the Knapsack problem.

    Args:
        wt (list[int]): List of item weights.
        val (list[int]): List of item values (profits).
        W (int): Maximum capacity of the knapsack.
        n (int): Number of items available.
        t (list[list[int]]): 2D list to store previously computed results for memoization.

    Returns:
        int: Maximum profit that can be obtained from the given items using the Knapsack problem.
    """
    # Base case: If there are no items or the knapsack has no capacity, the profit is 0.
    if n == 0 or W == 0:
        return 0

    # If the result for the current subproblem is already computed, return it from the memoization table 't'.
    if t[n][W] != -1:
        return t[n][W]

    # If the weight of the current item is less than or equal to the remaining capacity of the knapsack,
    # we have two choices: either include the current item or exclude it.
    if wt[n - 1] <= W:
        # Calculate the maximum profit by including the current item or excluding it.
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1, t),  # Include the current item
            knapsack(wt, val, W, n - 1, t),  # Exclude the current item
        )
        return t[n][W]
    else:
        # If the weight of the current item exceeds the remaining capacity of the knapsack,
        # we can only exclude the current item.
        t[n][W] = knapsack(wt, val, W, n - 1, t)
        return t[n][W]


def main():
    # Example input
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)

    # Initialize a memoization table 't' with all values set to -1
    # to store previously computed results for memoization.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # Call the knapsack function to calculate the maximum profit that can be obtained.
    return knapsack(weight, profit, W, n, t)
