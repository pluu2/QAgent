import numpy as np
#class that adds columns as rows are added. 
class dynamic_QM(): 
  def __init__(self,rows=1,cols=1): 
    self.table =np.zeros((1,1)) 
    self.rows=rows
    self.cols=cols

  def add_state(self,state_val): 
    to_add= np.zeros((1,self.cols))
    to_add[0,0]= state_val
    self.rows+=1
    self.table = np.concatenate([self.table,to_add]) 

  def add_action(self): 
    to_add  = np.zeros((1,self.rows))
    self.cols+=1
    self.table=np.concatenate ([self.table.T,to_add]).T

  def search_states(self,value): #returns all indices of search states
    return np.where(self.table[0:self.rows,0]==value)[0]

  def summary(self): 
    return self.table
