# https://codeforces.com/problemset/problem/32/B
code = input()
out = ""
nextUsed = 0
for i,c in enumerate(code):
    if c == ".":
        if nextUsed == 1:
            nextUsed = 0
        else:
            out += "0"
    if c == "-":
        if i+1 != len(code):
            x = c + code[i+1]
        if nextUsed == 1:
            nextUsed = 0
        elif x == "-.":
            out += "1"
            nextUsed = 1
        elif x == "--":
            out += "2"
            nextUsed = 1
print(out)
