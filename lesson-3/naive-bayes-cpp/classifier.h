#ifndef CLASSIFIER_H
#define CLASSIFIER_H
#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

class GNB {
public:
    vector<string> possible_labels = {"left","keep","right"};
    GNB();
    virtual ~GNB();
    void train(vector<vector<double> > data, vector<string>  labels);
    string predict(vector<double>);
};

#endif

