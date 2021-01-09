import numpy as np
from utils.Utils import *
class Q_agent_base(): 
  def __init__(self): 
    self.states = []
    self.QM=dynamic_QM()
    
  def add_state (self,state):  #add new state not before checking if it exists. 
    if  self.QM.search_states(state).size==0:  #state does not exist
      self.QM.add_state(state)
  def add_action(self): 
      self.QM.add_action() #no need to check, this action literally adds in numerical order
  def table(self): 
     return self.QM.summary()

  def reward(self,state,action,reward): 
    try: #to ensure that only states that exist and actions that exist are used. 
      self.QM.table[self.QM.search_states(state)[0]][action+1]=reward  #assumes the first value is the correct one, as there should be no duplciates
    except: 
       pass
