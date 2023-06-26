N, K, A = map(int, input().split(" "))

card_index = 0
member_index = A

while True:
    if member_index > N:
        member_index = 1

    card_index += 1

    if card_index == K:
        break

    member_index += 1


print(member_index)
