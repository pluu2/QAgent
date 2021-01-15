#### Training Loop 


import numpy as np
from utils.QAgent import *
from utils.localizationNet import *
import matplotlib.pyplot as py
from utils.Utils import generate_square as GS
import random
from model.model import MSE


sampling_grid=generate_sampling_grid()
square=GS(14,2) 

#transpose array 
identity= np.array([[1,0,0],[0,1,0],[0,0,1]]) 
affine1=np.array( [[0,0,0],[0,0,0.5],[0,0,0]])
affine2=np.array( [[0,0,0],[0,0,0.5],[0,0,0]])
mod=identity+affine1
resultant_affine=np.dot ((affine1+identity),(affine2+identity)) 
#print(resultant_affine)

affines =[]
affine1=np.array( [[0,0,0.5],[0,0,0],[0,0,0]]) #action 0 
affine2=np.array( [[0,0,0],[0,0,0.5],[0,0,0]]) #actinon1
affines.append(affine1)
affines.append(affine2) 

#answer is 0,1 
manipulation3 = np.ceil(affine_transformation(square,resultant_affine,sampling_grid)) #for data processing, all values are inputted using ceil. 
#py.imshow(manipulation3.reshape(28,28))
target=manipulation3 #This will be our target. 


#STEP1: Load up Q values and add most current state. Since we are looking at MSE it looks up only 1s
agent = Q_agent_base(starting_actions=2) 


current_state = np.array2string(square.flatten())

agent.add_state(current_state)
#load up MSE start state with real MSE: 
print('first MSE: ',MSE(target.flatten(),square.flatten()))
agent.reward(current_state,0,MSE(target.flatten(),square.flatten()))
agent.reward(current_state,1,MSE(target.flatten(),square.flatten()))

transformation=square
episilon = 1
#Trainign loop 
print(agent.table())
for epochs in range(10): 
    print(f'epoch ', epochs)
    current_state = np.array2string(square.flatten()) #start from beginning
    for steps in range(2): 
        #print('iteration')
        #Step 2: Randomize a value to perform a value. 
        decision = random.uniform(0,1)
        
        if decision < episilon: 
            #do a random choice 
            action=random.randint(1,agent.total_actions()-1) #will randomize actions.
        else: 
            action=agent.return_lowest (current_state) #lowest in this context is MSE.

        print(f'action:', int(action))
        action=int(action)
        #Step 3: Perform the action (in this case it is a affine transformation)
        transformation= affine_transformation(transformation.reshape(28,28),identity+affines[action-1],sampling_grid)

        py.imshow(transformation.reshape(28,28))
        py.show()
        #step 4: Check if state exists. 
        next_state =np.array2string( np.ceil(transformation.flatten()))
        if (agent.search(next_state)==-1) : #if state does not exist. 
            agent.add_state(next_state)


        #Step 5: Check MSE to ensure that MSE has reduced. If it has then change the value 
        loss = MSE (target.flatten(), transformation.flatten() )
        if agent.return_Q(current_state,action-1) > loss: #if the loss is reduced. 
            #print('lower')
            reward = loss#+agent.return_lowest(next_state) #kind of like bellman eqn
            agent.reward(current_state,action,reward)
            #print(reward) 
            episilon-= 0.1
            if episilon <=0: 
                episilon=0
        else: 
            pass
            #print('nothing')

        current_state=next_state
        

print(f'lowest', agent.return_lowest(current_state))
print(f'episilon:', episilon)
print(agent.table())

print(agent.total_actions())
#test: 
