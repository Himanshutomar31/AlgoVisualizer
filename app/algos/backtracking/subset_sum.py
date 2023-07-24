from typing import List


def generate_sum_of_subsets_soln(nums: List[int], max_sum: int) -> List[List[int]]:
    # Initialize an empty list to store the result
    result: List[List[int]] = []
    # Initialize an empty list to keep track of the current path
    path: List[int] = []
    # Start exploring the state space from the first number (index 0)
    num_index = 0
    # Calculate the sum of all numbers in the 'nums' list
    remaining_nums_sum = sum(nums)
    # Start creating the state space tree
    create_state_space_tree(nums, max_sum, num_index,
                            path, result, remaining_nums_sum)
    # Return the list of subsets that add up to the target sum
    return result


def create_state_space_tree(
    nums: List[int],
    max_sum: int,
    num_index: int,
    path: List[int],
    result: List[List[int]],
    remaining_nums_sum: int,
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    It terminates the branching of a node when any of the two conditions
    given below satisfy.
    This algorithm follows depth-first search and backtracks when the node is not branchable.

    Args:
        nums: The list of numbers from which subsets are generated.
        max_sum: The target sum for subsets.
        num_index: The current index in the 'nums' list.
        path: The current path (subset) being explored.
        result: The final list to store all subsets that add up to the target sum.
        remaining_nums_sum: The sum of the numbers remaining in the 'nums' list.
    """
    # If the current path sum exceeds the target sum or adding all remaining numbers
    # still does not reach the target sum, terminate the branch.
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return

    # If the current path sum equals the target sum, add the path to the result list.
    if sum(path) == max_sum:
        result.append(path)
        return

    # Explore the state space tree by recursively considering the next numbers in 'nums'.
    # Start the loop from the current index to avoid duplicate subsets.
    for index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            index + 1,  # Move to the next index to avoid using the same number again
            path + [nums[index]],  # Add the current number to the path
            result,
            remaining_nums_sum - nums[index],  # Update the remaining sum
        )


def main() -> List[List[int]]:
    # Example input
    nums = [3, 34, 4, 12, 5, 2]
    max_sum = 9
    # Call the function to generate subsets that add up to the target sum
    return generate_sum_of_subsets_soln(nums, max_sum)


if __name__ == "__main__":
    # Print the subsets that add up to the target sum
    print(main())
