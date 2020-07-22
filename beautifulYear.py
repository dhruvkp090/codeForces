# https://codeforces.com/problemset/problem/271/A
inp = int(input())
for i in range(inp + 1, 10000 ):
    strI = str(i)
    distinct = 1
    for j in range(4):
        if strI[j] in strI[j+1:]:
            distinct = 0
            break
    if distinct == 1:
        print(i)
        break
