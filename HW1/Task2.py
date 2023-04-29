import numpy as np

class TrainGame:
    def __init__(self):
        self.grid_size = 5  #the grid dimension is 5*5
        self.num_states = self.grid_size**2  # the number of the states is gouble the size of the grid (here will be 25)
        self.num_actions = 4  #four actions can be taken by the agent
        self.obstacle_states = [6, 18] # Two obstacles at states 6 and 18
        self.goal_state = 24  #the goal will be at the last state
        self.reward_goal = 1  #positive reward +1 (reaching the goal)
        self.reward_obstacle = -1  #negative reward -1 (Hit an obstacle)
        self.reward_step = -0.1 #negative reward for each time step to finish faster the game
        self.transitions = np.zeros((self.num_states, self.num_actions, self.num_states)) #current state and the next state after taking the action
        for s in range(self.num_states): #convert the grid into 2D
            row = s // self.grid_size
            col = s % self.grid_size
            for a in range(self.num_actions):
                if a == 0: # Move up
                    next_state = s - self.grid_size
                    if next_state < 0:
                        next_state = s #reached to boundries end, so the next state will be the same state 
                elif a == 1: # Move down
                    next_state = s + self.grid_size
                    if next_state >= self.num_states:
                        next_state = s #reached to boundries end, so the next state will be the same state 
                elif a == 2: # Move left
                    next_state = s - 1
                    if col == 0:
                        next_state = s #reached to boundries end, so the next state will be the same state 
                elif a == 3: # Move right
                    next_state = s + 1
                    if col == self.grid_size - 1:
                        next_state = s #reached to boundries end, so the next state will be the same state 
                if next_state in self.obstacle_states:
                    reward = self.reward_obstacle #if the agent hit an obstacle, it will get a negative reward
                elif next_state == self.goal_state:
                    reward = self.reward_goal #if the agent reached to the goal
                else:
                    reward = self.reward_step
                self.transitions[s, a, next_state] = 1 
                #if the agent keep moving from one position to another, then the transition become 1
                self.transitions[s, a, s] = reward 
                #if the agent didn't move from one position to another then it will recieve a negative reward -0.1
    
