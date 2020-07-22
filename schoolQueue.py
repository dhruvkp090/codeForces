# https://codeforces.com/problemset/problem/266/B
import sys
u = sys.stdin.read().split("\n")
t  = int(u[0].split()[1])
s = u[1]
newS = ""
for i in range(t):
    if newS != "":
        s = newS
    newS = ""
    switched = 0
    for j in range(len(s)):
        if s[j] == 'G':
            if switched == 1:
                newS += 'B'
                switched = 0
            else:
                newS += s[j]
        else:
            if(j+1 == len(s)):
                newS += s[j]
            else:
                if s[j+1] == 'G':
                    newS += 'G'
                    switched = 1
                else:
                    newS += s[j]
print(newS)