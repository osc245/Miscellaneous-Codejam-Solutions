for case in range(1, int(input()) + 1):
    cost, extra, finish = [float(n) for n in input().split()]
    curr, time = 2, 0
    while finish / curr >= cost/curr + finish / (curr + extra):
        time += cost / curr
        curr += extra
    time += finish / curr
    print('Case #{}: {}'.format(case, time))
