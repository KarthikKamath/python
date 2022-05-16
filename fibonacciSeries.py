def printFibonacciSeries(limit=11):
    print("Printing Fibonacci series in Python till limit", limit)
    a, b = 0, 1
    i = 3
    while i <= limit + 2:
        print(a)
        a, b = b, a + b
        i = i + 1
    print("Finished printing Fibonacci series in Python!")


printFibonacciSeries()
#
# l = int(input("Specify the limit length of Fibonacci series: "))
# printFibonacciSeries(l)
