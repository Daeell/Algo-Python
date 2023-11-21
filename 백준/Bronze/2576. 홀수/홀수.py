# 리스트 컴프리헨션 적용 풀이
numbers = [int(input()) for _ in range(7)]
odds = [num for num in numbers if num % 2 == 1]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)