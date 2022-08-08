import math


def D(N=2022):
    ans = 19
    for i in range(3, N+1):
        print(i)
        for j in range((i//2)+1, i+1):
            if i == j:
                ans += 9
            else:
                ans += ((10*9**(i-j)*math.comb(i, j)) - (9**(i-j)*math.comb(i-1, j-1)) - (9*9**(i-j-1)*math.comb(i-1, i-j-1)))

    return ans

print(D(2022) % 1000000007)