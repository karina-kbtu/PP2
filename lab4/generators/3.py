def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
result = [str(num) for num in divisible_by_3_and_4(n)]
print(", ".join(result))