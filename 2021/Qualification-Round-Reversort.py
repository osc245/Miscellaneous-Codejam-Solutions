for case in range(1, int(input()) + 1):
    input()
    elements = [int(x) for x in input().split()]
    ans = 0
    for i in range(len(elements) - 1):
        j = elements.index(min(elements[i:]))
        elements[i:j + 1] = elements[i:j + 1][::-1]
        ans += j - i + 1
    print("Case #{}: {}".format(case, ans))


