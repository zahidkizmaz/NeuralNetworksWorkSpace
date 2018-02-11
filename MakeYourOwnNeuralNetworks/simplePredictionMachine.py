# simple classifer:
import numpy as np

"""
Example Values:
    w = 3, l = 1
    w = 1, l = 3
"""

"""
 y = A*x  | A => slope 
"""
def func(A, x):
    return A*x

"""
E = t - y  | t => true value
"""
def E(t, y):
    return t-y

"""
DeltaA = L * (E/x)  | L => Learning rate
"""
def deltaA(L, E, x):
    return L*E/x


if __name__ == "__main__":
    print("Hello from simple classifier")
    t = 1.1 # desired result value
    x = 3.00
    A = 0.25 # arbitrary initial value
    l = 0.5 # learning rate

    y = func(A,x)
    e = E(t,y)
    a_delta = deltaA(l, e, x)
    A = A + a_delta

    print('Result: {}, A: {}'.format(func(A,x), A))



