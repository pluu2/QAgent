
import numpy as np
from utils.QAgent import *
from utils.localizationNet import *
import matplotlib.pyplot as py

agent = Q_agent_base()  #this works. 

print(generate_sampling_grid())

#generate data 

a=3
input=np.zeros((28,28))
for y in range (28-a-4,28-a): 
    for x in range(12,16): 
        input[y][x]=1
py.imshow(input)
py.show()
input=input.flatten() 

input=np.array(input)
input=input.reshape(28,28)
