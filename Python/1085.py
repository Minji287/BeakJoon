# x, y, w, h = input().split(' ')
# d1 = int(w) - int(x)
# d2 = int(h) - int(y)
# print(min(int(x), int(y), d1, d2))

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))