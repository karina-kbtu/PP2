from datetime import datetime

def date_diff_seconds(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()

# Пример использования
date_format = "%Y-%m-%d %H:%M:%S"
date_str1 = "2022-01-01 00:00:00"
date_str2 = "2022-01-02 12:00:00"

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

diff_seconds = date_diff_seconds(date1, date2)
print("Разница между датами в секундах:", diff_seconds)