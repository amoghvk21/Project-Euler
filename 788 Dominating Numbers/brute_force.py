# N = 1: 10
# N = 2: 9
# N = 3: 271
# N = 4: 603
# N = 5: 8308
# N = 6: 19738

MAX = 999 # This is the max number that the for loop will check
ans = 0 # Answer
l = []

for n in range(0, (MAX+1)):
    digits = len(str(n))
    if str(n).count('0') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('1') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('2') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('3') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('4') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('5') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('6') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('7') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('8') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)
    if str(n).count('9') >= (digits//2)+1:
        ans += 1
        print(n)
        l.append(n)

print(f"answer is {ans}")
print(len(l))
l = set(l)

for x in l:
    if str(x)[0] == '0':
        print(x)
        break