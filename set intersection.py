# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())              
myset = set(map(int, input().split()))
#print(myset)
N = int(input())              
myset1 = set(map(int, input().split()))
#print(myset1)
students=myset.intersection(myset1)
print(len(students))