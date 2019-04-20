import math
 
class XmathError(Exception): pass
 
def fact(n):
    """fact(n) --> Compute the factorial of n"""
    try:
        if isinstance(n, bool): raise #numeric type required
        if int(n) != n: raise #value must be an integer
        if n < 0: raise #value cannot be nagative
        # if n==0 or n==1: return 1
        # else: return n*fact(n-1)
        result = 1
        for i in range(2, n+1):
            result = i*result
        return result
    except:
        raise XmathError
 
def ave(x):
    """ave(x) --> Calculate the mean of x"""
    try:
        if isinstance(x, bool): raise #numeric type required
        for type in [int, float]:
            if isinstance(x, type): return x
        xsum = 0.0
        for i in range(len(x)):
            xsum = xsum + x[i]        
        return xsum/len(x)
    except:
        raise XmathError
 
if __name__ == '__main__':
    print('fact(10) = ', fact(10))
    x = [10,19,30,33]
    print('ave([10,19,30,33]) = ', ave(x))

