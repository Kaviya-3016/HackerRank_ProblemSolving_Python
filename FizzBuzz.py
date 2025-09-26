def fizzBuzz(n):
    # Loop from 1 to n (inclusive)
    for i in range(1, n+1):

        # If number divisible by both 3 and 5 → print "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        # If number divisible by only 3 → print "Fizz"
        elif i % 3 == 0:
            print("Fizz")

        # If number divisible by only 5 → print "Buzz"
        elif i % 5 == 0:
            print("Buzz")

        # Otherwise, just print the number itself
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
