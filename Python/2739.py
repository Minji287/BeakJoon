"""
n = input()
print(str(n) + " * 1 = " + str(1 * int(n)))
print(str(n) + " * 2 = " + str(2 * int(n)))
print(str(n) + " * 3 = " + str(3 * int(n)))
print(str(n) + " * 4 = " + str(4 * int(n)))
print(str(n) + " * 5 = " + str(5 * int(n)))
print(str(n) + " * 6 = " + str(6 * int(n)))
print(str(n) + " * 7 = " + str(7 * int(n)))
print(str(n) + " * 8 = " + str(8 * int(n)))
print(str(n) + " * 9 = " + str(9 * int(n)))
"""

n = int(input())
for i in range(1, 10):
    print(n, "*", i , "=", n * i)