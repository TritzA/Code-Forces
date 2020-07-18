# https://codeforces.com/problemset/problem/4/A
p = int(input())


def separation(nb):
    if nb == 2:
        return "NO"
    if nb % 2 == 0:
        return "YES"
    return "NO"


print(separation(p))
