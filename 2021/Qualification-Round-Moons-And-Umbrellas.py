# only pasts first two test sets

for case in range(1, int(input()) + 1):
    line = input().split()
    cjPrice, jcPrice = int(line[0]), int(line[1])
    started = prevC = False
    ans = 0
    for elem in list(line[2]):
        if started and elem == "C":
            ans += (not prevC) * jcPrice
            prevC = True
        elif started and elem == "J":
            ans += prevC * cjPrice
            prevC = False
        elif not started and elem != "?":
            started = True
            if elem == "C":
                prevC = True
    print("Case #{}: {}".format(case, ans))
