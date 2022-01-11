'''A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

# 1
num = []
for a in range(100,1000):
    for b in range(100,1000):
        if a * b == int(str(a * b) [::-1]):
            num.append(a * b)

print(max(num))