S, T, X = map(int, input().split(" "))

if S > T:
    T = T + 24

    if T > X and S > X:
        X = X + 24

if S <= X < T:
    print("Yes")
else:
    print("No")
