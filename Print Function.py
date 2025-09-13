# This line checks if the file is being run directly
# (not imported as a module in another file).
if __name__ == '__main__':
    
    # Take an integer input from the user (e.g., 5).
    n = int(input())
    
    # Initialize i = 1 (though not really needed here, because
    # in the for loop, i will be reassigned).
    i = 1
    
    # Run a loop from 0 to n-1 (range(n) means: 0,1,2,...,n-1).
    for i in range(n):
        # Print i+1 (so it starts from 1 instead of 0).
        # end="" means print on the same line without spaces/newlines.
        print(i+1, end="")
