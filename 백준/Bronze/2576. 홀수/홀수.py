min_ = 101
sum_ = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        if min_ > n:
            min_ = n
        sum_ += n

if min_ == 101:
    print(-1)
else:
    print(sum_)
    print(min_)