#Find cube root of a perfect cube

# x = int(input('Enter an integer:'))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x,'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of',x,'is',ans)

#Test if an integer greater than 2 is prime. if not print smallest divisor

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
if x%2 == 0:
    smallest_divisor = 2
else:
    for guess in range(2,x):
        if x%guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print('Smallest divisor of',x,'is',smallest_divisor)
else:
    print(x,'is a prime number')
