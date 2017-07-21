import numpy as np
from sklearn import tree

class GNB(object):

    def train(self, data, labels):
        data = np.array(data)
        labels = np.array(labels)
        self.nb = tree.DecisionTreeClassifier()
        self.nb.fit(data, labels)

    def predict(self, observation):
        return self.nb.predict([observation])
