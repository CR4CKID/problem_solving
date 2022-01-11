"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""
# 1
mul = set([])
for num in range(1,334):
    mul.add(num * 3)

for num in range(1,200):
    mul.add(num * 5)
    
print(sum(mul))

# 2
def multi(below):
    mul = set([])
    
    for m3 in range(1, below):
        if m3 * 3 < below:
            mul.add(m3 * 3)

    
    for m5 in range(1, below):
        if m5 * 5 < below:
            mul.add(m5 * 5)
    
    print(sum(mul))

multi(1000)

# 3
def multi(below):
    mul = set([])
    
    for m3 in range(0, below, 3):
        mul.add(m3)

    for m5 in range(0, below, 5):
        mul.add(m5)

    print(sum(mul))

multi(1000)

# 4
print(sum(set(range(0,1000,3))|set(range(0,1000,5))))