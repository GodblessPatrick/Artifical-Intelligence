#include <iostream>
using namespace std;

int main(){
	cout << "#!/bin/sh" << endl;
	for (int i = 0;i < 100;i++){
		cout << "python tsp.py instance_10.txt" << endl;
	}
	return 0;
}
