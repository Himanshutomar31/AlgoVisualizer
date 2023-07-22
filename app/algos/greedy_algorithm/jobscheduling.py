# Function to perform Job Scheduling using the Greedy Algorithm
def printJobScheduling(arr, t):
    # Sort the jobs in non-increasing order of their profits (third element of each job)
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Initialize arrays to keep track of the schedule and selected jobs
    result = [False] * t
    job = ['-1'] * t

    # List to store the sequence of jobs for maximum profit
    max_profit_sequence = []

    # Iterate through the sorted jobs and assign them to time slots
    for i in range(len(arr)):
        # Search for a free time slot starting from the job's deadline
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # If a free slot is found, assign the job to that slot
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                max_profit_sequence.append(arr[i][0])
                break

    # Return the sequence of jobs for maximum profit
    return max_profit_sequence 

def main():
    # Example job list: [Job ID, Deadline, Profit]
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    # Call the Job Scheduling function
    max_profit_sequence = printJobScheduling(arr, 3)

    # Check if the sequence is empty or not
    if not max_profit_sequence:
        print("No jobs scheduled.")
    else:
        # Print the header and the sequence of jobs for maximum profit
        print("Following is the maximum profit sequence of jobs:")
        print(max_profit_sequence)

# if __name__ == "__main__":
#     main()
