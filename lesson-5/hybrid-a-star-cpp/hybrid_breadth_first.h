#ifndef HYBRID_BREADTH_FIRST_H_
#define HYBRID_BREADTH_FIRST_H_

#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

class HBF {
public:

    int NUM_THETA_CELLS = 90;
    double SPEED        = 1.45;
    double LENGTH       = 0.5;
    
    vector< vector<int> > heuristic = {
        {30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15},
        {29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14},
        {28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13},
        {27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12},
        {26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11},
        {25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10},
        {24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9},
        {23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8},
        {22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9, 8, 7},
        {21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8, 7, 6},
        {20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7, 6, 5},
        {19, 18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6, 5, 4},
        {18, 17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5, 4, 3},
        {17, 16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4, 3, 2},
        {16, 15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3, 2, 1},
        {15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2, 1, 0}
    };

    struct maze_s {
        int f;
        int g;
        int h;
        double x;
        double y;
        double theta;
    };

    struct maze_path {
        vector< vector< vector<maze_s> > > closed;
        vector< vector< vector<maze_s> > > came_from;
        maze_s final;
    };

    HBF();
    virtual ~HBF();
    int theta_to_stack_number(double theta);
    int idx(double float_num);
    vector<maze_s> expand(maze_s state);
    maze_path search(vector< vector<int> > grid, vector<double> start, vector<int> goal);
    vector<maze_s> reconstruct_path(vector< vector< vector<maze_s> > > came_from, vector<double> start, HBF::maze_s final);
};

#endif

