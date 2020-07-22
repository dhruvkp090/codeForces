# https://codeforces.com/problemset/problem/275/A
import sys
u = sys.stdin.read().split('\n')
arr = []
light = [[1,1,1], [1,1,1], [1,1,1]]
for line in u:
    c = []
    for x in line.split():
        if int(x) %2 == 0:
            c.append(0)
        else:
            c.append(1)
    arr.append(c)
for i,row in enumerate(arr):
    for j,a in enumerate(row):
        if a == 1:
            if light[i][j] == 1:
                light[i][j] = 0
            else:
                light[i][j] = 1
            if i+1 != 3:
                if light[i + 1][j] == 1:
                    light[i +1][j] = 0
                else:
                    light[i+1][j] = 1
            if i-1 != -1:
                if light[i-1][j] == 1:
                    light[i-1][j] = 0
                else:
                    light[i-1][j] = 1
            if j-1 != -1:
                if light[i][j-1] == 1:
                    light[i][j-1] = 0
                else:
                    light[i][j-1] = 1
            if j+1 != 3:
                if light[i][j+1] == 1:
                    light[i][j+1] = 0
                else:
                    light[i][j+1] = 1

for li in light:
    c = ""
    for a in li:
        c += str(a)
    print(c)