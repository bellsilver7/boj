import sys

input = sys.stdin.readline
n = int(input())

x = []
for i in range(n):
    s = input().strip()
    if s == 'pop':
        if len(x) == 0:
            print(-1)
        else:
            print(x[-1])
            del x[-1]
    elif s == 'size':
        print(len(x))
    elif s == 'empty':
        print(1 if len(x) == 0 else 0)
    elif s == 'top':
        print(-1 if len(x) == 0 else x[-1])
    else:
        tmp = s.split()
        x.append(tmp[1])
