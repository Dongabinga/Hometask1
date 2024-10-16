def gcd(*numbers):
    n = list(numbers)
    temp=0
    while len(n) > 1:
        while n[1]!=0:
            temp = n[0]
            n[0] = n[1]
            n[1] = temp % n[1]
        n.pop(1)
    return n[0]
print(gcd(36, 48, 156, 100500))