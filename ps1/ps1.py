import numpy as np

## House Hunting

## cost of home is total_cost
## portion of cost needed for down payment is portion_down_payment, assume 25%
## amount saved to date is current_savings, start value is $0
## invest savings each month at r, assume 4% and earn current_savings * (r/12)
## save portion of salary each month to saving for down payment, portion_saved
## savings increases each month by return on investment plus portion of salary

##Write program to calculate how many months it will take to save up enough money
##for a down payment.

## Ask user for following variables:
## 1.) Starting annual salary(annual_salary)
## 2.) Portion of salary to be saved(portion_saved)
## 3.) Cost of dream home(total_cost)

# Test Case 1 >>> 
# Enter your annual salary: 120000 
# Enter the percent of your salary to save, as a decimal: . 10
# Enter the cost of your dream home: 1000000
# Number of months: 183 
# >>>

# Test Case 2 >>> 
# Enter your annual salary: 80000 
# Enter the percent of your salary to save, as a decimal: . 15
# Enter the cost of your dream home: 500000
# Number of months: 105 
# >>>

## User Inputs
annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))

## Constraints
current_savings = 0
downpayment = .25 * total_cost

## Calculations
monthly_salary = annual_salary / 12
numMonths = 0
r = .04

while current_savings < downpayment:
    numMonths += 1
    current_savings = (current_savings + current_savings * r/12) + (portion_saved * monthly_salary)
    
if current_savings >= downpayment:
    print(numMonths)