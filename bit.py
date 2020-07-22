# https://codeforces.com/problemset/problem/282/A
import sys
inp = sys.stdin.read().split('\n')
x = 0
for i in inp[1:]:
    if '++' in i:
        x += 1
    elif '--' in i:
        x -= 1
print(x)