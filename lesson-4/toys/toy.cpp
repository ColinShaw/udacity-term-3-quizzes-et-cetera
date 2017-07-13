#include <string.h>
#include <math.h>
#include <iostream>
#include <map>
#include <vector>
#include <iterator>
#include <utility>

using namespace std;

int main ()
{
    // Map of possible car operations and initial costs
    map<string, float> costs = { 
                                 {"KL",   0.0},
                                 {"LCL",  0.0},
                                 {"LCR",  0.0},
                                 {"PLCL", 0.0},
                                 {"PLCR", 0.0}
                               };
    float test = costs["KL"];

    cout << test << endl;

}
