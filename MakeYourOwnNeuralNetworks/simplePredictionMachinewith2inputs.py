import math

def y( x):
    return sigmoid(x)

def E(t, y):
    return t -y

def deltaA(L,E,x):
    return L * E / x

def sigmoid(y):
    return 1 / (1 + math.exp(-x))

# OR Logic gate
inputs= [(1,1), (1,0), (0, 0), (0,1)]
t = [1, 1, 0, 1]
#A = 0.25
L = 0.5

for i in range(len(t)):
    x = inputs[i][0] + inputs[i][1]
    res = y( x)
    e = E(t[i], res)
    #dA = deltaA(L, e, res)
    #A = A + dA
     
r = y(0)
print((r))
