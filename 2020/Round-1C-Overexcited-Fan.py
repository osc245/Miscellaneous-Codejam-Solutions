for case in range(1, int(input()) + 1):
    line = input().split()
    x, y, moves = int(line[0]), int(line[1]), list(line[2])
    ans = 0 if x == y == 0 else "IMPOSSIBLE"
    if ans:
        for i in range(len(moves)):
            if moves[i] == "N":
                y += 1
            elif moves[i] == "S":
                y -= 1
            if moves[i] == "E":
                x += 1
            elif moves[i] == "W":
                x -= 1
            if abs(x) + abs(y) <= i + 1:
                ans = i + 1
                break
    print("Case #{}: {}".format(case, ans))
