# Read the number of elements in the first set
M = int(input())              

# Read M space-separated integers, convert them to a set (removes duplicates)
myset = set(map(int, input().split()))
# Example: if input = "1 2 2 3", myset = {1, 2, 3}

# Read the number of elements in the second set
N = int(input())              

# Read N space-separated integers, convert them to a set
myset1 = set(map(int, input().split()))
# Example: if input = "3 4 5", myset1 = {3, 4, 5}

# Difference operation: elements present in myset but NOT in myset1
students = myset.difference(myset1)
# Example: {1, 2, 3} - {3, 4, 5} = {1, 2}

# Print the number of such elements
print(len(students))
