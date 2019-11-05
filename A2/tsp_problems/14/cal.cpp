#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	string input;
	float sum = 0;
	float sum2 = 0;
	int flag = 0;
	while(getline(cin,input)){
		istringstream s1{input};
		if(flag == 0){
			float num;
			s1 >> num;
			sum += num;
			flag = 1;
		}
		else{
			float num2;
			s1 >> num2;
			sum2 += num2;
			flag = 0;
		}
	}
	sum /= 100;
	sum2 /= 100;
	cout << sum << " " <<  sum2 << endl;
	return 0;
}
