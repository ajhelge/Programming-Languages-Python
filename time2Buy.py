#A calculator for finding time required to save for a home.

total_cost = float(input("Whats the total cost of the home? : "))
portion_down_payment = float(input("Percentage needed for a down payment (0-1): ")) #percentage of house cost needed for down payment.
current_savings = 0.0
annual_salary = float(input("Whats your annual salary? : "))
portion_saved = float(input("Percentage of your annual salary to be saved (0-1): ")) #percent of monthly salary saved.
total_interest_earned = 0
this_months_interest = 0
amount_payed_in = 0
current_pay_in = 0

r = .04 #annual interest on invested savings

#find total down payment and monthly salary.
total_upfront = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

#main
months = 0
while not (current_savings >= total_upfront):
    #calculate interest on current investment
    this_months_interest = current_savings * ((r/12))
    total_interest_earned = total_interest_earned + this_months_interest
    current_savings =  current_savings + this_months_interest
    #add monthly salary to investment
    current_pay_in  = (monthly_salary * portion_saved)
    amount_payed_in += current_pay_in
    current_savings += current_pay_in
    #increment the month
    months += 1

# print everything in a convenient little table
print("---------------------------------")
print("| Total months    | {:11} |".format(months))
print("---------------------------------")
print("| Amount needed   | {:11} |".format(total_upfront))
print("---------------------------------")
print("| Amount saved    | {:11.2f} |".format(current_savings))
print("---------------------------------")
print("| Interest Earned | {:11.2f} |".format(total_interest_earned))
print("---------------------------------")
print("| Salary Saved    | {:11.2f} |".format(amount_payed_in))
print("---------------------------------")




