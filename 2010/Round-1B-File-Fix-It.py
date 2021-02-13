def findDirs(lineNum):
    unique = set()
    for i in range(lineNum):
        foo = ""
        for x in input()[1:].split("/"):
            foo += "/" + x
            unique.add(foo)
    return unique


for case in range(1, int(input()) + 1):
    n, m = [int(x) for x in input().split()]
    curr, new = findDirs(n), findDirs(m)
    ans = len(new - curr)
    print("Case #{}: {}".format(case, ans))
