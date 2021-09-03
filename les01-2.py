total_seconds = int(input("Введите количество секунд для конвертации: "))
total_minutes = total_seconds // 60
left_seconds = total_seconds % 60
left_minutes = total_minutes % 60
total_hours = total_minutes // 60

# print(total_minutes)
# print(left_seconds)
# print(left_minutes)
# print(total_hours)

print(f'Это {total_hours:02}h:{left_minutes:02}m:{left_seconds:02}s')
