def factorial(n: int) -> int:
    """
    Function to compute the factorial of a non-negative integer n.

    Args:
        n (int): The non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of the input integer n.
    """

    # Base Case: If n is 0 or 1, the factorial is 1.
    if n <= 1:
        return 1
    else:
        # Recursive Case: Compute the factorial of (n-1) and multiply it with n.
        return n * factorial(n - 1)


def main() -> int:
    """
    Main function to compute the factorial of the number 5.

    Returns:
        int: The factorial of the number 5.
    """
    return factorial(5)
