'''2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?'''
import time
s = time.time()

# 1
def prime(n):
    prime_list = [2]
    i = 3
    grid_list = [0] * (n+1)
    while i <= n:
        if grid_list[i] == 0:
            mul_num = i
            prime_list.append(i)
            while mul_num <= n:
                grid_list[mul_num] = 1
                mul_num += i
        i += 2
    return prime_list

def multiple(n):
    prime_list = prime(n)
    final_list = [0] * len(prime_list)
    i = 2
    while i <= n:
        multi_list = [0] * len(prime_list)
        for num in prime_list:
            ind = prime_list.index(num)
            div = i
            while div % num == 0:
                div /= num
                multi_list[ind] += 1
        i += 1
        a = 0
        while a < len(prime_list):
            if multi_list[a] > final_list[a]:
                final_list[a] = multi_list[a]
            a += 1
    from functools import reduce
    final_nums = [x ** y for x , y in zip(prime_list, final_list)]
    print(reduce(lambda x , y : x * y, final_nums ))
multiple(2000)

# 2 
def multiple2(n):
    i = 1
    for k in (range(1, n+1)):
        if i % k > 0:
            for j in range(1, n+1):
                if (i*j) % k == 0:
                    i *= j
                    break
    print (i)
multiple2(49)


print(time.time() - s)