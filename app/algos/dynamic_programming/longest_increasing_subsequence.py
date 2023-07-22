global maximum


def _lis(arr, n):
    global maximum

    # Base Case
    if n == 1:
        return 1
    maxEndingHere = 1

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1

    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    global maximum

    # Length of arr
    n = len(arr)

    # Maximum variable holds the result
    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, n)
    return maximum


# Driver program to test the above function
def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(arr)

    # Function call
    output = "Length of lis is  " + str(lis(arr))
    return output
