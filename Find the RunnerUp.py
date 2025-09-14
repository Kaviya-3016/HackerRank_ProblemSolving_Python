if __name__ == '__main__':
    n = int(input())  
    # read number of elements (but here n is not really used)

    arr = list(map(int, input().split()))  
    # read n numbers, split them by space, convert each to int
    # example input: 2 3 6 6 5
    # arr = [2, 3, 6, 6, 5]

    arr.sort(reverse=True)  
    # sort in descending order
    # arr = [6, 6, 5, 3, 2]

    if arr[0] > arr[1]:
        print(arr[1])
        # if the largest is greater than the second largest,
        # then print second largest
        # problem: if arr[0] == arr[1], it skips this

    elif arr[1] > arr[2]:
        print(arr[2])
        # if second is greater than third, print third
        # example: arr[1] = 6, arr[2] = 5 → this will print 5

    elif arr[2] > arr[3]:
        print(arr[3])
        # continues checking next numbers

    elif arr[8] > arr[9]:
        print(arr[9])
        

    elif arr[3] > arr[4]:
        print(arr[4])
        # similar issue — manually checking, not scalable
