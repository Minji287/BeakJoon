h, m = map(int, input().split())
t = int(input())

h = (t // 60) + h
m = (t % 60) + m

if(m >= 60):
    h = h + 1
    m = m - 60
if(h >= 24):
    h = h - 24

print(h, m)