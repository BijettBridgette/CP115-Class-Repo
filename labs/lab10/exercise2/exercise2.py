num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total_temperature = 0.0

for _ in range(num_days):
    current_temp = float(input())
    total_temperature += current_temp
    
   
    if current_temp > danger_threshold:
        danger_days += 1

average_temp = total_temperature / num_days if num_days > 0 else 0.0

print(danger_days)
print(f"{average_temp:.1f}")
