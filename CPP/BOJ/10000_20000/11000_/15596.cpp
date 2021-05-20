#include <vector>
using namespace std;

long long sum(vector<int> &a) {
	int num = 0;
	for(int i = 0; i < a.size(); i++) {
		num += a[i];
	}
	
	return num;
}