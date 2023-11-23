n = int(input())
max_prize = 0

for _ in range(n):
    dices = list(map(int, input().split()))
    numbers = [0 for _ in range(7)]

    for dice in dices:
        numbers[dice] += 1

    if 4 in numbers:
        prize = 50000 + (numbers.index(4) * 5000)
    elif 3 in numbers:
        prize = 10000 + (numbers.index(3) * 1000)
    elif numbers.count(2) == 2:
        idx = numbers.index(2)
        prize = 2000 + (idx * 500) + ((numbers.index(2, idx + 1)) * 500)
    elif 2 in numbers:
        prize = 1000 + (numbers.index(2) * 100)
    else:
        prize = max(dices) * 100

    max_prize = max(max_prize, prize)

print(max_prize)
