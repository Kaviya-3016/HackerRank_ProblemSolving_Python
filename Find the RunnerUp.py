if __name__ == '__main__':
    n = int(input())
    arr=list(map(int, input().split()))
    arr.sort(reverse=True)
    if arr[0]>arr[1]:
        print(arr[1])
    elif arr[1]>arr[2]:
        print(arr[2])
    elif arr[2]>arr[3]:
        print(arr[3])
    elif arr[8]>arr[9]:
        print(arr[9])
    elif arr[3]>arr[4]:
        print(arr[4])
    
    



    