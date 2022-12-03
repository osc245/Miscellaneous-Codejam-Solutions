for case in range(1, int(input()) + 1):
    maxLevel, people = input().split()
    crowd = [int(n) for n in people]
    count = extra = 0
    for i in range(0, int(maxLevel) + 1):
        extra += max(0, i - count)
        count += max(0, i - count) + crowd[i]
    print('Case #{}: {}'.format(case, extra))
