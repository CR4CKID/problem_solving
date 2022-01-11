'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''

import time
s = time.time()

# 1
def prime(n):
    from math import sqrt
    for div in range(2, int(sqrt(n)) + 1):
        if n % div == 0:
            return 0
    return 1

sum = 2
i = 3
while i < 2000000:
    if prime(i) == 1:
        sum += i
        i += 2
    else:
        i += 2

print(sum)

# 2
def P10(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]
print(P10(2000000))

# 3
def prime(n):
    marked = [0] * n
    value = 3
    sum = 2
    while value < n:
        if marked[value] == 0:
            sum += value
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2
    print (sum)

prime(2000000)


print(time.time() - s)
