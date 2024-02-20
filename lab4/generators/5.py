def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Введите число n: "))

for num in numbers_down_to_zero(n):
    print(num, end=' ')