import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import random

gamma = 1 # discounting rate
rewardSize = -0.25
gridSize = 5
terminationStates = [[0,0], [gridSize-1, gridSize-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
numIterations = 1

def actionRewardFunction(initialPosition, action):
    
    if initialPosition in terminationStates:
        return initialPosition, 0
    
    reward = rewardSize
    #print("reward",reward)
    print("initial",initialPosition)
    print("action",action)
    finalPosition = np.array(initialPosition) + np.array(action)
    #print("finalPosition",finalPosition)
    if -1 in finalPosition or 5 in finalPosition: 
        finalPosition = initialPosition
        #print("finalPosition",finalPosition)
        
    return finalPosition, reward

valueMap = np.zeros((gridSize, gridSize))
print("valuemap",range(gridSize))
states = [[i, j] for i in range(gridSize) for j in range(gridSize)]
print("'States",states)
valueMap
deltas = []
for it in range(numIterations):
    copyValueMap = np.copy(valueMap)
    deltaState = []
    for state in states:
        print("--------------new State--------\n",state)
        weightedRewards = 0
        actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for action in actions:
            print("action",action)
            #print("length",(1/len(actions)))
            finalPosition, reward = actionRewardFunction(state, action)
            print("reward",reward)
            #print("finalPosition[0]",finalPosition[0])
            #print("finalPosition[1]",finalPosition[1])
            print("valueMap[finalPosition[0], finalPosition[1]",valueMap[finalPosition[0], finalPosition[1]])

            weightedRewards += ((1/len(actions))*(reward+(gamma*valueMap[finalPosition[0], finalPosition[1]])))
            print("weightedvalue",weightedRewards)
            print("copyValueMap[state[0], state[1]]",copyValueMap[state[0], state[1]])
            #deltaState.append(np.abs(copyValueMap[state[0], state[1]]-weightedRewards))
            #deltaState.append(np.abs(-1 + weightedRewards))
           #print("deltaState",deltaState)
            copyValueMap[state[0], state[1]] = -1+ weightedRewards
            #deltas.append(deltaState)
            valueMap = copyValueMap
    if it in [0,1,2,9, 99, numIterations-1]:
        print("Iteration {}".format(it))
        print(valueMap)
        print("")