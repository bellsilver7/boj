import sys


def move(num, start, end):
    if num == 1:
        print(start, end)
        return
    # step1
    move(num - 1, start, 6 - start - end)
    # step2
    print(start, end)
    # step3
    move(num - 1, 6 - start - end, end)


input = sys.stdin.readline
n = int(input())

print(2**n-1)
move(n, 1, 3)
