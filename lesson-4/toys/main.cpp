#include <string.h>
#include <math.h>
#include <iostream>
#include <map>
#include <vector>
#include <iterator>
#include <utility>

using namespace std;

    /*  predictions is a dictionary like this:
     *   {
     *     3 : [
     *       {"s" : 4, "lane": 0},
     *       {"s" : 6, "lane": 0},
     *       {"s" : 8, "lane": 0},
     *       {"s" : 10, "lane": 0},
     *     ]
     *   }
     */

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

    // Define vehicle predictions
    map<int, vector<vector<int>>> predictions = { 
                                                  {1, {{1,2},{3,4}}} ,
                                                  {1, {{1,2},{3,4}}} 
                                                };


    // Loop over the possible car operations and costs
    map<string, float>::iterator costs_iter = costs.begin();
    while (costs_iter != costs.end())
    {
    
        // Loop over the predictions
        map<int, vector<vector<int>>>::iterator pred_iter = predictions.begin();
        while (pred_iter != predictions.end())
        {
            int                 vehicle_id = pred_iter->first;
            vector<vector<int>> data       = pred_iter->second;

            int position = data[0][0];
            int lane     = data[0][1];
            int speed    = data[1][0] - data[0][0]; 

            // Compute cost for the particular car move 
            float cost = 0.0;
            string move = costs_iter->first;
                                  
            // Update the cost for this move
            costs[move] += cost;

            pred_iter++;
        }
      
        costs_iter++;
    }


    // Just some dumb stuff
    map<string, int> test;
    test["what"] = 10;
    cout << test["what"] << endl;

}
