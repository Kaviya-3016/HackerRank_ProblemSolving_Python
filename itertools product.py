# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A=tuple(map(int, input().split()))
B=tuple(map(int, input().split()))
iter=product(A,B)
print(*iter)