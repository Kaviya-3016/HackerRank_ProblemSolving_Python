# Read the number of elements in the first set
M = int(input())              

# Read M space-separated integers, convert them into a set (duplicates removed)
myset = set(map(int, input().split()))
# Example: if input = "1 2 2 3", then myset = {1, 2, 3}

# Read the number of elements in the second set
N = int(input())              

# Read N space-separated integers, convert them into a set
myset1 = set(map(int, input().split()))
# Example: if input = "3 4 5", then myset1 = {3, 4, 5}

# Intersection: elements that are common to both sets
students = myset.intersection(myset1)
# Example: {1, 2, 3} ∩ {3, 4, 5} = {3}

# Print the number of elements in the intersection set
print(len(students))
