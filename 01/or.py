#-*-cording:utf-8-*-
import numpy as np

def step(x , theta=0.3):
    return np.where(x >= theta, 1, 0)

X = np.array([0.1, 0.2, 0.3, 0.4])
y = step( x=X)

def OR( x_1, x_2):
    x = np.array([x_1, x_2])
    w = np.array([0.5, 0.5])
    u = np.dot( x , w )

    return u



z1 = OR( x_1=0, x_2 = 0)
y1 = step( x=z1)
#print(z1, y1)

def test(GATE):
    for i in [0,1]:
        for j in [0,1]:
            z = GATE( x_1=i, x_2 = j)
            y = step( x=z)
            print("x_1={}, x_2={} : y={}".format( i , j, y))

test(GATE = OR)
