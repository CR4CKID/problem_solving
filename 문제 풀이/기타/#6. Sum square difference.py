# 1
def square(n):
    a = (n * (n+1) / 2) **2
    nums = []
    
    for num in range(1,n+1):
        nums.append(num ** 2)

    b = sum(nums)
    print(a-b)

square(100)

# 2
print(sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)]))