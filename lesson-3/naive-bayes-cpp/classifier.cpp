nclude <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include <map>
#include "classifier.h"

GNB::GNB() { }

GNB::~GNB() { }

/*
    Trains the classifier with N data points and labels.

    INPUTS
    data - array of N observations
      - Each observation is a tuple with 4 values: s, d, 
        s_dot and d_dot.
      - Example : [
            [3.5, 0.1, 5.9, -0.02],
            [8.0, -0.3, 3.0, 2.2],
            ...
        ]

    labels - array of N labels
      - Each label is one of "left", "keep", or "right".
*/
void GNB::train(vector<vector<double>> data, vector<string> labels)
{
    // Compute mu by label and attribute
    for (int i=0; i<labels.size(); i++)
    {
        string label = labels[i];
        vector<double> attributes = data[i];
        for (int j=0; j<4; j++)
        {
            total_for_mu[label][j] += attributes[j];
            count[label][j] += 1.0;        
        }
    }
    for (int j=0; j<4; j++)
    {
        mu["left"][j] = total_for_mu["left"][j] / count["left"][j];
        mu["keep"][j] = total_for_mu["keep"][j] / count["keep"][j];
        mu["right"][j] = total_for_mu["right"][j] / count["right"][j];
    }
    
    // Compute standard deviation (for samples) by label and attribute   
    for (int i=0; i<labels.size(); i++)
    {
        string label = labels[i];
        vector<double> attributes = data[i];
        for (int j=0; j<4; j++)
        {
            double diff = mu[label][j] - attributes[j];
            total_for_sigma[label][j] += diff * diff;
        }
    }
    for (int j=0; j<4; j++)
    {
        sigma["left"][j] = sqrt(total_for_sigma["left"][j] / (count["left"][j] - 1.0));
        sigma["keep"][j] = sqrt(total_for_sigma["keep"][j] / (count["keep"][j] - 1.0));
        sigma["right"][j] = sqrt(total_for_sigma["right"][j] / (count["right"][j] - 1.0));
    }
    
}

/*
    Once trained, this method is called and expected to return 
    a predicted behavior for the given observation.

    INPUTS

    observation - a 4 tuple with s, d, s_dot, d_dot.
      - Example: [3.5, 0.1, 8.5, -0.2]

    OUTPUT

    A label representing the best guess of the classifier. Can
    be one of "left", "keep" or "right".
*/
    
string GNB::predict(vector<double> input)
{
    double highest_value = 0.0;
    string highest_label = "";
    
    for (int i=0; i<possible_labels.size(); i++)
    {
        string label = possible_labels[i];
        double total = 1.0;
        for (int j=0; j<4; j++)
        {
            double v = input[j];
            double m = mu[label][j];
            double s = sigma[label][j];
            cout << v << " - " << m << " - " << s << endl;
            total *= gaussian(v, m, s);
            cout << total << endl;
        }
        cout << endl;
        if (total > highest_value)
        {
            highest_value = total;
            highest_label = label;
        }
    }
    
    return highest_label;
}

double GNB::gaussian(double val, double mean, double sigma)
{
    if (sigma == 0.0)
        return 1.0;
    double den = sqrt(2.0 * M_PI * sigma * sigma);
    double ex = (val - mean) * (val - mean) / (2.0 * sigma * sigma);
    return exp(-1.0 * ex) / den;
}
    

