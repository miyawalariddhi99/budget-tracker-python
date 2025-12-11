# Project: Personal Budget & Savings Tracker------
print("Personal Budget & Savings Tracker")

monthly_income=float(input(("Enter your total monthly income : ")))

print("\n Enter your monthly expenses below : ")
rent=float(input("Rent amount : "))
food=float(input("Food/Groceries amount : "))
electricity=float(input("Electricity amount : "))
internet=float(input("Internet amount: "))
travel=float(input("Travel/Transportation amount: "))
shopping=float(input("Shopping amount: "))
other_expenses=float(input("Other expenses amount: "))

## calculating total expenses

total_expenses=rent+food+electricity+internet+travel+shopping+other_expenses
## saving
remaining_budget=monthly_income-total_expenses
print("\n Remaining Budget : ",remaining_budget)

savings_percentage=(remaining_budget/monthly_income)*100
print("\n Savings Percentage : ",savings_percentage)

print("\n ----Monthly budget Summery---- ")
print("Rent : ",rent)
print("Food/Groceries : ",food)
print("Electricity : ",electricity)
print("Internet : ",internet)
print("Travel/Transportation : ",travel)
print("Shopping : ",shopping)
print("Other Expenses : ",other_expenses)
print("------------------------------------")
print("Total Expenses : ",total_expenses)

## if saving are negative then overspending warning

if remaining_budget < 0:
    print(" You are overspending! Try to reduce expenses.")
else:
    print(f"Savings Percentage: {savings_percentage:.2f}%")
    if savings_percentage < 10:
        print("Savings are very low. Try to control expenses.")
    elif savings_percentage < 30:
        print("Moderate savings. You can improve more.")
    else:
        print("Great! You are saving well.")
