main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    price = 10
elif main_course == "Beef":
   price = 12
else :
    price = 11

if drink == "Soft Drink":
    price = 2
else :
    price = 3

if dessert == "Ice Cream":
    price = 4
else :
    price = 5

total_bill = (main_course + drink + dessert) * 0.1

print(f"{final_bill:.2f}")
