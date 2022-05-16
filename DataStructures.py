import fibonacciSeries as fs

# Stack
my_stack = ["a", "c", "d", "b"]
print(my_stack)
my_stack.append("e")
my_stack.append("f")
print(my_stack)
print("First element: ", my_stack[0])

my_stack.sort()
print(my_stack)

# FIFO
print("Pop Latest: ", my_stack.pop())
print(my_stack)

del my_stack[4]
print("After delete", my_stack)

print("===\n")
# List Comprehensions
squares = [x**2 for x in range(10)]
print("List Comprehensions\nSquares: ", squares)

# Tuples
t = "a", 2, 3, "Z"
print("===\n")
print("Tuples: ", t)
# del t[1] -- This is NOT allowed

# Sets
set1 = set(["a", "b", "b", "Z"])
set2 = {"a", "b", "b", "Z"}
print("===\n")
print("Set1: ", set1)
print("Set2: ", set2)

# Dictionaries
dic1 = {"a": 1, "b": 2, "c": 3}
print("===\n")
print("Dic1: ", dic1)
print("Dic1's b: ", dic1["b"])
dic2 = dict(sape=4139, guido=4127, jack=4098)
print("Dic2: ", dic2)

for (k, v) in dic1.items():
    print(k, v)

fs.printFibonacciSeries(5)

print("===\nFormatted String")
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
