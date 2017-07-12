#include <string.h>
#include <iostream>
#include <map>
#include <utility>

using namespace std;

int main ()
{
  map<string, int> test;
  
  test["what"] = 10;

  cout << test["what"] << endl;

}
