target_points = int(input())

total_points = 0
rounds_played = 0

while total_points < target_points:
    current_points = int(input())
    total_points += current_points
    rounds_played += 1

print(total_points)
print(rounds_played)
