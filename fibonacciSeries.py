print("Printing Fibonacci series in Python!")
a, b = 0, 1
i = 3
limit = int(input("Specify the limit: "))
while i <= limit+2:
    print(a)
    a, b = b, a+b
    i = i + 1
print("Finished printing Fibonacci series in Python!")
