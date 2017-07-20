#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

#include "Dense"

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;

vector<double> JMT(vector< double> start, vector <double> end, double T)
{
    MatrixXd A = MatrixXd(3, 3);
    A <<   T*T*T,   T*T*T*T,  T*T*T*T*T,
         3*T*T,   4*T*T*T,  5*T*T*T*T,
         6*T,    12*T*T,   20*T*T*T;
        
    MatrixXd B = MatrixXd(3,1);     
    B << end[0] - (start[0] + start[1]*T + 0.5*start[2]*T*T),
         end[1] - (start[1] + start[2]*T),
         end[2] - start[2];
                
    MatrixXd Ai = A.inverse();
    MatrixXd C = Ai*B;
    
    vector <double> result = {start[0], start[1], 0.5 * start[2]};
    for(int i = 0; i < C.size(); i++)
    {
        result.push_back(C.data()[i]);
    }
    
    return result;
}

bool close_enough(vector< double > poly, vector<double> target_poly, double eps=0.01) 
{
    if(poly.size() != target_poly.size())
    {
        cout << "your solution didn't have the correct number of terms" << endl;
        return false;
    }
    for(int i = 0; i < poly.size(); i++)
    {
        double diff = poly[i]-target_poly[i];
        if(abs(diff) > eps)
        {
            cout << "at least one of your terms differed from target by more than " << eps << endl;
            return false;
        }
    }
    return true;
}
    
struct test_case {
    vector<double> start;
    vector<double> end;
    double T;
};

vector< vector<double> > answers = {{0.0, 10.0, 0.0, 0.0, 0.0, 0.0},{0.0,10.0,0.0,0.0,-0.625,0.3125},{5.0,10.0,1.0,-3.0,0.64,-0.0432}};

int main() {
    vector< test_case > tc;

    test_case tc1;
    tc1.start = {0,10,0};
    tc1.end   = {10,10,0};
    tc1.T     = 1;
    tc.push_back(tc1);

    test_case tc2;
    tc2.start = {0,10,0};
    tc2.end   = {20,15,20};
    tc2.T     = 2;
    tc.push_back(tc2);

    test_case tc3;
    tc3.start = {5,10,2};
    tc3.end   = {-30,-20,-4};
    tc3.T     = 5;
    tc.push_back(tc3);

    bool total_correct = true;
    for(int i = 0; i < tc.size(); i++)
    {
        vector< double > jmt = JMT(tc[i].start, tc[i].end, tc[i].T);
        bool correct = close_enough(jmt,answers[i]);
        total_correct &= correct;

    }
    if(!total_correct)
    {
        cout << "Try again!" << endl;
    }
    else
    {
        cout << "Nice work!" << endl;
    }

    return 0;
}
