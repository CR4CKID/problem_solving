n = input()
nums = list(map(int, input().split(" ")))

arr = sorted(set((nums)))
num_dict = {n: i for i, n in enumerate(arr)}

print(" ".join([str(num_dict[num]) for num in nums]))
