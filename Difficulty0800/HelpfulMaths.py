# https://codeforces.com/problemset/problem/339/A
s = input()

s = s.split("+")
s.sort()

t = ""

for n in s:
    t += n + "+"

print(t[:-1])
