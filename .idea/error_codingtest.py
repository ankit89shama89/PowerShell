def count_zeroto_n(n):
    if n < 0 or n == 0:
       raise  ValueError(f'Negative values or 0 value are not allowed {n}')
    for x in range(0, n+1):
        print(x)

count_zeroto_n(1)