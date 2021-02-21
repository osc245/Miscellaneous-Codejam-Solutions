for case in range(1, int(input()) + 1):
    input()
    x = []
    for i, value in enumerate(input().split()):
        if len(x) < int(value):
            x.extend(["" for _ in range(int(value) - len(x))])
        for j in range(int(value)):
            if len(x[j]) % 3 == 2:
                x[j] += " "
            x[j] += chr(ord("A") + i)
    ans = " ".join(x)[::-1]
    print("Case #{}: {}".format(case, ans))
