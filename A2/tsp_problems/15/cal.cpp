#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	string input;
	float sum = 0;
	while(getline(cin,input)){
		istringstream s1{input};
		int num;
		s1 >> num;
		float ratio =  num / 325;
		sum += ratio;
	}
	sum /= 100;
	cout << sum << endl;
	return 0;
}
