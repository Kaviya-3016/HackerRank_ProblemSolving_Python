# Enter your code here. Read input from STDIN. Print output to STDOUT

T=int(input())
for i in range(T):
    A=int(input())
    A_set= set(map(int, input().split()))
    B=int(input())
    B_set=set(map(int, input().split()))
    print(A_set.issubset(B_set))