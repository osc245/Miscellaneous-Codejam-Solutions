for case in range(1, int(input()) + 1):
    num1, num2 = '', ''
    for s in input():
        num1 += '2' if s == '4' else s
        num2 += '2' if s == '4' else '0'
    print('Case #{}: {} {}'.format(case, int(num1), int(num2)))
