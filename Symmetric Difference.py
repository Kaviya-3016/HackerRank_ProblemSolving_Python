M = int(input())              # size of first set (not really needed)
myset = set(map(int, input().split()))

N = int(input())              # size of second set (not really needed)
myset1 = set(map(int, input().split()))

# symmetric difference (elements in either set but not both)
result = sorted(myset.difference(myset1).union(myset1.difference(myset)))

for i in result:
    print(i)
