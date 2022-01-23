s = "GATATATGCATATACTT"
t = "ATAT"

answer = []
start_idx = 0

try:
    while True:
        idx = s.index(t, start_idx)
        answer.append(idx + 1)
        start_idx = idx + 1
except:
    print(" ".join(map(str, answer)))

