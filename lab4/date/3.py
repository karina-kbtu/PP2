from datetime import datetime

now = datetime.now()
new_datetime = now.replace(microsecond=0)

print("Original Datetime:", now)
print("Datetime without Microseconds:", new_datetime)