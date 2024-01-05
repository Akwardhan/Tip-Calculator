print("Welcome to the Tip Calculator")
Bill=input("Enter the total Bill Please:\n")

Bill_new=int(Bill)
tip=int(input("What percentage tip would you like to give: 10, 15 or 12\n"))


percentage= Bill_new*(tip/100)


total_Bill1= percentage + Bill_new


a=input("How many people are there to split the bill\n")
a_new=int(a)

bill_new1=total_Bill1/a_new


print((f"Each Person should pay:{round(bill_new1,2)}"))








