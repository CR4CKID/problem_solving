fin = []
for i1 in range(1, 4):
    ans = []
    ans.append(i1)
    for i2 in range(1, 4):
        if i2 in ans:
            continue
        else:
            ans.append(i2)
            for i3 in range(1, 4):
                if i3 in ans:
                    continue
                else:
                    ans.append(i3)
                    fin.append(ans)

print(fin)
