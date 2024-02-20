from datetime import datetime, timedelta

# Получаем текущую дату
current_date = datetime.now()

# Вычисляем вчерашнюю дату
yesterday = current_date - timedelta(days=1)

# Вычисляем завтрашнюю дату
tomorrow = current_date + timedelta(days=1)

# Выводим результаты
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))