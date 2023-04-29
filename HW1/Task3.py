
import numpy as np

class BasicAgent:
    def __init__(self, grid_size, goal_state):
        self.grid_size = grid_size
        self.goal_state = goal_state

    def get_action(self, state):
        row = state // self.grid_size
        col = state % self.grid_size
        
        # Walk towards goal with probability 0.8, otherwise act randomly
        if np.random.uniform() < 0.8:
            if row < self.grid_size-1 and state+self.grid_size != self.goal_state:
                return 1 # Move down
            elif col < self.grid_size-1 and state+1 != self.goal_state:
                return 3 # Move right
            elif col > 0 and state-1 != self.goal_state:
                return 2 # Move left
            else:
                return 0 # Move up
        else:
            return np.random.choice(range(4))


def evaluate_policy(agent, grid, num_episodes):
    state_returns = np.zeros(grid.num_states)
    state_counts = np.zeros(grid.num_states)
    
    for episode in range(num_episodes):
        state_sequence = []
        action_sequence = []
        reward_sequence = []

        state = np.random.choice(grid.num_states)
        while state != grid.goal_state:
            action = agent.get_action(state)
            next_state = np.random.choice(grid.num_states, p=grid.transitions[state, action])
            reward = grid.transitions[state, action, next_state]
            
            state_sequence.append(state)
            action_sequence.append(action)
            reward_sequence.append(reward)
            
            state = next_state
        
        # Calculate returns and update state values
        G = 0
        for t in range(len(state_sequence)-1, -1, -1):
            G += reward_sequence[t]
            state = state_sequence[t]
            if state not in state_sequence[:t]:
                state_returns[state] += G
                state_counts[state] += 1
    
    state_values = np.zeros(grid.num_states)
    for state in range(grid.num_states):
        if state_counts[state] > 0:
            state_values[state] = state_returns[state] / state_counts[state]
    
    return state_values
