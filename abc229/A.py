S1 = list(input())
S2 = list(input())

S = [S1, S2]

if S[0][0] == S[1][1] == '.':
    print('No')
elif S[0][1] == S[1][0] == '.':
    print('No')
else:
    print('Yes')