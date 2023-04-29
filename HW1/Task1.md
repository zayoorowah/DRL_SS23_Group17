# 1 Understanding MDPs
## 1.1 Representing the chess game using the Markov Decision Process (MDP):
1. State space: all the possible states we can encounter in the environment
2. Actions: the set of different moves that the agent must do. It could be categorical or
continuous
3. Rewards: represent the outcome of the game after taking an action. The reward can
be positive or negative reward depending on whether the action is correct (+ve
reward) or wrong then (-ve reward)
4. Policy: sum of the probability distribution of all the actions in the action space
5. Agent: who makes the actions
6. Environment: everything surrounding the agent
7. state transition function: takes as input the current state of the system and an action
or event that occurs, and outputs the new state of the system that results from that
action or event

- The policy can be formalized as a function that maps a state to an action. The policy
can be deterministic or stochastic, depending on the learning algorithm used. In the
case of a deterministic policy, the function would always return the same action for a
given state. In the case of a stochastic policy. The goal of the learning algorithm is to
maximize the expected total reward over the game

## 1.2 LunarLander
1. State: represent the state of the spacecraft including the position, velocity and
direction
2. Actions: firing, which can take place in four directions (up, down, left, right)
3. Reward: the agent receives a positive reward when t moves closer to the landing
pad, and a negative reward when it moves away from the landing pad. The agent
gets the biggest reward when it lands successfully on the landing pad.
4. Agent: spacecraft
5. Environment: everything surrounding the agent as the landing pad.
6. Policy: sum of the probability distribution of all the actions in the action space
7. state transition function: takes as input the current state of the system and an action
or event that occurs, and outputs the new state of the system that results from that
action or event

- The policy can be formalized as a function that maps a state to an action. The policy
can be deterministic or stochastic, depending on the learning algorithm used. In the
case of a deterministic policy, the function would always return the same action for a
given state. In the case of a stochastic policy. The goal of the learning algorithm is to
maximize the expected total reward over the game

## 1.3 Model Based RL: Accessing Environment Dynamics

- ### Explain what the environment dynamics (i.e. reward function and state transition function) are and give at least two examples.
    Environment dynamics refers to changes in the state of the environment that affect the behaviour of an agent as:
1. reward function: it is a mathematical function that gives rewards to the agent after each
action whether positive or negative reward, it is used to define the goal of the agent and
guide it toward it.

2. state transition function: it is a mathematical function which use to express the change in
the state because an action takes place. The input is the current state and the action, output
is new state
- examples:
1. Game playing: the environment and the state will change depending on the agent’s
action, according to this action the agent will get a positive or negative reward. On the other
side, the state transition function will take the current state and the agent’s action and give
the new state as the output
2. Robot navigation: the environment and the state will change depending on the robot’s
action, according to this action the robot will get a positive or negative reward. On the other
side, the state transition function will take the current state and the agent’s action and give
the new state as the output
---

- ### Discuss: Are the environment dynamics generally known and can practically be used to solve a problem with RL?
In environments like OpenAI Gym, the environment dynamics are generally known and can be used to solve problems with RL. In this case, model-based RL methods would work well. However, real-life environments are uncertain and mostly unknown. So, in this case, it's better to use model-free RL methods. Environment dynamics can practically be used in RL. For example, we can train self-driving cars. RL can be used to learn the optimal driving policy by using the environment dynamics, such as road conditions, traffic patterns, and road signs, to determine the best driving actions at each step. By using model-based RL methods, these tasks can be accomplished more efficiently and effectively than with other approaches.
One practical example of using model-free RL is in recommender systems, where the goal is to recommend items to users based on their preferences. In this case, the environment dynamics are difficult to model due to the complex and constantly changing preferences of users. Instead of modeling the environment dynamics, model-free RL algorithms can learn to make recommendations based on previous user interactions with items. By using techniques such as Q-learning, the RL algorithm can learn to recommend items that maximize user satisfaction without requiring a full model of the environment dynamics. This approach has been successfully applied in real-world applications such as movie recommendations on Netflix and product recommendations on Amazon.