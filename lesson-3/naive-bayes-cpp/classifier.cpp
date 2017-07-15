#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>
#include "classifier.h"

GNB::GNB() {}
GNB::~GNB() {}

void GNB::train(vector<vector<double>> data, vector<string> labels)
{

}

string GNB::predict(vector<double>)
{

    return this->possible_labels[1];
}
