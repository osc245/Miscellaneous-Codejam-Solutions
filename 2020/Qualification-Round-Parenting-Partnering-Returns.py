for case in range(1, int(input()) + 1):
    cEnd = jEnd = 0
    moves = int(input())
    table = ["-"]*moves
    activities = [[int(x) for x in input().split()] + [i] for i in range(moves)]
    activities.sort(key=lambda x: x[0])
    for activity in activities:
        start, end, index = activity
        if start >= cEnd:
            cEnd = end
            table[index] = "C"
        elif start >= jEnd:
            jEnd = end
            table[index] = "J"
        else:
            break
    ans = "IMPOSSIBLE" if "-" in table else "".join(table)
    print("Case #{}: {}".format(case, ans))
