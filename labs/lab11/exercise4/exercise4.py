sales = int(input())
count = 0
record_days = 0
previous_sales = 0

while sales != 0:
    count += 1
    if sales > previous_sales:
        record_days += 1
        previous_sales = sales
    sales = int(input())

print(count)
print(record_days)
