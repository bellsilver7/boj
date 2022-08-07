import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
answer = max(nums) * min(nums)
print(answer)
