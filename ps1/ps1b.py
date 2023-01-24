import numpy as np

## Saving, with a raise


## Additionally, ask user for:
## 1.) Starting annual salary(annual_salary)
## 2.) Portion of salary to be saved(portion_saved)
## 3.) Cost of dream home(total_cost)
## 4.) Semi-annual salary raise(semi_annual_raise)

# Test Case 1 >>>
# Enter your starting annual salary: 120000
# Enter the percent of your salary to save, as a decimal: . 05
# Enter the cost of your dream home: 500000
# Enter the semiannual raise, as a decimal: .03
# Number of months: 142 
# >>>

# Test Case 2 >>>
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: . 1
# Enter the cost of your dream home: 800000
# Enter the semiannual raise, as a decimal: .03
# Number of months: 159
# >>> 

# Test Case 3 >>> 
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: . 05
# Enter the cost of your dream home: 1500000 
# Enter the semiannual raise, as a decimal: .05
# Number of months: 261
# >>>

## User Inputs
annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal:"))

## Constraints
current_savings = 0
downpayment = .25 * total_cost

## Calculations

numMonths = 0
r = .04


    
while current_savings < downpayment:
    numMonths += 1
    monthly_salary = annual_salary / 12    
    current_savings = (current_savings + current_savings * r/12) + (portion_saved * monthly_salary)
    
    if numMonths % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    
    
      
if current_savings >= downpayment:
    print(numMonths)