# simple classifer:

"""
 y = A*x  | A => slope 
"""
def y(A, x):
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


