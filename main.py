
print("Welcome to the tip calculator.")

Bill = float(input("What was the total bill? $"))

percentageTip= int(input("What percentage tip would you like to give ? 10, 12, or 15? "))

tip_total = Bill * (percentageTip/100)

amount_people =int(input("How many people to split the bill? "))
 
Totalbill = Bill + tip_total

Bill_per_person = round(Totalbill/amount_people,2)
# Rounding to two decimal places
final_amount ="{:.2f}".format(Bill_per_person) 

print(f"Each person should pay: ${final_amount}")
