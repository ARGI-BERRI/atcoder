N = int(input())
S = list(map(int, input().split(" ")))


def area(a: int, b: int) -> int:
    return (4 * a * b) + (3 * a) + (3 * b)


def solve() -> None:
    sqs = [area(a, b) for a in range(1, 251) for b in range(1, 251)]
    print([s in sqs for s in S].count(False))


solve()
