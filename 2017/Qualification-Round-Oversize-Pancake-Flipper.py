for case in range(1, int(input()) + 1):
    line = input().split()
    pancakes, size = [s == "+" for s in line[0]], int(line[1])
    flips = 0
    for i in range(len(pancakes) - size + 1):
        if not pancakes[i]:
            flips += 1
            for j in range(i, i + size):
                pancakes[j] = not pancakes[j]
    ans = "IMPOSSIBLE" if not all(pancakes) else flips
    print("Case #{}: {}".format(case, ans))
