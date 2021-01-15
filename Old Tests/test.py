
#To test various modules
import numpy as np
from utils.QAgent import Q_agent_base
from utils.localizationNet import *
import matplotlib.pyplot as py
from utils.Utils import generate_square as GS
from utils.Utils import dynamic_QM
from model.model import MSE 

agent=Q_agent_base(2)

agent.add_state('0212') #the states will have to be stored as a text
agent.add_state('1232')

print(agent.allstates())

print(agent.search('0212'))
print(agent.search(12312))

print(agent.reward('0212',1,10))

print(agent.table())

print(agent.return_highest('0212'))
print(agent.return_highest('1232'))


print(agent.return_Q('0212',1))