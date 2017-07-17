#ifndef CLASSIFIER_H
#define CLASSIFIER_H
#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include <map>

using namespace std;

class GNB {
public:

    vector<string> possible_labels = {"left","keep","right"};
    
    map<string, vector<double>> mu = { 
        {"left", {0.0, 0.0, 0.0, 0.0}},
        {"keep", {0.0, 0.0, 0.0, 0.0}},
        {"right", {0.0, 0.0, 0.0, 0.0}} 
    };
    
    map<string, vector<double>> sigma = { 
        {"left", {0.0, 0.0, 0.0, 0.0}},
        {"keep", {0.0, 0.0, 0.0, 0.0}},
        {"right", {0.0, 0.0, 0.0, 0.0}} 
    };
    
    map<string, vector<double>> count = { 
        {"left", {0.0, 0.0, 0.0, 0.0}},
        {"keep", {0.0, 0.0, 0.0, 0.0}},
        {"right", {0.0, 0.0, 0.0, 0.0}} 
    };
    
    map<string, vector<double>> total_for_mu = { 
        {"left", {0.0, 0.0, 0.0, 0.0}},
        {"keep", {0.0, 0.0, 0.0, 0.0}},
        {"right", {0.0, 0.0, 0.0, 0.0}} 
    };
    
    map<string, vector<double>> total_for_sigma = { 
        {"left", {0.0, 0.0, 0.0, 0.0}},
        {"keep", {0.0, 0.0, 0.0, 0.0}},
        {"right", {0.0, 0.0, 0.0, 0.0}} 
    };

    /**
    * Constructor
    */
    GNB();

    /**
    * Destructor
    */
    virtual ~GNB();

    void train(vector<vector<double> > data, vector<string>  labels);

    string predict(vector<double>);
    
    double gaussian(double, double, double);

};

#endif
