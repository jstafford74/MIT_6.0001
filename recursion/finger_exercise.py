def harmonic_sum(n:int):
   
   if n < 2:
       return 1
   else:
       return 1 / n + (harmonic_sum(n - 1))
    
    
## print(harmonic_sum(5))

def fib(n):
    """Assumes n an int >= 0
    Returns FIbonaccie of n"""
    global num_fib_calls
    num_fib_calls += 1
    
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(5)) 

def test_fib(n):
    for i in range(n+1):
        global num_fib_calls
        num_fib_calls = 0
        print('fib of',i,'=',fib(i))
        print('fib called',num_fib_calls,'times')
    
test_fib(6)
 
def is_palindrome(s):
    """Assumes s is a str
    Returns True if letters in s form a palindrome;
    False otherwise. Non-letters and capitalization are ignored."""
    
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def is_pal(s):
        print(' is_pal called with',s)
        if len(s) <= 1:
            print(' About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print(' About to return',answer,'for',s)
            return answer 
        
    return is_pal(to_chars(s))

# print('Try dogGod')
# print(is_palindrome('dogGod'))
# print('Try doGood')
# print(is_palindrome('doGood'))
