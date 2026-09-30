num_rounds = int(input())

final_score = 0.0
rounds_processed = 0

for i in range(num_rounds):
    score = float(input())

    # 1. Apply the 20% bonus properly if greater than 100
    if score > 100:
        score *= 1.20
    
    # 2. Accumulate EVERY score outside of the if/else block
    final_score += score
    rounds_processed += 1

# 3. If this is a script, print the raw float. 
# (If this is inside a function for pytest, use: return final_score)
print(final_score) 
print(rounds_processed)

