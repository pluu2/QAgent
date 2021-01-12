import numpy as np
#class that adds columns as rows are added. 
class dynamic_QM(): 
  def __init__(self,rows=1,cols=1): 
    self.table =np.zeros((1,1)) 
    self.rows=rows
    self.cols=cols

  def add_state(self): 
    to_add= np.ones((1,self.cols))
    self.rows+=1
    self.table = np.concatenate([self.table,to_add]) 

  def add_action(self): 
    to_add  = np.ones((1,self.rows))
    self.cols+=1
    self.table=np.concatenate ([self.table.T,to_add]).T

  def search_states(self,value): #returns all indices of search states
    return np.where(self.table[0:self.rows,0]==value)[0]

  def summary(self): 
    return self.table



def generate_square(x,y,s=4,w=28,h=28):
  square=np.zeros((28,28))
  for y_ in range (w-x-4,w-x): 
      for x_ in range(h-y-4,h-y): 
          square[x_][y_]=1
  square= np.array(square)
  return square