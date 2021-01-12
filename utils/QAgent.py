import numpy as np
from utils.Utils import dynamic_QM
class Q_agent_base(): 
  def __init__(self,starting_actions=2): #starting action is how many actions are initially present. 
    self.states = [] #will store the names of the states 
    self.states.append('0')
    self.QM=dynamic_QM()
    for _ in range(starting_actions):
      self.QM.add_action()
    
  def add_state (self,state):  #add new state not before checking if it exists. 
    if  not(state in self.states):  #state does not exist
      self.states.append(state)
      self.QM.add_state()
      
  def total_actions(self): 
    return self.QM.cols-1

  def add_action(self): 
      self.QM.add_action() #no need to check, this action literally adds in numerical order
  
  def table(self): 
     return self.QM.summary()

  def allstates(self):
    return self.states

  def search (self,search_value): #search and return index
    try:
      return self.states.index(search_value)
    except: 
      return -1 #if the state does not exist.

  def reward(self,state,action,reward): 
    try: #to ensure that only states that exist and actions that exist are used. 
  
     self.QM.table[self.states.index(state)][action+1]=reward
    except:
      pass
    #self.QM.table[self.QM.search_states(state)[0]][action+1]=reward  #assumes the first value is the correct one, as there should be no duplciates

  def return_highest (self, state): 
    return np.argmax(self.QM.summary()[self.states.index(state)] )
  
