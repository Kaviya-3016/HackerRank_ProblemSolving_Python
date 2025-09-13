if __name__ == '__main__':
    # Take four integers as input
    x = int(input())   # maximum value for i
    y = int(input())   # maximum value for j
    z = int(input())   # maximum value for k
    n = int(input())   # condition value (sum to exclude)

    # Generate all possible coordinates [i, j, k]
    # where:
    #   0 <= i <= x
    #   0 <= j <= y
    #   0 <= k <= z
    # BUT only include those where (i + j + k) != n
    coordinates = [[i, j, k] 
                   for i in range(x + 1)     # loop i from 0 to x
                   for j in range(y + 1)     # loop j from 0 to y
                   for k in range(z + 1)     # loop k from 0 to z
                   if (i + j + k) != n]      # condition to exclude sum == n

    # Print the final list of coordinates
    print(coordinates)
