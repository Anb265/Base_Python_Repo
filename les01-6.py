dist_in_day = 2        # Расстояние, пробегаемое в день
goal_dist = 3          # Хочет пробегать в день
day = 1

while dist_in_day < goal_dist:
    dist_in_day = dist_in_day * 1.1
    day += 1
print(day)