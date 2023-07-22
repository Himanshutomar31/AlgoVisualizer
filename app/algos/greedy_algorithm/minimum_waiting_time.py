def minimum_waiting_time(queries: list[int]) -> int:
    """
    This function takes a list of query times and returns the minimum waiting time
    for all queries to be completed.
    """

    # Get the number of queries
    n = len(queries)

    # If there is only one query or no queries, the waiting time is 0
    if n <= 1:
        return 0

    # Sort the queries in ascending order to minimize waiting time
    sorted_queries = sorted(queries)

    # Calculate the total waiting time by summing up the waiting time for each query
    total_waiting_time = sum(query * (n - i - 1) for i, query in enumerate(sorted_queries))

    # Return the minimum waiting time
    return total_waiting_time


def main() -> int:
    # Example usage: Calculate the minimum waiting time for the given list of queries
    return minimum_waiting_time([3, 2, 1, 2, 6])
