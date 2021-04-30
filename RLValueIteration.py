import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import random

gamma = 1 # discounting rate
rewardSize = -1
gridSize = 5
terminationStates = [[0,0], [gridSize-1, gridSize-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
numIterations = 6

def actionRewardFunction(initialPosition, action):
    
    if initialPosition in terminationStates:
        return initialPosition, 0
    
    reward = rewardSize
    #print("reward",reward)
    #print("initial",initialPosition)
    #print("action",action)
    finalPosition = np.array(initialPosition) + np.array(action)
    #print("finalPosition",finalPosition)
    if -1 in finalPosition or 5 in finalPosition: 
        finalPosition = initialPosition
        #print("finalPosition",finalPosition)
        
    return finalPosition, reward

valueMap = np.zeros((gridSize, gridSize))
#print("valuemap",range(gridSize))
states = [[i, j] for i in range(gridSize) for j in range(gridSize)]
#print("'States",states)
deltas = []
for it in range(numIterations):
    copyValueMap = np.copy(valueMap)
    #print("valueMap",copyValueMap)
    
    for state in states:
        #print("--------------new State--------\n",state)
        weightedRewards = 0
        statevalue =0
        deltaState = []
        for action in actions:
            #print("action",action)
            #print("length",(1/len(actions)))
            finalPosition, reward = actionRewardFunction(state, action)
            deltaState.append(reward+(gamma*valueMap[finalPosition[0], finalPosition[1]]))
            #print("the value of deltaState",deltaState) 
        weightedRewards =max(deltaState) 
        #print("weightedRewards",weightedRewards)
        copyValueMap[state[0], state[1]] = weightedRewards
        
    valueMap = copyValueMap
    if it in [0,1,2,3,4,5,9,  numIterations-1]:
        print("Iteration {}".format(it+1))
        print(valueMap)
        print("")