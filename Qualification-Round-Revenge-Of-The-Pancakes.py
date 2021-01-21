# currently incomplete

for case in range(1, int(input()) + 1):
    ans = 0
    pancakes = [p == "+" for p in list(input())]
    for i in range(len(pancakes) - 1, -1, -1):
        if not pancakes[i]:
            pancakes[0:i] = [not b for b in reversed(pancakes[0:i])]
            ans += 1
            print(pancakes)
    print("Case #{}: {}".format(case, ans))
