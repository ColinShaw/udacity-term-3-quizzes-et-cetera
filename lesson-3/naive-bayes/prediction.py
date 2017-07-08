#!/usr/bin/env python

from classifier import GNB
import json



def main():

   gnb = GNB()

   with open('train.json', encoding='utf-8') as f:
       j = json.load(f)

   print(j.keys())

   X = j['states']
   Y = j['labels']

   gnb.train(X, Y)

   with open('test.json', encoding='utf-8') as f:
       j = json.load(f)

   X = j['states']
   Y = j['labels']

   score = 0

   for coords, label in zip(X,Y):
       predicted = gnb.predict(coords)

       if predicted == label:
           score += 1

   percent_correct = 100 * float(score) / len(X)
   print(str(percent_correct) + " percent correct.")



if __name__ == "__main__":
    main()
