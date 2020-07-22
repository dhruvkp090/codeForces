# https://codeforces.com/problemset/problem/59/A
word = input()
small = 'abcdefghijklmnopqrstuvwxyz'
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numSmall = 0
numCap = 0
out = ''
wordLen = len(word)
for w in word:
    if w in small:
        numSmall += 1
    elif w in cap:
        numCap += 1
if numCap > numSmall:
    for w in word:
        if w in small:
            out += cap[small.index(w)]
        else:
            out += w
else:
    for w in word:
        if w in cap:
            out += small[cap.index(w)]
        else:
            out += w
print(out)