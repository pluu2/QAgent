
import numpy as np
from utils.QAgent import *
from utils.localizationNet import *
import matplotlib.pyplot as py
from utils.Utils import generate_square as GS

agent = Q_agent_base()  #this works. 

#generate data 

square=GS(1,2)
py.imshow(square)
py.show()