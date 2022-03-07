height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

ans = 0


def find_bigger(num):
    for i, h in enumerate(height):
        if h >= num:
            return i


while height:
    n = height.pop(0)
    if find_bigger(n):
        end = find_bigger(n)
        ans += sum(map(lambda x: min(n, height[end]) - x, height[:end]))
        height = height[end - 1 :]
    height = height[1:]

print(ans)
