import math


def g(x):
    for i in range((x)+1, 1, -1):
        if x % i == 0:
            if int(math.sqrt(i) + 0.5) ** 2 == i:
                return i
    return 1


def S(N):
    ans = 0
    for n in range(1, N+1):
        print(n)
        ans += g(n)
    return ans


print(f'ans is {S(10**14)}')