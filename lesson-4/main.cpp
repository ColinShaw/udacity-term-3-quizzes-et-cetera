#include "road.h"
#include "vehicle.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

int         SPEED_LIMIT            = 10;
vector<int> LANE_SPEEDS            = {6,7,8,9}; 
double      TRAFFIC_DENSITY        = 0.15;
int         MAX_ACCEL              = 2;
vector<int> GOAL                   = {300, 3};
int         FRAMES_PER_SECOND      = 4;
int         AMOUNT_OF_ROAD_VISIBLE = 40;

int main() {
	Road road = Road(SPEED_LIMIT, TRAFFIC_DENSITY, LANE_SPEEDS);
	road.update_width = AMOUNT_OF_ROAD_VISIBLE;
	road.populate_traffic();
	int goal_s = 300;
	int goal_lane = 3;
	int num_lanes = LANE_SPEEDS.size();
	vector<int> ego_config = {SPEED_LIMIT,num_lanes,goal_s,goal_lane,MAX_ACCEL};
	road.add_ego(2,0, ego_config);
	int timestep = 0;

	while (road.get_ego().s <= GOAL[0]) {
		timestep++;
		if (timestep > 150) {
			cout << "Taking too long to reach goal. Go faster!" << endl;
			break;
		}
		road.advance();
		road.display();
	}
	Vehicle ego = road.get_ego();
	if (ego.lane == GOAL[1])
	{
		cout << "You got to the goal in " << timestep << " seconds!" << endl;
	}
	else
	{
		cout << "You missed the goal. You are in lane " << ego.lane << " instead of " << GOAL[1] << endl;
	}
	return 0;
}
