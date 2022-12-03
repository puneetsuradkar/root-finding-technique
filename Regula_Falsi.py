"""
The regula-falsi method is the oldest method of finding the approximate numerical value of a real root of an equation f(x) = 0.
This method is also known as method of false position. The method used to estimate the roots of a polynomial f(x).
In this method we suppose that x1 and x2 are two points where f(x1) and f(x2) are of opposite sign .Let f(x1) < 0 and f(x2) > 0. 
Hence the root of the equation f(x) = 0 lies between x1 and x1 and so, f(x1)f(x2) < 0.
"""
#Program For Bisection Method
# Defining Function
def f(x):
    return x**2-x-1

# Implementing False Position Method or Regula Falsi  Method
def falsePosition(a,b,e):
    step = 1
    print('\n\n --> FALSE POSITION METHOD IMPLEMENTATION <--')
    condition = True
    while condition:
        m = a - (b-a) * f(a)/( f(b) - f(a) )
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

        step = step + 1
        condition = abs(f(m)) > e

    print('\nRequired root is: %0.8f' % m)
a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = float(input('Error: '))


# Checking Correctness of initial guess values and false positioning
if f(a) * f(b) > 0.0:
    print('Try Again with different valid Interval.')
else:
    falsePosition(a,b,e)
