'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?'''
# 1
# def prime(n):
#     pri_list = []
#     pri_num = 2
#     while len(pri_list) != n:
#         for num in range(2,pri_num+1):
#             if pri_num == num:
#                 pri_list.append(pri_num)
#                 pri_num += 1
#             elif pri_num % num == 0:
#                 pri_num += 1
#                 break
    
#     print(pri_list[-1])
            
# prime(10001)

# 2
import time, math
s = time.time()
def IsPrime( n ):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0
	
	i = 3
	range = int( math.sqrt(n) ) + 1
	while( i < range ):
		if( n % i == 0):
			return 0
		i += 1
	return 1
N,T = 1,3
while N < 10001:
	if IsPrime(T):
		N+=1
	T+=2
print (T-2)
print (time.time() - s)