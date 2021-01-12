import numpy as np 
def MSE(target,prediction): 
    return (1/len(target))*np.sum((target-prediction) **2 )
