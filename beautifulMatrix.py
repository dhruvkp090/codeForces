# https://codeforces.com/problemset/problem/263/A
import sys
u = sys.stdin.read().split('\n')
mat = []
for line in u:
    mat.append([int(x) for x in line.split()])
i1 = -1
j1 = -1
for x in mat:
    i1 += 1
    if 1 in x:
        j1 = x.index(1)
        break
moves = abs(i1 - 2) + abs(j1 - 2)
print(moves)
