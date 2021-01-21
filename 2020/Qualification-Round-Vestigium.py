for case in range(1, int(input()) + 1):
    size = int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(size)]
    trace = sum([matrix[i][i] for i in range(size)])
    rows = sum([len(set(r)) < size for r in matrix])
    cols = sum([len(set(c)) < size for c in zip(*matrix)])  # using zip(*matrix) as the transpose of the matrix
    print("Case #{}: {} {} {}".format(case, trace, rows, cols))
