A, B = map(str, input().split(" "))
l = min(len(A), len(B))
A, B = A[-l:], B[-l:]

for i in range(0, l):
    if int(A[i]) + int(B[i]) > 9:
        print("Hard")
        exit()

print("Easy")
