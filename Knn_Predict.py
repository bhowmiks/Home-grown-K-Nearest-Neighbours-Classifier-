import  matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
from Knn_Utils import *

p=[1.5,-1] # the point to be classified


def generate_data(n):
    '''generates some data for demonstration'''
    points=np.concatenate((ss.norm(0,1).rvs((n,2)) , ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes= np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return points,outcomes

n=25
points,outcomes=generate_data(n)




def predict_knn(points, p, outcomes, k=5):
    '''Predicts the Nearest Neighbours'''
    nRes=findNearestNeighbours(points,p,k);
    return majorityVote(outcomes[nRes])


plt.figure()
plt.plot(points[:n,0],points[:n,1],"go")
plt.plot(points[n:,0],points[n:,1],"yo")
plt.plot(p[0],p[1],"rs")
result="Red point Belongs to group: " + str(predict_knn(points, p, outcomes, 3))
plt.xlabel(result)

plt.show()
print(predict_knn(points, p, outcomes, 3))  # prints  out the group to which the point belongs to.
