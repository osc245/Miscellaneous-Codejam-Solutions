for case in range(1, int(input()) + 1):
    line = [int(x) for x in input().split()]
    ans = 0
    suprise, cutOff = line[1:3]
    for score in line[3:]:
        if score >= cutOff * 3 - 2 * min(1, cutOff):
            ans += 1
        elif score >= cutOff * 3 - 2 * min(2, cutOff) and suprise != 0:
            ans += 1
            suprise -= 1
    print('Case #{}: {}'.format(case, ans))
