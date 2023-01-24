import numpy as np
## Finding the right amount to save away

## Assume:
## 1.) semi-annual raise is 7%
## 2.) Investments have return of 4%
## 3.) Down payment is 25% cost of house
## 4.) Cost of house saving for is $1M

## Find the best rate of savings to achieve a down payment
## on a $1M house in 36 months, within $100.

## use bisection search

# Test Case 1 >>> 
# Enter the starting salary: 150000 
# Best savings rate: 0.4411 
# Steps in bisection search: 12
# >>>

## User Inputs
annual_salary = int(input("Enter your annual salary:"))

## Constraints
current_savings = 0
total_cost = 1000000
semi_annual_raise = .07
downpayment = .25 * total_cost
r = .04

## Calculations
low = 0
high = 1000
steps = 0
month = 1
guess = (low + high ) / 2
tolerance = 100
monthly_salary = annual_salary / 12
distFromGoal = abs(current_savings - downpayment)

def calcDist(curSav):
    return abs(curSav - downpayment)

def calcSavings(anSal,gs):
    curSav = 0
    for m in range(1,37):   
      if ((m % 6 == 1) and m != 1):
        anSal = np.floor(anSal * (1 + semi_annual_raise))
        monthly_salary = anSal / 12  
        curSav = np.round((curSav * (1 + r/12)) + (gs/1000 * monthly_salary),2)
      else:
        monthly_salary = anSal / 12
        curSav = np.round((curSav * (1 + r/12)) + (gs/1000 * monthly_salary)) 
    
    return curSav

while distFromGoal >= tolerance:
    ## Rate was too low
    if (current_savings - downpayment) < 0: 
        low = guess
        steps+= 1
        guess = (low + high) / 2
        current_savings = calcSavings(annual_salary,guess)
        distFromGoal = calcDist(current_savings)   
    ## Rate was too high
    elif (current_savings - downpayment) > 0: 
        print("too high start:",current_savings,distFromGoal,guess)
        high = guess 
        steps+= 1
        guess = (low + high) / 2
        current_savings = calcSavings(annual_salary,guess)
        distFromGoal = calcDist(current_savings)  
        print("too high end:",current_savings,distFromGoal,guess)
        
if distFromGoal <= tolerance:
    print(np.round(guess/1000,2),steps,current_savings)
    
    