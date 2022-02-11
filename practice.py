arr = [1112, 695]

while max(arr) % min(arr) != 0:
    arr.append(max(arr) % min(arr))
    arr.pop(0)

print(arr[-1])

