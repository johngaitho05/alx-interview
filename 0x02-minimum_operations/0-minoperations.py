"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    if n == 1:
        return 0

    # Initialize an array to store the minimum number of operations for each position
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize the minimum number of operations for the current position as the maximum possible value
        dp[i] = float('inf')

        # Iterate through all factors of i to find the optimal solution
        for j in range(1, i):
            if i % j == 0:
                # If j is a factor of i, it means we can copy and paste j times to reach i
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0

