# QAgent

Practice with Q-Learning. Q-Learning is roughly implemented from scratch using numpy. 
In the above code a Q-agent learns to use a use a STN modified to transpose a square in four directions in order to reach a specified target in a specified number of steps. 

In this implementation, the list of states in the Q-table is dynamically increased as new states are discovered. 

Under test.ipynb, you can see the network learning to move the square in such a way that the square ends up at the target square position over a variable number of actions. 

This is a first prototype of using RL to link together layers in a network. 
