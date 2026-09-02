#Put student info in the same line using escape characters
student  = "Name:Ahmad Bin Abu\t\t\t\tMatric.No:MS2025123499\n\n"

#Making alphabet K with stars using escape characters
star1 = "*\t\t\t*\n"
star2 = "**\t\t**\n"
star3 = "***\t***\n"
star4 = "********\n"
star5 = star3 + star2 + star1
combine = star1 + star2 + star3 + star4 + star5

#make a sentence in 3 lines
sentence1 = "\n\nThis is my\n\tsecond\n\t\tassignment"

#do the arithmetic operations
mark = 2 * 10

# combine the calculation in new variable to conclude it
sentence2 = "\nI want my 2x10 marks, which is " +str(mark) + " full marks\n"

# display output by combining all variables
print (student + combine + sentence1 + sentence2)