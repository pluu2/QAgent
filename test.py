
import numpy as np
from utils.QAgent import Q_agent_base
from utils.localizationNet import *
import matplotlib.pyplot as py
from utils.Utils import generate_square as GS
from utils.Utils import dynamic_QM


agent=Q_agent_base()

print(agent.states)