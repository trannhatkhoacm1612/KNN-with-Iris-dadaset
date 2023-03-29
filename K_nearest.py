import numpy as np
from collections import Counter

class KNN:
    def __init__(self,k):
        self.k = k
    def fit(self,X,Y):
        self.X_train = X
        self.Y_train = Y
    def euclid_dis(self,X):
        return np.sqrt(np.sum((self.X_train - X)**2, axis = 1))
    def predict(self,X):
        distances = self.euclid_dis(X)
        nearest = np.argsort(distances)[:self.k]
        labels = self.Y_train[nearest]
        return Counter(labels).most_common(1)[0][0]

    

        