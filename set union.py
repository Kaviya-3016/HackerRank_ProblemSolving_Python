# Read the number of elements in the first set
M = int(input())              

# Read M space-separated integers, convert them to a set (to remove duplicates automatically)
myset = set(map(int, input().split()))
# Example: if input = "1 2 2 3", myset = {1, 2, 3}

# Read the number of elements in the second set
N = int(input())              

# Read N space-separated integers, convert them to a set
myset1 = set(map(int, input().split()))
# Example: if input = "3 4 5", myset1 = {3, 4, 5}

# Union operation: combines both sets, keeping only unique values
students = myset.union(myset1)
# Example: {1, 2, 3} U {3, 4, 5} = {1, 2, 3, 4, 5}

# Print the number of unique elements in the union set
print(len(students))
# Output will be the count of unique elements across both sets
