"""
What is Bisection Method? 
The method is also called the interval halving method, the binary search 
method or the dichotomy method. This method is used to find root 
of an equation in a given interval that is value of ‘x’ for which f(x) = 0 . 
The method is based on The Intermediate Value Theorem which states that 
if f(x) is a continuous function and there are two real numbers a and b
such that f(a)*f(b) 0 and f(b) < 0), then it is guaranteed that it has at 
least one root between them.
"""
#Program For Bisection Method
def f(x):	
    return x**2-x-1
# Implementing Bisection Method
def bisection(a,b,e):
    step = 1
    print('\n\n--> BISECTION METHOD IMPLEMENTATION <--')
    condition = True
    while condition:
        m = (a + b)/2
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        step = step + 1
        condition = abs(f(m)) > e
    print('\nRequired Root is : %0.8f' % m)
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = float(input('Error: '))
if f(a) * f(b) > 0.0:
  
    print('Try Again with different valid Interval .')
else:
    bisection(a,b,e)
