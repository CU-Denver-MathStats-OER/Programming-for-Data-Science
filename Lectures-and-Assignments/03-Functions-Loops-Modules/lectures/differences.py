# module differences.py
def for_diff(f,x=0,h=.1):
    '''
    Computes a forward difference approximation to the derivative of f at
    x using a step-size of h.
    
    >>> for_diff(lambda x : 5)
    0.0
    
    >>> for_diff(lambda x : 5*x)
    5.0
    '''
    deriv=(f(x+h)-f(x))/h
    return deriv

def back_diff(f,x=0,h=.1):
    deriv=(f(x)-f(x-h))/h
    return deriv

def cent_diff(f,x=0,h=.1):
    deriv=(f(x+h)-f(x-h))/(2*h)
    return deriv
