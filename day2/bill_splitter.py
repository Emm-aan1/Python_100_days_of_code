print("Welcome to Dilaro's Restuarant")
bill = int(input("Enter your bill: $"))
tip_bill = int(input("How much tips in percentage? 5, 7, or 10? "))
tip_percentage = tip_bill / 100
# print(tip_percentage)

total_tip = bill * tip_percentage
# print(bill + total_tip)

split_bill = int(input("How many people are splitting the bill? "))

total_bill = (bill + total_tip) / split_bill
round_bill = round(total_bill, 2)
print(f"Each person will pay: ${round_bill}")
print("Thank you")