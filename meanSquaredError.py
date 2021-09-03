import numpy as np

t =[0,0,1,0,0,0,0,0,0,0]
y =[0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

def mean_squared_eror(y,t):
    return 0.5 * np.sum((y-2)**2)


print(mean_squared_eror(np.array(y), np.array(t)))