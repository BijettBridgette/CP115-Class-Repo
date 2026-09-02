receipt = "Item\tPrice\tQuantity\ncofee\t3.50\t2\nmuffin\t2.10\t3\nwater\t1.05\t4"
coffee = 3.50 * 2
muffin = 2.10 * 3
water = 1.05 * 4
subtotal = coffee + muffin + water
tax = subtotal * 0.06
total = subtotal + tax
Final_total = receipt + "\nsubtotal\t" + str(subtotal) +  "\ntax\t" + str(tax) + "\ntotal\t" + str(total)
print(Final_total)