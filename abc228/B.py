N, X = map(int, input().split(" "))
friends = list(map(int, input().split(" ")))

friend = X
flags = [False] * N
flags[X - 1] = True

while True:
    friend = friends[friend - 1]

    if flags[friend - 1]:
        break

    flags[friend - 1] = True

print(flags.count(True))
