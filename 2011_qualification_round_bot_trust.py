for case in range(1, int(input()) + 1):
    line = input().split()
    robot = [line[i] for i in range(1, len(line)) if i % 2]
    pos = [int(line[i]) for i in range(1, len(line)) if i % 2 == 0]
    info = [[1, 0], [1, 0]] # [[oTime, oPos], [bTime, bPos]]
    ans = 0
    for i in range(len(robot)):
        index = 1 if robot[i] == 'B' else 0
        time = max(0, abs(pos[i] - info[index][0]) - info[index][1]) + 1
        ans += time
        info[1 - index][1] += time
        info[index][1] = 0
        info[index][0] = pos[i]
    print('Case #{}: {}'.format(case, ans))
