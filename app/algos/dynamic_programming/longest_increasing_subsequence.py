def _lis(arr, n):
    """
    Recursive helper function to find the length of the Longest Increasing Subsequence (LIS).

    Args:
        arr (list[int]): The input list of integers.
        n (int): The current index of the element being considered.

    Returns:
        int: The length of the LIS ending at the current index.
    """
    global maximum

    # Base Case: If there is only one element, the LIS length is 1.
    if n == 1:
        return 1

    # Initialize the maximum LIS ending at the current index as 1.
    maxEndingHere = 1

    # Check all elements before the current index to find a subsequence with increasing order.
    for i in range(1, n):
        # Recursively find the length of LIS ending at index 'i'.
        res = _lis(arr, i)

        # If the current element is greater than the element at index 'i'
        # and the length of LIS ending at 'i' plus 1 is greater than the current maximum LIS,
        # update the maximum LIS ending at the current index.
        if arr[i-1] < arr[n-1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Update the global maximum LIS with the maximum LIS ending at the current index.
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    """
    Function to find the length of the Longest Increasing Subsequence (LIS) in the given list.

    Args:
        arr (list[int]): The input list of integers.

    Returns:
        int: The length of the Longest Increasing Subsequence (LIS).
    """
    global maximum

    n = len(arr)

    # Initialize the global maximum LIS as 1 (minimum length is 1).
    maximum = 1

    # Call the recursive helper function to find the maximum LIS.
    _lis(arr, n)

    # Return the maximum LIS as the final output.
    return maximum


def main():
    # Example input list
    arr = [10, 22, 9, 33, 21, 50, 41, 60]

    # Find the length of the Longest Increasing Subsequence (LIS).
    output = "Length of LIS is " + str(lis(arr))

    return output
