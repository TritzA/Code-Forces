# https://codeforces.com/problemset/problem/71/A
n = int(input())


def trop_long(mot):
    taille = len(mot)
    if taille > 10:
        return mot[0] + str(taille - 2) + mot[-1]
    return mot


for _ in range(n):
    print(trop_long(input()))
