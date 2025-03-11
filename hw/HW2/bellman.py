import numpy as np



reward = np.array([10, 0, 3])
value_ = np.array(3)
P = np.array([
    [0.1, 0.6, 0.3],
    [0.4, 0.2, 0.4],
    [0.5, 0.3, 0.2]
])
 
I = np.eye(3)
gamma_discount= 0.9
value_ = np.linalg.inv(I - gamma_discount*P)@R
print("Final Value State Function: \n",value_)
