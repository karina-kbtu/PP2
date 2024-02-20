def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

# Тестируем генератор с помощью цикла "for" и печатаем каждое из возвращаемых значений
for square in squares(2, 10):
    print(square)