# https://codeforces.com/problemset/problem/281/A
word = input()
small = 'abcdefghijklmnopqrstuvwxyz'
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if word[0] in small:
    print(cap[small.index(word[0])] + word[1:])
else:
    print(word)