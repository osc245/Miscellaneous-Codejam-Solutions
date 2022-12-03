for case in range(1, int(input()) + 1):
    input()
    m = [int(x) for x in input().split()]
    amounts = [m[i - 1] - m[i] for i in range(1, len(m)) if m[i] < m[i - 1]]
    first = sum(amounts)
    biggest = max(amounts) if amounts else 0
    second = sum(min(m[i], biggest) for i in range(len(m) - 1))
    print('Case #{}: {} {}'.format(case, first, second))
