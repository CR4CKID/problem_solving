'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

# 1
def find_prime(n):
    num = []
    for div in range(2,n):
        if n % div == 0:
            num.append(div)
            n = n / div
        
        if n == 1 or div > n:
            print(max(num))
            break

        
find_prime(600851475143)


# 2
from math import sqrt

primes = set([2])
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print (value)
            number /= value
print (number)

# 3
roots = []; product = 1; x = 2; y = 13195
while product != y:
	while (y % x == 0):
		roots.append(x)
		y /= x
		product *= roots[-1]
	x += 1
print (roots)