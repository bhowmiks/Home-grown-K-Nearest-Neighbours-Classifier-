import numpy as np
import random

def findDistance(p1,p2):
    '''Finds the distance between two points  on the co-ordinate plane'''
    return  np.sqrt(np.sum(np.power(p2-p1, 2)))


def majorityVote(votes):
    allVotes={}
    for vote in votes:
        if vote in allVotes:
            allVotes[vote] +=1
        else:
            allVotes[vote] = 1
    winners=[]
    highest=  max(allVotes.values())
    for Key, c in allVotes.items():
        if c==highest:
            winners.append(Key)

    return  random.choice(winners)


def findNearestNeighbours(points, p, k=5):
    '''Finds the nearest points for a given point p from a pool of points'''
    distances= np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i]=findDistance(points[i],p)
    indices= np.argsort(distances)
    return indices[:k]