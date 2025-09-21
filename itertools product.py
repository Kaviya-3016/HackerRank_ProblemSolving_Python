# Importing product from itertools
# 'product' generates the Cartesian product of input iterables
from itertools import product

# Read first line of input (space-separated integers) and convert to a tuple
A = tuple(map(int, input().split()))

# Read second line of input (space-separated integers) and convert to a tuple
B = tuple(map(int, input().split()))

# Generate the Cartesian product of A and B
# Example: if A = (1, 2) and B = (3, 4), 
# product(A, B) → (1, 3), (1, 4), (2, 3), (2, 4)
iter = product(A, B)

# Print all pairs from Cartesian product in a single line
# '*' unpacks the iterable into separate elements
print(*iter)
