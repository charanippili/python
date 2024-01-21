# Input: Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input time 1 and time 2 as lists of integers
    time1 = list(map(int, input().split()))
    time2 = list(map(int, input().split()))
    c = int(input())  # Input the operation code

    # Calculate the total seconds based on the operation
    total_seconds = (sum(time1) + (1 if c == 1 else -1) * sum(time2)) % (24 * 3600)

    # Calculate new hours, minutes, and seconds
    new_hh, remainder = divmod(total_seconds, 3600)
    new_mm, new_ss = divmod(remainder, 60)

    # Print the result as hh:mm:ss
    print(new_hh, new_mm, new_ss)
