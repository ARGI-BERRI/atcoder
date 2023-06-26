import collections

N = int(input())

votes = [input() for _ in range(N)]
votes = collections.Counter(votes)

print(votes)
