import numpy as np
from sklearn.naive_bayes import GaussianNB

class GNB(object):

    def train(self, data, labels):
        data = np.array(data)
        labels = np.array(labels)
        self.nb = GaussianNB()
        self.nb.fit(data, labels)

    def predict(self, observation):
        return self.nb.predict([observation])
