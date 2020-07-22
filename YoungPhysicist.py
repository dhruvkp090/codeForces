# https://codeforces.com/problemset/problem/69/A
import sys
x=y=z = 0
inp = sys.stdin.read().split("\n")
for i in range(1, int(inp[0]) + 1):
    c = [int(x) for x in inp[i].split()]
    x += c[0]
    y += c[1]
    z += c[2]
if x != 0 or y!=0 or z!=0:
    print('NO')
else:
    print('YES')