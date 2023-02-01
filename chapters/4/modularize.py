def find_root_bounds(x,power):
    """return low,high such that low**power <= x and high**power >=x

    Args:
        x (float): _description_
        power (int): positive integer
    """
    low = min(-1,x)
    high = max(1,x)
    return low, high

def bisection_solve(x,power,epsilon,low,high):
    """returns ans so that ans ** power within epsilon of x

    Args:
        x (float): _description_
        power (int): _description_
        epsilon (float): _description_
        low (float): _description_
        high (float): _description_
    """
    ans = (high + low) / 2
    while abs(ans**power -x) >= epsilon:
        if ans**power <x:
            low = ans
        else:
            high = ans
            
        ans = (high + low) / 2
    
    return ans 

## Generalizing bisection_solve
def bisection_solve(x,eval_ans,epsilon,low,high):
    """Returns ans such that eval(ans) within epsilon of x

    Args:
        x (float): _description_
        eval_ans (function): maps float to float
        epsilon (float): _description_
        low (float): _description_
        high (float): _description_
    """
    ans = (high + low) / 2
    while abs(eval_ans(ans) -x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
   
    return ans


def find_root(x,power,epsilon):
    """Returns float y such that y** power is within epsilon of x
    If such a float does not exist, it returns None

    Args:
        x (int or float): _description_
        power (int): _description_
        epsilon (int or float): _description_
    """
    
    if x < 0 and power%2 == 0:
        return None
    low, high = find_root_bounds(x,power)
    
    return bisection_solve(x,power,epsilon,low,high)